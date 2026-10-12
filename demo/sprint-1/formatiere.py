"""
Ausgabe-Aufbereitung für die Sprint-1-Vorführung

Macht aus den JSON-Antworten der API eine Darstellung, die am Beamer lesbar
ist. Rechnet nichts aus und ruft nichts ab: jeder angezeigte Wert steht so in
der Antwort des Servers, diese Datei ordnet ihn nur an.

Bewusst getrennt von demo.sh, damit beim Vorführen sichtbar bleibt, welcher
Teil die API aufruft und welcher nur formatiert.
"""

import json
import sys

FETT = "\033[1m"
GRAU = "\033[2m"
AUS = "\033[0m"

LABELS = {
    "product_name": "Produktname",
    "description": "Beschreibung",
    "ean": "EAN",
    "manufacturer_sku": "Hersteller-Nr.",
    "supplier_sku": "Lieferanten-Nr.",
    "brand": "Marke",
    "weight_grams": "Gewicht",
    "length_mm": "Länge",
    "width_mm": "Breite",
    "height_mm": "Höhe",
    "price_centimes": "Preis",
    "dimensions": "Masse",
}

EINHEITEN = {
    "weight_grams": "g",
    "length_mm": "mm",
    "width_mm": "mm",
    "height_mm": "mm",
}

VERTRAUEN = {"high": "hoch", "medium": "mittel", "low": "tief"}


def wert_mit_einheit(key, wert):
    if wert is None:
        return "—"
    if key == "price_centimes":
        try:
            return f"{int(wert) / 100:.2f} CHF"
        except (TypeError, ValueError):
            return str(wert)
    einheit = EINHEITEN.get(key)
    return f"{wert} {einheit}" if einheit else str(wert)


def upload(d):
    print(f"  Dokument-ID   {d['id']}")
    print(f"  Dateiname     {d['filename']}")
    print(f"  Grösse        {d['byte_size']:,} Bytes".replace(",", "’"))
    print(f"  Hochgeladen   {d['uploaded_by']}")
    print(f"  Status        {d['status']}")
    print()
    print(f"{GRAU}  Die Datei liegt im Dateispeicher, der Datensatz in PostgreSQL.{AUS}")
    print(f"{GRAU}  Wer hochgeladen hat, steht im Protokoll (DA-9).{AUS}")
    print()
    print("  Weiter mit: ./demo.sh extract")


def extract(d):
    print(f"  Produktvorschläge   {d['proposals_created']}")
    print(f"  Modellaufrufe       {d['model_calls']}")
    print(f"  Token hinein        {d['input_tokens']:,}".replace(",", "’"))
    print(f"  Token heraus        {d['output_tokens']:,}".replace(",", "’"))
    print(f"  Nachbesserungen     {d['repairs_applied']} von {d['repairs_requested']} angefragt")
    print(f"  Eskaliert           {'ja' if d['escalated'] else 'nein'}")
    print()
    if d["model_calls"] == 1:
        print(f"{GRAU}  Ein einziger Modellaufruf. Verankern, Vereinheitlichen und Prüfen{AUS}")
        print(f"{GRAU}  sind Regeln und kosten kein Modell (DA-7, DA-8).{AUS}")
    print()
    print("  Weiter mit: ./demo.sh show")


def show(vorschlaege):
    gesamt = 0
    mit_fundstelle = 0

    for nummer, p in enumerate(vorschlaege, start=1):
        name = p.get("product_name") or "(ohne Namen)"
        print(f"{FETT}  {nummer}. {name}{AUS}")
        print()

        for f in p["fields"]:
            if f["extracted_value"] is None and f["source_text"] is None:
                continue

            gesamt += 1
            label = LABELS.get(f["key"], f["key"])
            wert = wert_mit_einheit(f["key"], f["extracted_value"])
            print(f"     {label:<17}{wert}")

            if f["source_text"]:
                mit_fundstelle += 1
                zitat = f["source_text"]
                if len(zitat) > 46:
                    zitat = zitat[:45] + "…"
                r = f.get("source_region")
                ort = (
                    f"S.{r['page']}  {r['left']:.1f}% / {r['top']:.1f}%"
                    if r
                    else f"S.{f['source_page']}"
                    if f.get("source_page")
                    else ""
                )
                print(f'     {GRAU}{"":<17}← „{zitat}"  {ort}{AUS}')
            else:
                print(f'     {GRAU}{"":<17}← keine Fundstelle{AUS}')

        fehlend = [
            LABELS.get(f["key"], f["key"])
            for f in p["fields"]
            if f["extracted_value"] is None and f["source_text"] is None
        ]
        if fehlend:
            print()
            print(f"     {GRAU}Nicht im Dokument: {', '.join(fehlend)}{AUS}")

        print()

    print(f"  {FETT}{len(vorschlaege)} Produkte, {gesamt} Werte, "
          f"{mit_fundstelle} davon mit Fundstelle{AUS}")
    print()
    print(f"{GRAU}  Das Zitat nennt das Modell. Das Rechteck misst pdfium im Dokument —{AUS}")
    print(f"{GRAU}  die Geometrie stammt also aus dem PDF, nicht aus dem Modell.{AUS}")


URTEILE = {
    "correct": "korrekt",
    "wrong": "falsch",
    "missing": "fehlend",
    "invented": "erfunden",
}


def accuracy(d):
    erwartet = d["expected_total"]
    correctness = d["correctness_percent"]
    anchor_rate = d["anchor_rate_percent"]

    print(f"  Testdatensatz    {d['filename']}")
    if d.get("source"):
        print(f"  Herkunft         {d['source']}")
    print()

    print(f"  Erwartete Werte  {erwartet}")
    print(f"  Korrekt          {FETT}{d['correct']}{AUS}")
    print(f"  Falsch           {d['wrong']}")
    print(f"  Fehlend          {d['missing']}")
    print(f"  Erfunden         {d['invented']}")
    print()

    if correctness is not None:
        erreicht = "erreicht" if d["meets_target"] else "verfehlt"
        print(f"  {FETT}Correctness      {correctness:.1f} %{AUS}"
              f"   (Ziel {d['target_percent']:.0f} %, {erreicht})")
    if anchor_rate is not None:
        print(f"  Mit Fundstelle   {d['anchored']} von {erwartet} ({anchor_rate:.2f} %)")
    print(f"  Produkte         {d['products_matched']} von {d['products_expected']} erkannt")
    print()

    for p in d["products"]:
        haken = "✓" if p["matched"] else "✗"
        gesamt = len(p["fields"])
        mit_fundstelle = sum(1 for f in p["fields"] if f["anchored"])
        print(f"  {haken} {p['name']:<28}{p['correct']}/{gesamt} korrekt"
              f"   {mit_fundstelle}/{gesamt} mit Fundstelle")

        for f in p["fields"]:
            if f["verdict"] == "correct" and f["anchored"]:
                continue

            label = LABELS.get(f["key"], f["key"])
            urteil = URTEILE.get(f["verdict"], f["verdict"])
            zusatz = "" if f["anchored"] else ", ohne Fundstelle"
            print(f"       {GRAU}{label:<17}{urteil}{zusatz}{AUS}")

    print()
    if d["invented"] == 0:
        print(f"{GRAU}  Kein erfundener Wert. Was nicht im Dokument steht, wurde als{AUS}")
        print(f"{GRAU}  fehlend gemeldet statt plausibel ergänzt.{AUS}")
    print(f"{GRAU}  Die Sollwerte sind von Hand abgelesen und über die Prüfsumme des{AUS}")
    print(f"{GRAU}  Dokuments zugeordnet, nicht über den Dateinamen.{AUS}")


def reset(d):
    print(f"  Gelöscht: {d['documents']} Dokumente, "
          f"{d['proposals']} Vorschläge, {d['products']} Produkte")


def main():
    was = sys.argv[1] if len(sys.argv) > 1 else ""
    daten = json.load(sys.stdin)

    print()
    {
        "upload": upload,
        "extract": extract,
        "show": show,
        "accuracy": accuracy,
        "reset": reset,
    }[was](daten)
    print()


if __name__ == "__main__":
    main()
