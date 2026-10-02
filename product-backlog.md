# PIMFLOW — Product Backlog

Diplomarbeit ITCNE24 · David Unterguggenberger · Ambit IQ
Stand: 07.09.2026 · Entwurf zur Prüfung vor der Übertragung nach Linear

---

## Rahmen

| | |
|---|---|
| Offizieller Beginn | Montag, 14.09.2026 |
| Abgabe | Freitag, 18.12.2026 |
| Vorgehen | Scrum, drei Sprints |
| Board | Linear, Team *Diplomarbeit*, drei Cycles |

### Sprints und Meilensteine

| Sprint | Zeitraum | Dauer | Story Points | Zwischenpräsentation |
|---|---|---|---|---|
| 1 — Fundament und Extraktion | Mo 14.09. – So 11.10.2026 | 4 Wochen | 51 | **ZP1: Mo 19.10., 11:30–12:00** |
| 2 — Qualität, Bilder und Shop | Mo 12.10. – So 08.11.2026 | 4 Wochen | 55 | **ZP2: Mo 16.11., 11:30–12:00** |
| 3 — PIMFLOW Oberfläche | Mo 09.11. – So 06.12.2026 | 4 Wochen | 59 | **ZP3: Mo 14.12., 11:30–12:00** |
| Abgabephase | Mo 07.12. – Fr 18.12.2026 | 2 Wochen | — | **Abgabe: Fr 18.12.** |

**Alle drei Sprints sind exakt gleich lang (je vier Wochen)** und schliessen
lückenlos aneinander an. Das ist die Voraussetzung dafür, die Velocity über den
gesamten Projektverlauf hinweg zu vergleichen: Bei ungleich langen Sprints sagt
eine höhere Punktzahl nur, dass mehr Zeit zur Verfügung stand.

Die Zwischenpräsentationen finden jeweils **acht Tage nach Sprint-Ende** statt.
Dieser Abstand ist eingeplant und dient der Aufbereitung des Sprint Reviews sowie
der Auswertung des Burndown-Charts. Der Sprint ist zum Zeitpunkt der Präsentation
bereits abgeschlossen, die Zahlen stehen fest.

Die verbleibenden zwei Wochen vom 07. bis 18.12. sind bewusst kein Sprint, sondern
Abgabephase: Fertigstellung der Dokumentation, Schlusspräsentation und Abgabe des
Quellcodes (siehe DA-30).

Die Punkteverteilung liegt mit 51 / 55 / 59 innerhalb von ±7 % um den Mittelwert
von 55. Eine weitere Angleichung würde die fachliche Reihenfolge zerreissen: Die
Messung der Extraktionsgüte (DA-19) setzt die Extraktion voraus, die
Fundstellen-Anzeige (DA-23) die Berechnung der Koordinaten (DA-7).

### Umsetzung in Linear

Die drei Sprints sind als **Cycles** im Team *Diplomarbeit* abgebildet (Cycle 1–3,
Präfix `TBZ`). Linear zeichnet daraus je Sprint automatisch Burndown-Chart und
Velocity. Vier Wochen Cycle-Länge, kein Cooldown, Start Montag 14.09.2026.

Die Automatik „Completed issues" bleibt ausgeschaltet, damit eine nachträglich
abgeschlossene Aufgabe nicht in einen späteren Sprint wandert und dadurch beide
Burndown-Charts verfälscht. Der Sprint-Umfang bleibt während des laufenden Sprints
stabil.

### Abweichung von der Projektbeschreibung

Die unterschriebene Projektbeschreibung sieht die Oberfläche in Sprint 2 und die
Shopify-Integration in Sprint 3 vor. Das Board dreht diese Reihenfolge um: **die
ersten beiden Sprints bauen ausschliesslich Backend, KI und Shopify**, sodass zur
ZP2 ein vollständiger Ablauf vom Lieferantendokument bis zum angelegten Produkt im
Shop vorführbar ist, und zwar über die API, ohne Oberfläche. Sprint 3 setzt die Oberfläche
darauf.

Begründung: Der fachliche Kern der Arbeit ist die KI-gestützte Extraktion. Steht
dieser früh und ist messbar, bleibt für die Oberfläche ein ganzer Sprint mit
bekannter Datenlage. Umgekehrt wäre eine Oberfläche ohne belastbare Extraktion
gebaut worden.

Diese Umpriorisierung wird in der Dokumentation als bewusste Entscheidung
festgehalten und im Sprint Review begründet.

### Abgrenzung: was in Sprint 1 und 2 ausdrücklich nicht gebaut wird

**In den Sprints 1 und 2 entsteht keine einzige Zeile Oberflächencode.** Beide
Sprints liefern ausschliesslich:

- Fachlogik und Datenhaltung im Rust-Backend
- die KI-gestützte Extraktion über die Claude API
- die Anbindung an den Shopify-Shop

Jede Anforderung dieser beiden Sprints gilt als erfüllt, wenn sie **über die
HTTP-API nachweisbar** ist, geprüft mit `curl` oder einem Integrationstest. Der
Shopify-Shop ist in dieser Phase die einzige sichtbare Oberfläche, und er wird
nicht von uns gebaut, sondern über die Shopify API befüllt.

Konkret **nicht** Gegenstand von Sprint 1 und 2:

- kein React, kein Vite, kein Tailwind, keine Komponenten
- keine Darstellung von Fundstellen auf dem Dokument (das ist DA-23 in Sprint 3)
- keine Formulare, Tabellen, Fortschrittsbalken oder Schaltflächen
- keine Benutzerführung jeglicher Art

Wo eine Story dieser Sprints aus der Sicht eines Fachmitarbeiters formuliert ist,
beschreibt sie **den fachlichen Nutzen, nicht dessen Darstellung**. Die Rolle
benennt, wem das Ergebnis dient; geliefert wird die API dahinter. Die zugehörige
Oberfläche folgt in Sprint 3 und ist dort als eigene Story geführt.

**Vorführung zur ZP1 und ZP2** erfolgt daher über API-Aufrufe und den
Shopify-Shop, nicht über eine eigene Weboberfläche.

### Story Points

Fibonacci: 1, 2, 3, 5, 8. **Keine Story über 8 Punkten**, grössere Themen sind
zerlegt. (Konsequenz aus der Rückmeldung zur SA5, wo eine 13-Punkte-Story zu gross
geriet.)

### Abdeckung des Bewertungsrasters

Merkblatt A bewertet in sieben Bereichen. Diese Zuordnung zeigt, welche Tickets
darauf einzahlen, und wo die Bewertung ausserhalb des Backlogs stattfindet.

| Bereich | Kriterium | Abgedeckt durch |
|---|---|---|
| 1 Wissen | Fachwissen, Hintergründe, neu erarbeitetes Wissen | DA-6, DA-7, DA-16 (Modellanbindung, pdfium, Websuche) |
| 2 Praktische Arbeiten | Infrastruktur, technische Umsetzung | DA-1, DA-4, DA-18 |
| 2 Praktische Arbeiten | **Schulung / Schulungsunterlagen** | **DA-31** |
| 3 Intellektuelle Fähigkeiten | Problemdiagnose, Zusammenhänge, Urteilsvermögen | DA-8, DA-11, DA-19, DA-32 |
| 4 Organisatorische Fähigkeiten | Projektabwicklung, Steuerung | Cycles 1–3, Burndown je Sprint |
| 4 Organisatorische Fähigkeiten | Wöchentlicher Statusbericht | *entfällt laut Projektbeschreibung*, ersetzt durch **DA-33** und die drei Zwischenpräsentationen |
| 4 Organisatorische Fähigkeiten | Zwischenpräsentationen | ZP1–ZP3, je acht Tage nach Sprint-Ende |
| 5 Soziale Kompetenzen | Zusammenarbeit, Ausdauer | Zusammenarbeit mit Firmenexperte, **DA-33** |
| 6 Präsentation & Dokumentation | Dokumentation, Kolloquium, Management Summary | **DA-30** |
| 7 Zielerreichung | Umsetzung der definierten Ziele | **DA-19** (Correctness ≥ 99 %), Sprint Goals |

Weitere Pflichtinhalte aus Merkblatt A: Wirtschaftlichkeitsbetrachtung (**DA-32**),
agile Projektdokumentation (**DA-33**, **DA-30**), Einführung und Schulung von
Nutzenden (**DA-31**).

**Offener Punkt:** Die Projektbeschreibung hält fest, dass auf wöchentliche
Statusberichte verzichtet wird. Das Bewertungsraster führt sie jedoch als eigenes
Kriterium. Der Verzicht ist mit dem Schulexperten vereinbart und unterschrieben; an
ihrer Stelle stehen das fortlaufende Projektjournal und die drei
Zwischenpräsentationen.

### Definition of Done

Gilt einheitlich für jedes Ticket:

- [ ] Code oder Konfiguration funktioniert und wurde getestet
- [ ] `cargo fmt --check`, `cargo clippy -- -D warnings` und `cargo test` sind sauber
  (Frontend: `tsc`, `oxlint`, `build`)
- [ ] Code ist in Git committed und gepusht, in atomaren Commits
- [ ] Dokumentation erstellt oder aktualisiert
- [ ] Keine bekannten Bugs oder offenen Fehler

---

# Sprint 1 — Fundament und Extraktion

**Mo 14.09. – So 11.10.2026 · 4 Wochen · 11 Tickets · 51 Story Points**

**Sprint Goal:** Ein Lieferantendokument kann hochgeladen werden, wird von einem
Sprachmodell gelesen und liefert strukturierte Produktvorschläge, bei denen jeder
Wert auf die Stelle im Dokument zeigt, aus der er stammt.

**Umfang: ausschliesslich Backend und KI.** Kein Oberflächencode.

**Vorführbar zur ZP1** über `curl` gegen die API: PDF hochladen, Extraktion
auslösen, Vorschläge mit Konfidenz und Fundstellen-Koordinaten als JSON abrufen.

---

## DA-1 · Projektfundament aufsetzen

**Als** Software Engineer
**möchte ich** ein lauffähiges Projektgerüst mit typisierter Konfiguration
**damit** jede weitere Arbeit auf einer verlässlichen Grundlage aufsetzt.

**Story Points: 3**

### Beschreibung

Rust-Projekt mit axum als HTTP-Schicht, PostgreSQL in Docker und einer
Konfiguration, die beim Start einmal aus der Umgebung gelesen und validiert wird.
Fehlt ein Wert oder ist er unbrauchbar, bricht der Prozess sofort ab und benennt
die Variable, statt später beim ersten Zugriff zu scheitern.

Betrifft `src/main.rs`, `src/config.rs`, `docker-compose.yml`.

### Akzeptanzkriterien

- [ ] `docker compose up -d` startet die Datenbank auf Port 5442
- [ ] `cargo run` startet den Dienst; `GET /api/health` antwortet mit `ok`
- [ ] Konfiguration wird in eine typisierte Struktur gelesen, nicht als Strings verteilt
- [ ] Fehlt `ANTHROPIC_API_KEY`, bricht der Start ab und nennt die Variable
- [ ] Geheimnisse werden in `Debug`-Ausgaben redigiert und erscheinen in keinem Log
- [ ] `.env.example` dokumentiert jede Variable

---

## DA-2 · Schichtenarchitektur festlegen

**Als** Software Engineer
**möchte ich** eine Architektur, in der die Abhängigkeiten nach innen zeigen
**damit** die Fachlogik ohne Datenbank und ohne Netzwerk testbar bleibt.

**Story Points: 3**

### Beschreibung

Vier Schichten: `domain` (Entitäten, Wertobjekte, Regeln, Ports), `application`
(Anwendungsfälle), `infrastructure` (PostgreSQL, Claude, Dateisystem), `api`
(HTTP). Die Domäne definiert Traits; die Infrastruktur implementiert sie.

Betrifft `src/domain/ports.rs` und den Modulschnitt.

### Akzeptanzkriterien

- [ ] Die vier Schichten existieren als Module
- [ ] `domain` importiert weder `infrastructure` noch `api`
- [ ] Persistenz, Dateiablage und Extraktion sind als Traits in `domain/ports.rs` definiert
- [ ] Mindestens ein Anwendungsfall ist mit einem Test-Double ohne Datenbank getestet
- [ ] Jede Datei trägt einen Kopfkommentar, der ihre Rolle in der Architektur benennt

---

## DA-3 · Produktdaten als Typen modellieren

**Als** Software Engineer
**möchte ich** Fachwerte als eigene Typen statt als Zeichenketten
**damit** ungültige Zustände gar nicht erst darstellbar sind.

**Story Points: 5**

### Beschreibung

Bezeichner als Newtypes (`ProductId`, `ProposalId`), Masse als `Grams` und
`Millimetres`, Preise als `Money` in ganzen Rappen. Eingaben werden einmal an der
Grenze in gültige Typen überführt und danach nicht mehr geprüft.

Betrifft `src/domain/ids.rs`, `money.rs`, `measurement.rs`, `product.rs`, `actor.rs`.

### Akzeptanzkriterien

- [ ] Bezeichner sind Newtypes; drei nackte `Uuid` als Argumente sind nicht möglich
- [ ] `Money` rechnet in ganzen Rappen, nie in Fliesskomma
- [ ] `Grams::parse` und `Millimetres::parse` liefern bei unlesbarer Eingabe einen Fehler, keinen Standardwert
- [ ] Ein Handelnder (`Actor`) ist nicht leer und höchstens 120 Zeichen lang
- [ ] Fehler nutzen `thiserror` mit typisierten Varianten
- [ ] Unit-Tests decken Grenzfälle ab: leer, negativ, überlang, Komma statt Punkt

---

## DA-4 · Produktdaten dauerhaft speichern

**Als** Software Engineer
**möchte ich** Dokumente, Vorschläge und Produkte in PostgreSQL ablegen
**damit** ein Neustart des Dienstes keine Arbeit vernichtet.

**Story Points: 5**

### Beschreibung

Migrationen, die beim Start automatisch laufen, und Repositories, die das gesamte
SQL einer Tabelle kapseln. Ausschliesslich parametrisierte Abfragen.

Betrifft `migrations/pimflow/`, `src/infrastructure/db/`.

### Akzeptanzkriterien

- [ ] Migrationen laufen beim Start automatisch
- [ ] Tabellen für `supplier_documents`, `extractions`, `proposals`, `proposal_fields`, `products`
- [ ] Jede Abfrage ist parametrisiert; kein SQL wird aus Zeichenketten zusammengesetzt
- [ ] Repositories implementieren die Traits aus `domain/ports.rs`
- [ ] Eine Entscheidung trägt per Datenbank-Constraint immer Zeitpunkt **und** handelnde Person
- [ ] Integrationstests laufen gegen eine echte Datenbank und legen je Test ein eigenes Schema an

---

## DA-5 · Lieferantendokument hochladen

**Als** Fachmitarbeiter im Produktdatenmanagement
**möchte ich** ein Datenblatt als PDF hochladen
**damit** die enthaltenen Produktdaten maschinell gelesen werden können.

**Story Points: 5**

### Beschreibung

Multipart-Upload mit Prüfung der Datei, Ablage im Dateispeicher und Eintrag in der
Datenbank. Eine bereits hochgeladene Datei wird anhand ihrer Prüfsumme erkannt.

Betrifft `src/application/upload_document.rs`, `src/api/handlers/documents.rs`.

### Akzeptanzkriterien

- [ ] `POST /api/documents` nimmt eine PDF-Datei als Multipart entgegen
- [ ] Der Dateityp wird an den Magic Bytes (`%PDF-`) erkannt, nicht am gemeldeten Content-Type
- [ ] Dateien über 25 MB werden mit HTTP 413 abgewiesen
- [ ] Eine inhaltsgleiche Datei (SHA-256) wird mit HTTP 409 abgewiesen und nennt das bestehende Dokument
- [ ] Jeder Upload nennt die hochladende Person; ohne Namen HTTP 400
- [ ] `GET /api/documents/{id}/file` liefert die Originaldatei zurück
- [ ] Integrationstests decken alle Abweisungsfälle ab

---

## DA-6 · Produktdaten mit einem Sprachmodell auslesen

**Als** Fachmitarbeiter im Produktdatenmanagement
**möchte ich** die Produktdaten automatisch aus dem Dokument gelesen bekommen
**damit** ich sie nicht Feld für Feld abtippen muss.

**Story Points: 8**

### Beschreibung

Das PDF wird der Claude API übergeben, die je erkanntem Produkt einen Satz Felder
zurückliefert. Die Antwort ist über ein Schema erzwungen, damit sie nicht als
Freitext ankommt. Zu jedem Wert meldet das Modell seine Konfidenz und den
wörtlichen Textausschnitt, aus dem es den Wert gelesen hat.

Betrifft `src/infrastructure/claude/`, `src/application/extract_document.rs`.

### Akzeptanzkriterien

- [ ] `POST /api/documents/{id}/extract` liest das Dokument und legt je Produkt einen Vorschlag an
- [ ] Ausgelesen werden: Produktname, Beschreibung, EAN, Hersteller-Nr., Lieferanten-Nr., Marke, Gewicht, Länge, Breite, Höhe, Preis
- [ ] Felder, die keiner dieser Kategorien entsprechen, werden als freie Attribute übernommen
- [ ] Je Feld werden Konfidenz (high/medium/low/missing) und Fundstellen-Zitat mitgeführt
- [ ] Jeder ausgehende Aufruf hat ein Zeitlimit; bei 429 und 5xx wird mit wachsendem Abstand wiederholt
- [ ] Verbrauchte Token, Anzahl Aufrufe und Dauer werden je Extraktion gespeichert
- [ ] Der API-Schlüssel erscheint in keiner Log-Ausgabe
- [ ] Eine unlesbare Modellantwort führt zu einem typisierten Fehler, nicht zu einem Absturz

---

## DA-7 · Fundstelle im Dokument belegen

**Als** Software Engineer
**möchte ich** zu jedem ausgelesenen Wert die Fundstelle im Dokument als Koordinaten ermitteln
**damit** später belegt werden kann, woher der Wert stammt.

**Story Points: 8**

### Beschreibung

Das Modell meldet den Wortlaut, aus dem es einen Wert gelesen hat. Anschliessend
wird dieser Wortlaut mit pdfium im Dokument gesucht und das umschliessende Rechteck
vermessen. **Die Geometrie stammt damit aus dem Dokument, nie aus dem Modell.**

Ein Zitat, das sich nicht finden lässt, wird als Befund vermerkt. Denn ein Wert,
auf den das Modell nicht zeigen kann, stand möglicherweise nie auf der Seite.

> **Abgrenzung:** Diese Story liefert ausschliesslich die **Berechnung und
> Speicherung** der Koordinaten sowie deren Ausgabe über die API. Die grafische
> Hervorhebung auf dem Dokument ist Gegenstand von DA-23 in Sprint 3.

Betrifft `src/application/pipeline/anchor.rs`, `src/infrastructure/pdf/anchor.rs`.

### Akzeptanzkriterien

- [ ] Zu jedem Feld mit Zitat werden Seite und Rechteck (oben, links, Breite, Höhe) ermittelt
- [ ] Koordinaten sind seitenrelativ in Prozent, damit sie von einer späteren Darstellungsgrösse unabhängig sind
- [ ] Das Seitenverhältnis wird mitgeführt, damit die Fläche in Sprint 3 massstabsgetreu gezeichnet werden kann
- [ ] Ein nicht auffindbares Zitat erzeugt einen Befund und keinen leeren Bereich
- [ ] pdfium wird als Singleton hinter einem Mutex betrieben, da die Bibliothek keine zweite Bindung zulässt
- [ ] Die Suche toleriert abweichende Leerzeichen und Zeilenumbrüche
- [ ] Die Koordinaten sind über die API abrufbar und per `curl` nachweisbar
- [ ] Unit-Tests belegen Treffer, Fehltreffer und mehrseitige Dokumente

---

## DA-8 · Werte vereinheitlichen und prüfen

**Als** Fachmitarbeiter im Produktdatenmanagement
**möchte ich** dass offensichtlich falsche Werte markiert werden
**damit** ich meine Prüfung auf die zweifelhaften Stellen richten kann.

**Story Points: 5**

### Beschreibung

Nach der Extraktion laufen zwei Schritte ohne Modell: Einheiten werden vereinheitlicht
(kg → g, cm → mm, Preis → Rappen), danach greifen Regeln: EAN-Prüfziffer,
Plausibilitätsgrenzen, Pflichtfelder.

**Ein Regelergebnis schlägt die Selbsteinschätzung des Modells in beide Richtungen.**
Das gibt der Konfidenz eine überprüfbare Grundlage statt einer behaupteten.

Betrifft `src/application/pipeline/normalise.rs`, `validate.rs`, `split_dimensions.rs`.

### Akzeptanzkriterien

- [ ] Gewichte werden zu Gramm, Längen zu Millimetern, Preise zu ganzen Rappen vereinheitlicht
- [ ] Eine kombinierte Massangabe („12,5 x 8,4 x 5,1 cm") wird per Regel in Länge, Breite und Höhe zerlegt
- [ ] Die EAN-13-Prüfziffer wird gerechnet; eine falsche Prüfziffer erzeugt einen Befund
- [ ] Unplausible Werte erzeugen Befunde: Gewicht über 200 kg, Länge über 10 m, Preis über 100 000 CHF
- [ ] Befunde tragen einen Schweregrad: `Rejected` (unbrauchbar) oder `Suspect` (fragwürdig)
- [ ] Ein Befund senkt die Konfidenz des betroffenen Feldes
- [ ] Die Vereinheitlichung ist idempotent: zweimal angewandt ändert sich nichts
- [ ] Ein unlesbarer Wert wird gemeldet und bleibt erhalten, statt verworfen zu werden

---

## DA-9 · Jede Handlung nachvollziehbar protokollieren

**Als** Fachmitarbeiter im Produktdatenmanagement
**möchte ich** dass festgehalten wird, wer wann was getan hat
**damit** jede Freigabe später auf eine Person zurückgeführt werden kann.

**Story Points: 3**

### Beschreibung

Ein Protokoll, das nicht nur die handelnde Person festhält, sondern auch, ob sie
selbst gehandelt hat oder ein Modell in ihrem Auftrag. Ein vom Modell gelesener
Wert ist keine Entscheidung der Person, und das Protokoll muss beides unterscheiden
können.

Betrifft `src/infrastructure/db/audit_log.rs`, `src/domain/actor.rs`.

### Akzeptanzkriterien

- [ ] Jedes Ereignis speichert Zeitpunkt, Person, Ereignistyp, Gegenstand und Details
- [ ] Bei einer maschinell ausgeführten Handlung wird zusätzlich das Modell vermerkt
- [ ] Upload und Extraktion schreiben Einträge
- [ ] Es werden keine Geheimnisse und keine personenbezogenen Daten protokolliert
- [ ] Strukturiertes Logging über `tracing`, kein `println!`
- [ ] Integrationstest belegt, dass ein Upload einen Protokolleintrag erzeugt

---

## DA-10 · Fehler an der HTTP-Grenze abbilden

**Als** Software Engineer
**möchte ich** dass jeder Fehler als bewusster Statuscode mit stabiler Antwortform ankommt
**damit** ein Aufrufer darauf reagieren kann, ohne Fehlertexte zu interpretieren.

**Story Points: 3**

### Beschreibung

Domänen- und Infrastrukturfehler werden an der HTTP-Grenze auf Statuscodes
abgebildet. Interne Details werden protokolliert, aber nie an den Aufrufer gegeben.

Betrifft `src/api/error.rs`.

### Akzeptanzkriterien

- [ ] Jede Fehlerantwort hat dieselbe Form: `{ error: { code, message } }`
- [ ] Statuscodes sind bewusst gewählt: 400, 404, 409, 413, 422, 500, 503
- [ ] Interne Fehlerdetails werden geloggt und nicht ausgeliefert
- [ ] Die Ursachenkette bleibt über `#[source]` erhalten
- [ ] Kein `unwrap()` oder `expect()` im anfragebearbeitenden Code

---

## DA-33 · Projektjournal führen

**Als** Diplomand
**möchte ich** Entscheidungen und Beobachtungen fortlaufend festhalten
**damit** die Experten den Stand jederzeit einsehen können und die Reflexion auf Belegen fusst.

**Story Points: 3**

### Beschreibung

Merkblatt A verlangt ein „fortlaufendes Projektjournal, z. B. in MS Teams, in dem
zentrale Ereignisse, Entscheidungen, Beobachtungen und Reflexionen nachvollziehbar
festgehalten werden", und dass die Experten „laufend auf den aktuellen
Entwicklungsstand Zugriff haben".

Auf wöchentliche Statusberichte wird gemäss Projektbeschreibung verzichtet; das
Journal und die drei Zwischenpräsentationen treten an deren Stelle.

Ein Eintrag entsteht dann, wenn etwas entschieden oder verworfen wurde, nicht nach
Kalender. Was nachträglich rekonstruiert wird, ist keine Beobachtung mehr, sondern
eine Erinnerung.

### Akzeptanzkriterien

- [ ] Das Journal wird im Teams-Kanal der Diplomarbeit geführt und ist für beide Experten einsehbar
- [ ] Jede Architekturentscheidung ist mit Datum, Begründung und verworfener Alternative festgehalten
- [ ] Abweichungen von der Planung sind mit Ursache und Massnahme vermerkt
- [ ] Fehlgeschlagene Ansätze sind festgehalten, nicht nur die erfolgreichen
- [ ] Zu jeder Zwischenpräsentation ist die Rückmeldung der Experten dokumentiert
- [ ] Die Einträge sind in der Schlussreflexion als Beleg verwendbar

---

---

# Sprint 2 — Qualität, Bilder und Shop

**Mo 12.10. – So 08.11.2026 · 4 Wochen · 10 Tickets · 55 Story Points**

**Sprint Goal:** Ein geprüftes Produkt gelangt mitsamt Produktbild in den
Shopify-Shop, und die Güte der Extraktion ist an einem definierten Testdatensatz
gemessen.

**Umfang: ausschliesslich Backend, KI und Shopify.** Kein Oberflächencode. Die
einzige sichtbare Oberfläche ist der Shopify-Shop selbst. Er wird nicht gebaut,
sondern über die Shopify API befüllt.

**Vorführbar zur ZP2:** Der vollständige Ablauf vom PDF bis zum angelegten Produkt
im Shop, gezeigt über `curl` gegen die API und anschliessend das fertige Produkt im
Shopify-Storefront. Dazu die gemessene Correctness als Zahl.

---

## DA-11 · Fehlgelesene Werte gezielt nachbessern

**Als** Fachmitarbeiter im Produktdatenmanagement
**möchte ich** dass das System bei klar fehlerhaften Werten selbst nachfragt
**damit** ich weniger von Hand korrigieren muss.

**Story Points: 5**

### Beschreibung

Nur Befunde vom Schweregrad `Rejected` lösen einen zweiten Modellaufruf aus, und
zwar ausschliesslich für die betroffenen Felder, nicht für das ganze Dokument.
Auf einem sauberen Dokument kostet der Durchlauf damit einen einzigen Aufruf.

Betrifft `src/application/pipeline/mod.rs`, `src/infrastructure/claude/extractor.rs`.

### Akzeptanzkriterien

- [ ] Nur Befunde vom Schweregrad `Rejected` lösen eine Nachbesserung aus
- [ ] Die Anfrage enthält nur die beanstandeten Felder mit dem jeweiligen Problem
- [ ] Höchstens 12 Nachbesserungen je Durchlauf
- [ ] Antworten zu nicht angefragten Feldern werden verworfen
- [ ] Nach der Nachbesserung laufen die Regeln erneut
- [ ] Eine gescheiterte Nachbesserung lässt den Gesamtdurchlauf nicht scheitern
- [ ] Auf einem fehlerfreien Dokument findet genau ein Modellaufruf statt

---

## DA-12 · Bei unbrauchbarer Antwort auf ein stärkeres Modell wechseln

**Als** Software Engineer
**möchte ich** dass bei abgeschnittener Antwort ein grösseres Modell übernimmt
**damit** ein umfangreiches Dokument nicht an der Ausgabegrenze scheitert.

**Story Points: 3**

### Beschreibung

Eskaliert wird nach Fähigkeit, nicht durch Wiederholung derselben Anfrage. Ein
Zeitfehler oder abgelehnte Zugangsdaten eskalieren bewusst **nicht**, denn ein
grösseres Modell würde daran nichts ändern.

Betrifft `src/application/pipeline/mod.rs`, `src/config.rs`.

### Akzeptanzkriterien

- [ ] Abgeschnittene oder unlesbare Antworten lösen einen Wechsel auf das stärkere Modell aus
- [ ] Nichtverfügbarkeit und abgelehnte Zugangsdaten lösen **keinen** Wechsel aus
- [ ] Beide Modelle sind über Umgebungsvariablen konfigurierbar
- [ ] Die Extraktion vermerkt, ob eskaliert wurde
- [ ] Unit-Tests belegen beide Richtungen

---

## DA-13 · Einzelne Werte korrigieren oder verwerfen

**Als** Fachmitarbeiter im Produktdatenmanagement
**möchte ich** einen falschen Wert ersetzen oder ganz verwerfen können
**damit** nur fachlich geprüfte Daten weitergehen.

**Story Points: 5**

### Beschreibung

„Das ist falsch" und „das muss anders lauten" sind zwei verschiedene Aussagen und
werden getrennt festgehalten (`Replaced` / `Dismissed`). **Der ausgelesene Wert
bleibt in beiden Fällen erhalten**, sonst liesse sich später nicht mehr belegen,
wie oft die Extraktion danebenlag.

> **Abgrenzung:** Diese Story liefert die Regeln und die API-Endpunkte. Die
> Bearbeitung im Browser ist Gegenstand von DA-24 in Sprint 3; hier wird sie per
> `curl` nachgewiesen.

Betrifft `src/application/review_proposal.rs`, `src/domain/proposal.rs`.

### Akzeptanzkriterien

- [ ] Ein Feld kann ersetzt, verworfen und wieder hergestellt werden
- [ ] Der ursprünglich ausgelesene Wert bleibt unverändert neben der Korrektur bestehen
- [ ] Jede Korrektur trägt Zeitpunkt und Person
- [ ] Ein verworfenes Feld kann ein Pflichtfeld nicht erfüllen
- [ ] Freie Zusatzattribute können ergänzt und entfernt werden
- [ ] Änderungen an einem bereits entschiedenen Vorschlag werden mit HTTP 409 abgewiesen
- [ ] Jede Änderung erzeugt einen Protokolleintrag

---

## DA-14 · Eine Dokumentprüfung als Sitzung führen

**Als** Software Engineer
**möchte ich** die Prüfung eines Dokuments als eigenständiges Aggregat führen
**damit** Fortschritt und Abschluss abfragbar sind, ohne sie aus den Vorschlägen abzuleiten.

**Story Points: 5**

### Beschreibung

Die Prüfung eines Dokuments wird als eigenständiger Gegenstand geführt: eine
Sitzung, in der eine Person die Produkte eines Dokuments durchgeht. Fortschritt
und Abschlussbericht sind damit direkt abfragbar, statt aus den Vorschlägen
abgeleitet werden zu müssen.

> **Abgrenzung:** Diese Story liefert Aggregat und API. Die Darstellung des
> Fortschritts als Balken oder Zähler ist Gegenstand von DA-27 in Sprint 3.

Betrifft `src/domain/run.rs`, `src/application/review_run.rs`.

### Akzeptanzkriterien

- [ ] Eine Prüfung wird zu einem Dokument eröffnet und hält Beginn und Person fest
- [ ] Der Fortschritt ist als „entschieden von gesamt" abfragbar
- [ ] Eine Prüfung lässt sich erst abschliessen, wenn jedes Produkt entschieden ist
- [ ] Ein vorzeitiger Abschluss wird mit HTTP 422 abgewiesen
- [ ] Der Abschluss hält Zeitpunkt und Person fest
- [ ] Der Abschlussbericht nennt Freigaben, Ablehnungen und Korrekturen

---

## DA-15 · Geprüftes Produkt in den Stammdatenspeicher übernehmen

**Als** Fachmitarbeiter im Produktdatenmanagement
**möchte ich** einen geprüften Vorschlag freigeben
**damit** das Produkt als verbindlicher Stammdatensatz vorliegt.

**Story Points: 5**

### Beschreibung

Der Produktspeicher ist **ausschliesslich einfügend**: Ein Produkt entsteht durch
eine Freigabe, und es gibt keinen Weg, es danach zu überschreiben. Eine Korrektur
findet deshalb dort statt, wo die Werte noch Vorschläge sind. Das hält jeden
Datensatz genau einer Entscheidung zurechenbar.

Eine doppelte EAN wird zu einem **benannten Konflikt**, der das bereits
vorhandene Produkt nennt, statt zu einem gescheiterten Schreibvorgang.

> **Abgrenzung:** Freigabe und Ablehnung erfolgen hier über die API. Die
> Schaltflächen samt Rückfrage sind Gegenstand von DA-26 in Sprint 3.

Betrifft `src/application/review_proposal.rs`, `src/infrastructure/db/product_repository.rs`.

### Akzeptanzkriterien

- [ ] Ein Vorschlag kann freigegeben oder abgelehnt werden, jeweils mit Notiz
- [ ] Freigabe und Ablehnung halten Zeitpunkt und Person fest
- [ ] Ohne Produktname und Preis ist keine Freigabe möglich (HTTP 422)
- [ ] Eine bereits vorhandene EAN führt zu HTTP 409 und nennt das kollidierende Produkt
- [ ] Es gibt keinen Endpunkt, der ein freigegebenes Produkt ändert oder löscht
- [ ] Ein abgelehnter Vorschlag kann wieder geöffnet werden, ein freigegebener nicht
- [ ] `GET /api/products` liefert die freigegebenen Produkte

---

## DA-16 · Produktbild auf der Herstellerseite suchen

**Als** Fachmitarbeiter im Produktdatenmanagement
**möchte ich** dass zu jedem Produkt ein Bild auf der offiziellen Herstellerseite gesucht wird
**damit** ich es nicht selbst zusammensuchen muss.

**Story Points: 8**

### Beschreibung

Zuerst wird ermittelt, auf welcher Domäne die Marke veröffentlicht; die Suche wird
anschliessend auf genau diese Domäne beschränkt. **Ein Bild ist nur dann ein Beleg,
wenn es von der Seite des Herstellers stammt**. Ein Foto von einem Marktplatz
gehört jemand anderem, so deutlich es den Artikel auch zeigt.

Die Annahme oder Ablehnung geschieht allein durch Regeln über die Adresse. Das
macht ein Bild überprüfbar: Die Entscheidung lässt sich aus den zwei Adressen
nachrechnen, ohne jemanden fragen zu müssen.

Betrifft `src/application/find_product_image.rs`, `image_provenance.rs`,
`src/infrastructure/claude/image_finder.rs`, `page_reader.rs`.

### Akzeptanzkriterien

- [ ] Die Domäne der Marke wird ermittelt; ohne Marke findet keine Suche statt
- [ ] Die Suche ist auf die ermittelte Domäne beschränkt
- [ ] Die Fundseite muss auf der Herstellerdomäne oder einer Unterdomäne liegen
- [ ] Ähnlich aussehende Fremddomänen (`hersteller.com.shop.example`) werden abgelehnt
- [ ] Die Bilddatei selbst darf auf einem CDN liegen, muss aber über `https` erreichbar sein
- [ ] Ist kein Bild eindeutig zuordenbar, wird **keines** vorgeschlagen
- [ ] Jede Suche ist zeitlich begrenzt; danach übernimmt einmalig ein stärkeres Modell
- [ ] Die Bildsuchen aller Produkte eines Dokuments laufen nebenläufig, nicht nacheinander
- [ ] Bild und Fundseite werden gemeinsam gespeichert

---

## DA-17 · Vorgeschlagenes Bild bestätigen, ersetzen oder hochladen

**Als** Fachmitarbeiter im Produktdatenmanagement
**möchte ich** das gefundene Bild verwerfen, durch eine Adresse ersetzen oder eine eigene Datei hochladen
**damit** auch Produkte ohne brauchbares Herstellerfoto ein Bild bekommen.

**Story Points: 5**

### Beschreibung

Ein selbst gesetztes Bild wird **nicht** an die Herstellerdomäne gebunden: Die
Regel besteht, um zu verhindern, dass eine maschinelle Suche ein fremdes Foto als
Beleg ausgibt. Wer eine Adresse einträgt, hat entschieden und steht dafür ein. Das
Protokoll hält fest, welcher der beiden Fälle vorliegt.

Ein verworfenes Bild wird behalten, nicht gelöscht: Ein Vorschlag, dessen Bild
einfach entfernt wurde, liesse sich später nicht mehr von einem unterscheiden, für
den nie gesucht wurde.

> **Abgrenzung:** Diese Story liefert Speicherung, Formatprüfung und die
> Endpunkte. Der Upload wird per `curl` mit einer Datei nachgewiesen. Die
> Dateiauswahl und Bildvorschau im Browser sind Gegenstand von DA-25 in Sprint 3.

Betrifft `src/application/review_proposal.rs`, `src/infrastructure/storage/`,
`src/api/handlers/images.rs`.

### Akzeptanzkriterien

- [ ] Ein Bild kann per Adresse gesetzt und wieder entfernt werden
- [ ] Eine Bilddatei kann hochgeladen werden (JPEG, PNG, WebP)
- [ ] Das Dateiformat wird an den Magic Bytes erkannt, nicht am gemeldeten Content-Type
- [ ] Eine hochgeladene Datei erhält eine öffentlich abrufbare Adresse, damit der Shop sie holen kann
- [ ] Ohne konfigurierte öffentliche Adresse wird der Upload abgewiesen und auf die Adresseingabe verwiesen
- [ ] Bilder über 8 MB werden mit HTTP 413 abgewiesen
- [ ] Ein verworfenes Bild bleibt gespeichert, wird aber nie veröffentlicht
- [ ] Die Herkunft (gefunden / selbst gesetzt) wird unterschieden und protokolliert
- [ ] Dateinamen, die aus dem Verzeichnis herausführen, werden abgewiesen

---

## DA-18 · Freigegebenes Produkt in Shopify anlegen

**Als** Fachmitarbeiter im Produktdatenmanagement
**möchte ich** dass ein freigegebenes Produkt samt Bild im Shop erscheint
**damit** es ohne erneute Erfassung verkäuflich ist.

**Story Points: 8**

### Beschreibung

Der Stammdatenspeicher ist die Quelle, der Shop eine Kopie: Werte fliessen nach
aussen, und nichts, was der Shop sagt, wird zurückgelesen. Übertragen werden
Produkt, Variante (EAN, Preis, Artikelnummer, Gewicht), Masse als Metafelder und
das bestätigte Bild.

**Ein Fehlschlag beim Shop lässt die Freigabe nicht scheitern.** Ein Produkt ist
freigegeben, weil eine Person es geprüft hat; ob der Shop eine Sekunde später
erreichbar war, ist eine andere Tatsache, und wird als solche festgehalten.

Betrifft `src/infrastructure/shopify/`, `src/application/publish_product.rs`.

### Akzeptanzkriterien

- [ ] Nach der Freigabe wird das Produkt über die Shopify GraphQL API angelegt
- [ ] Übertragen werden Titel, Marke, Beschreibung, EAN, Preis, Artikelnummer und Gewicht
- [ ] Masse werden als Metafelder unter eigenem Namensraum übertragen
- [ ] Das bestätigte Bild wird mitgegeben; ein verworfenes Bild wird nicht übertragen
- [ ] Das Produkt wird im Storefront sichtbar veröffentlicht
- [ ] Es gibt **keinen** Endpunkt, der einen nicht freigegebenen Datensatz überträgt
- [ ] Fachliche Ablehnungen des Shops werden erkannt, auch wenn sie mit HTTP 200 ankommen
- [ ] Drosselung durch den Shop wird erkannt und die Anfrage wiederholt
- [ ] Ein Fehlschlag wird mit Begründung gespeichert und ist über `GET /api/publications/failed` abfragbar
- [ ] Ohne konfigurierten Shop bleibt die Freigabe möglich, die Übertragung entfällt
- [ ] Das Zugangstoken erscheint in keiner Log-Ausgabe

---

## DA-19 · Güte der Extraktion messen

**Als** Diplomand
**möchte ich** die Correctness der Extraktion an einem definierten Testdatensatz messen
**damit** die in der Projektbeschreibung zugesagten 99 % belegbar sind.

**Story Points: 8**

### Beschreibung

Die Projektbeschreibung nennt als Zielwert eine **Correctness von mindestens 99 %**,
gemessen am Anteil korrekt ausgelesener Attributwerte an allen erwarteten. Dafür
braucht es einen Testdatensatz mit dokumentierten Sollwerten und einen Vergleich,
der reproduzierbar läuft.

Grundlage ist das gemeinsam mit dem Kunden definierte Test-PDF:
`https://github.com/JumpiiX/diplomarbeit/blob/main/demo/test.pdf`

**Dies ist die einzige bezifferte Zusage der Projektbeschreibung und muss belegt
werden können.**

Betrifft `fixtures/`, `tests/`, `docs/`.

### Akzeptanzkriterien

- [ ] Das Test-PDF liegt als Fixture im Repository
- [ ] Die erwarteten Werte sind je Produkt und Feld als Sollwerte dokumentiert
- [ ] Ein reproduzierbarer Lauf vergleicht Ist gegen Soll und gibt die Correctness als Zahl aus
- [ ] Die Auswertung weist je Feld aus, ob korrekt, falsch oder fehlend
- [ ] Das Ergebnis wird mit Modell, Datum und Dokumentversion festgehalten
- [ ] Der gemessene Wert ist in der Dokumentation als Tabelle festgehalten
- [ ] Zusätzlich wird die Belegquote ausgewiesen (Anteil der Werte mit auffindbarer Fundstelle)
- [ ] Weicht das Ergebnis von 99 % ab, wird die Abweichung analysiert und begründet

---

## DA-32 · Wirtschaftlichkeit der Lösung bewerten

**Als** Auftraggeber
**möchte ich** wissen, was eine maschinelle Erfassung gegenüber der manuellen kostet
**damit** ich entscheiden kann, ob sich der Einsatz im Betrieb lohnt.

**Story Points: 3**

### Beschreibung

Die Projektinhalte verlangen eine „Wirtschaftlichkeitsbetrachtung: Bewertung des
Projekts hinsichtlich Kosten-Nutzen, Ressourcen, Nachhaltigkeit oder
Skalierbarkeit".

Die Datengrundlage liegt bereits vor: Zu jeder Extraktion werden Token, Anzahl
Modellaufrufe und Dauer gespeichert (siehe DA-6). Daraus lassen sich die Kosten je
Dokument und je Produkt errechnen und der manuellen Erfassung gegenüberstellen.

Die Betrachtung bleibt bei dem, was belegbar ist. Der Zeitaufwand der manuellen
Erfassung wird beim Kunden erhoben, nicht geschätzt. Eine erfundene Vergleichszahl
würde die ganze Rechnung wertlos machen.

### Akzeptanzkriterien

- [ ] Die Kosten je Dokument und je erkanntem Produkt sind aus den gespeicherten Token errechnet
- [ ] Der Zeitaufwand der manuellen Erfassung ist beim Kunden erhoben und als Quelle benannt
- [ ] Beide Werte sind in einer Tabelle gegenübergestellt
- [ ] Die Rechnung nennt ihre Annahmen offen, einschliesslich der Modellpreise zum Erhebungszeitpunkt
- [ ] Die Prüfzeit des Fachanwenders ist als verbleibender Aufwand berücksichtigt, nicht unterschlagen
- [ ] Das Verhalten bei wachsender Sortimentsgrösse ist beurteilt
- [ ] Die Betrachtung ist Teil der Dokumentation

---

---

# Sprint 3 — PIMFLOW Oberfläche

**Mo 09.11. – So 06.12.2026 · 4 Wochen · 12 Tickets · 59 Story Points**

**Sprint Goal:** Der Fachanwender führt den gesamten Ablauf (hochladen, prüfen,
korrigieren, freigeben) über die Weboberfläche durch, ohne die API zu kennen.

**Umfang: ausschliesslich Oberfläche.** Die Fachlogik steht vollständig aus den
Sprints 1 und 2; dieser Sprint fügt keine neuen fachlichen Regeln hinzu, sondern
macht die vorhandenen bedienbar. Wird während der Umsetzung eine Lücke im Backend
sichtbar, wird sie als eigene Story erfasst statt nebenbei geschlossen.

**Vorführbar zur ZP3:** Der vollständige Ablauf über die Oberfläche, mit
Fundstellen-Anzeige im Dokument.

---

## DA-20 · Frontend-Grundgerüst aufsetzen

**Als** Software Engineer
**möchte ich** ein Frontend-Projekt mit Routing, Datenanbindung und Gestaltungssystem
**damit** die Oberflächen darauf aufbauen können.

**Story Points: 3**

### Beschreibung

React mit TypeScript und Vite, TanStack Query für Serverdaten, React Router,
Tailwind und shadcn/ui. Ausschliesslich funktionale Komponenten.

Betrifft `pimflow-frontend/`.

### Akzeptanzkriterien

- [ ] `npm run dev` startet die Anwendung auf Port 5173
- [ ] Anfragen an `/api` werden auf den Dienst weitergeleitet
- [ ] Serverdaten laufen über TanStack Query, nicht über eigene Ladezustände
- [ ] Es gibt eine zentrale Stelle für API-Aufrufe; Komponenten rufen nicht selbst ab
- [ ] Jede Antwort wird zur Laufzeit auf ihre Form geprüft
- [ ] Jede Datei trägt einen Kopfkommentar
- [ ] `tsc` und der Linter laufen ohne Beanstandung

---

## DA-21 · Handelnde Person erfassen

**Als** Fachmitarbeiter im Produktdatenmanagement
**möchte ich** meinen Namen zu Beginn angeben
**damit** meine Freigaben mir zugeordnet werden.

**Story Points: 2**

### Beschreibung

Der Dienst verlangt bei jeder verändernden Anfrage einen Namen. Die Oberfläche
fragt ihn einmal ab und führt ihn für die Sitzung mit. Bewusst keine
Authentifizierung, das ist als Ausblick dokumentiert.

### Akzeptanzkriterien

- [ ] Ohne Namen ist die Anwendung nicht bedienbar
- [ ] Der Name wird bei jeder verändernden Anfrage mitgesendet
- [ ] Der Name bleibt über einen Seitenwechsel erhalten
- [ ] Der Name ist änderbar
- [ ] Die fehlende Authentifizierung ist als Ausblick dokumentiert

---

## DA-22 · Dokument über die Oberfläche hochladen

**Als** Fachmitarbeiter im Produktdatenmanagement
**möchte ich** ein PDF per Klick oder Ziehen hochladen und die Analyse starten
**damit** ich ohne technische Hilfsmittel arbeiten kann.

**Story Points: 5**

### Beschreibung

Betrifft `features/runs/CaptureDropzone.tsx`, `routes/DocumentsPage.tsx`.

### Akzeptanzkriterien

- [ ] Eine PDF-Datei kann per Ziehen oder Auswahl hochgeladen werden
- [ ] Nur PDF wird angenommen; die Grössenbegrenzung ist genannt
- [ ] Die Bildsuche ist zuschaltbar und standardmässig aus, da sie deutlich länger dauert
- [ ] Während der Analyse ist der Fortschritt sichtbar
- [ ] Nach Abschluss wird zur Prüfung gewechselt
- [ ] Fehler (zu gross, Doppelupload, kein PDF) erscheinen als verständliche deutsche Meldung
- [ ] Hochgeladene Dokumente sind in einer Liste mit Stand einsehbar

---

## DA-23 · Fundstelle im Dokument anzeigen

**Als** Fachmitarbeiter im Produktdatenmanagement
**möchte ich** zu jedem Wert die Stelle im Dokument hervorgehoben sehen
**damit** ich einen Wert prüfen kann, ohne im Dokument zu suchen.

**Story Points: 8**

### Beschreibung

Das Dokument wird neben den ausgelesenen Werten angezeigt. Fahre ich über ein Feld,
wird die zugehörige Stelle im Dokument hervorgehoben und beides mit einer Linie
verbunden.

**Dies ist das fachlich stärkste Merkmal der Arbeit.** Es macht die Extraktion
überprüfbar, statt sie nur zu behaupten.

Betrifft `features/runs/SourceDocument.tsx`, `ProvenanceLink.tsx`.

### Akzeptanzkriterien

- [ ] Das Dokument wird neben den Werten angezeigt
- [ ] Zu jedem belegten Feld ist die Fundstelle als Fläche eingezeichnet
- [ ] Die Fläche liegt massstabsgetreu über der Seite, auch bei geänderter Fenstergrösse
- [ ] Beim Überfahren eines Feldes wird die zugehörige Fläche hervorgehoben, und umgekehrt
- [ ] Bei mehrseitigen Dokumenten wird zur richtigen Seite gesprungen
- [ ] Felder ohne auffindbare Fundstelle sind als solche erkennbar
- [ ] Die Anzeige der Fundstellen ist abschaltbar

---

## DA-24 · Werte prüfen und korrigieren

**Als** Fachmitarbeiter im Produktdatenmanagement
**möchte ich** Werte direkt in der Übersicht bearbeiten und verwerfen
**damit** ich Fehler ohne Umwege beheben kann.

**Story Points: 5**

### Beschreibung

Betrifft `features/runs/RunFieldRow.tsx`, `RunReview.tsx`, `RunAttributes.tsx`.

### Akzeptanzkriterien

- [ ] Jeder Wert ist unmittelbar bearbeitbar
- [ ] Ein Wert kann verworfen und wieder hergestellt werden
- [ ] Ein korrigierter Wert ist als solcher erkennbar
- [ ] Die Konfidenz ist je Feld ablesbar
- [ ] Felder, die Aufmerksamkeit brauchen, sind hervorgehoben und lassen sich einzeln filtern
- [ ] Preise werden in Franken angezeigt und in Rappen gesendet
- [ ] Freie Zusatzattribute können ergänzt und entfernt werden
- [ ] Ein fehlgeschlagener Aufruf zeigt eine verständliche Meldung, der Wert geht nicht verloren

---

## DA-25 · Produktbild prüfen und ersetzen

**Als** Fachmitarbeiter im Produktdatenmanagement
**möchte ich** das gefundene Bild samt Quelle sehen und ersetzen können
**damit** nur ein passendes Bild in den Shop gelangt.

**Story Points: 5**

### Beschreibung

Das Bild wird gezeigt, nicht beschrieben. Eine Adresse sagt niemandem, ob das Foto
diesen Artikel zeigt oder das Modell daneben.

Betrifft `features/runs/RunImage.tsx`.

### Akzeptanzkriterien

- [ ] Das Bild wird angezeigt, mit Verweis auf die Herstellerseite
- [ ] Die Herkunft (vom Hersteller / selbst gesetzt) ist erkennbar
- [ ] Das Bild kann per Adresse ersetzt werden
- [ ] Eine Bilddatei kann vom eigenen Rechner hochgeladen werden
- [ ] Das Bild kann verworfen und wieder verwendet werden
- [ ] Ein nicht ladbares Bild wird als solches gekennzeichnet
- [ ] Wird der Upload abgewiesen, erscheint der Grund

---

## DA-26 · Produkt freigeben oder ablehnen

**Als** Fachmitarbeiter im Produktdatenmanagement
**möchte ich** ein geprüftes Produkt freigeben oder ablehnen
**damit** nur geprüfte Daten in den Shop gelangen.

**Story Points: 5**

### Beschreibung

Betrifft `features/runs/RunReview.tsx`, `ApproveAll.tsx`.

### Akzeptanzkriterien

- [ ] Ein Produkt kann freigegeben oder abgelehnt werden
- [ ] Sind noch Felder ungeprüft, wird vor der Freigabe nachgefragt
- [ ] Ohne Produktname ist die Freigabe gesperrt
- [ ] Ein abgelehntes Produkt kann wieder geöffnet werden; ein freigegebenes nicht, und der Grund wird genannt
- [ ] Alle offenen Produkte können gemeinsam freigegeben werden, mit sichtbarem Fortschritt
- [ ] Wird ein Produkt dabei abgewiesen, wird es mit Grund aufgeführt
- [ ] Eine doppelte EAN nennt das kollidierende Produkt

---

## DA-27 · Prüffortschritt und Abschlussbericht

**Als** Fachmitarbeiter im Produktdatenmanagement
**möchte ich** meinen Fortschritt sehen und die Prüfung abschliessen
**damit** ich weiss, wann ich fertig bin und was dabei herauskam.

**Story Points: 5**

### Beschreibung

Der Bericht weist die Korrekturen getrennt von den Zahlen aus, denn **wie oft die
Extraktion danebenlag, ist die Kennzahl, die zählt**, für das Vertrauen des
Prüfenden wie für die Bewertung des Systems.

Betrifft `features/runs/RunSummary.tsx`, `ReviewProgressBar.tsx`.

### Akzeptanzkriterien

- [ ] Der Fortschritt ist als „entschieden von gesamt" sichtbar
- [ ] Der Abschluss ist erst möglich, wenn alles entschieden ist
- [ ] Der Bericht nennt Freigaben, Ablehnungen, Korrekturen und Belegquote
- [ ] Jede Korrektur wird als vorher → nachher aufgeführt
- [ ] Der Bericht nennt, für wen protokolliert wurde

---

## DA-28 · Stand im Shop sichtbar machen

**Als** Fachmitarbeiter im Produktdatenmanagement
**möchte ich** sehen, welche freigegebenen Produkte der Shop abgelehnt hat
**damit** ein Produkt nicht unbemerkt fehlt.

**Story Points: 5**

### Beschreibung

Da eine fehlgeschlagene Übertragung die Freigabe nicht scheitern lässt, kann eine
Prüfung vollständig erfolgreich aussehen, während ein Artikel nie im Shop ankam.
Diese Lücke schliesst die Oberfläche hier.

Betrifft `features/products/PublicationBadge.tsx`, `routes/ProductsPage.tsx`.

### Akzeptanzkriterien

- [ ] Die Produktliste zeigt je Produkt den Stand: im Shop, nicht übertragen, abgelehnt, kein Shop
- [ ] Eine Ablehnung ist deutlicher hervorgehoben als ein Erfolg
- [ ] Der Abschlussbericht nennt die in dieser Prüfung freigegebenen, aber abgelehnten Produkte mit Grund
- [ ] „Nicht übertragen" und „kein Shop konfiguriert" sind unterscheidbar
- [ ] Ist ein Storefront hinterlegt, gibt es einen Verweis darauf

---

## DA-29 · Übersichtsseite

**Als** Fachmitarbeiter im Produktdatenmanagement
**möchte ich** eine Einstiegsseite mit dem aktuellen Stand
**damit** ich sehe, wo Arbeit liegt.

**Story Points: 3**

### Beschreibung

Betrifft `routes/DashboardPage.tsx`, `features/products/CompletenessPanel.tsx`.

### Akzeptanzkriterien

- [ ] Die Seite nennt offene Prüfungen, freigegebene Produkte und zuletzt bearbeitete Dokumente
- [ ] Die Vollständigkeit der Stammdaten ist je Feld ablesbar
- [ ] Von der Übersicht führen Verweise zur offenen Arbeit
- [ ] Ohne Daten erscheint ein erklärender Hinweis statt einer leeren Fläche

---

## DA-31 · Fachanwender in PIMFLOW einführen

**Als** Fachmitarbeiter im Produktdatenmanagement
**möchte ich** eine kurze Anleitung und eine Einführung in das System
**damit** ich damit arbeiten kann, ohne dass mir jemand über die Schulter schaut.

**Story Points: 5**

### Beschreibung

Das Bewertungsraster führt „Schulung / Schulungsunterlagen" als eigenes Kriterium
(Bereich 2, Praktische Arbeiten), und die Projektinhalte verlangen „Einführung und
Schulung von Nutzenden … mit Feedback-Rückfluss in das Projekt".

Die Unterlagen richten sich an den Fachanwender beim Kunden, nicht an
Entwicklerinnen. Sie erklären den Ablauf entlang der Aufgabe (Dokument hochladen,
Werte prüfen, Bild entscheiden, freigeben) und nicht entlang der Bildschirmmasken.

Der Rückfluss ist Teil der Aufgabe: Was in der Einführung als unklar auffällt, wird
als Befund festgehalten und, wo möglich, noch behoben.

### Akzeptanzkriterien

- [ ] Eine Kurzanleitung führt durch den vollständigen Ablauf vom Upload bis zur Freigabe
- [ ] Die Anleitung erklärt, was die Konfidenz je Feld bedeutet und wann eine Prüfung nötig ist
- [ ] Die Herkunftsregel für Produktbilder ist in einem Satz erklärt, den ein Fachanwender versteht
- [ ] Die Anleitung enthält Abbildungen der tatsächlichen Oberfläche
- [ ] Eine Einführung mit mindestens einer Person aus dem Fachbereich wurde durchgeführt
- [ ] Die Rückmeldungen aus der Einführung sind schriftlich festgehalten
- [ ] Behobene und nicht behobene Rückmeldungen sind getrennt ausgewiesen und begründet
- [ ] Die Unterlagen liegen im Repository und sind aus der Dokumentation verlinkt

---

## DA-30 · Abschluss: Tests, Dokumentation, Präsentation

**Als** Diplomand
**möchte ich** die Arbeit vollständig geprüft und dokumentiert abgeben
**damit** Ergebnis und Vorgehen nachvollziehbar sind.

**Story Points: 8**

### Beschreibung

Abschluss der Arbeit: Testabdeckung prüfen, Messwerte festhalten, Dokumentation
fertigstellen, Schlusspräsentation vorbereiten.

### Akzeptanzkriterien

- [ ] Die Correctness-Messung ist mit exakten Zahlen dokumentiert, nicht mit Wörtern wie „stabil"
- [ ] Das Testsetup ist einheitlich beschrieben und reproduzierbar
- [ ] Alle drei Sprints sind mit Planung, Burndown, Review und Retrospektive dokumentiert
- [ ] Die Sprint Reviews verweisen direkt auf Issues, Commits und Tests
- [ ] Die Abweichung von der geplanten Sprintreihenfolge ist begründet
- [ ] Risikomatrix und SWOT sind gegen den tatsächlichen Verlauf geprüft
- [ ] Die Story-Point-Schätzungen sind je Sprint reflektiert
- [ ] Die Dokumentation ist durchgängig strukturiert und ohne Medienbrüche sequentiell lesbar
- [ ] Ein **Management Summary** liegt vor
- [ ] Das **unterschriebene Ehrenwort** ist beigelegt
- [ ] Die Dokumentation liegt als Markdown und als PDF vor
- [ ] Fremde Inhalte sind an jeder betroffenen Stelle mit exakter Quellenangabe gekennzeichnet
- [ ] Der Quellcode ist als ZIP-Archiv abgabefertig
- [ ] Schul- und Firmenexperte haben die Dokumentation **vor** dem Abgabetermin erhalten
- [ ] Die Bestätigungsmail an `admin.wb@tbz.zh.ch` ist versandt (Schulexemplar, beide Experten, Ehrenwort)
- [ ] Die Schlusspräsentation dauert **15 Minuten**, ist in Schriftsprache gehalten und zeigt die Demo früh
- [ ] Der Raum für das Kolloquium ist beim Sekretariat der TBZ Weiterbildung reserviert

---

# Übersicht

| Sprint | Zeitraum | Wochen | Stories | Story Points | SP / Woche |
|---|---|---|---|---|---|
| 1 — Fundament und Extraktion | 14.09. – 11.10. | 4 | 11 | 51 | 12,8 |
| 2 — Qualität, Bilder und Shop | 12.10. – 08.11. | 4 | 10 | 55 | 13,8 |
| 3 — PIMFLOW Oberfläche | 09.11. – 06.12. | 4 | 12 | 59 | 14,8 |
| **Gesamt** | | **12** | **33** | **165** | **13,8** |

Sprint 1 liegt bewusst tiefer: Er beginnt mit dem Aufsetzen des Projekts, und in
einer unbekannten Ausgangslage ist die Schätzung am unsichersten. Die Abweichung
wird in der Retrospektive gegen die tatsächliche Velocity geprüft.

### Verteilung der Schätzungen

| Punkte | Anzahl |
|---|---|
| 2 | 1 |
| 3 | 9 |
| 5 | 16 |
| 8 | 7 |

Keine Story über 8 Punkten. Das ist eine Konsequenz aus der Rückmeldung zur SA5, wo
eine 13-Punkte-Story zu spät zerlegt wurde.

### Backend und Oberfläche im Paar

Mehrere fachliche Themen erscheinen zweimal: einmal als Fachlogik samt API in
Sprint 1 oder 2, einmal als Bedienung in Sprint 3. Das ist keine Doppelspurigkeit,
sondern die Folge der gewählten Reihenfolge. Die Trennlinie verläuft immer
zwischen *Regel und Schnittstelle* einerseits und *Darstellung* andererseits.

| Thema | Backend (Sprint 1/2) | Oberfläche (Sprint 3) |
|---|---|---|
| Dokument aufnehmen | DA-5 Upload-Endpunkt | DA-22 Ziehen und Ablegen |
| Fundstelle | DA-7 Koordinaten berechnen | DA-23 Fläche auf dem Dokument zeichnen |
| Werte korrigieren | DA-13 Regeln und Endpunkte | DA-24 Bearbeiten in der Tabelle |
| Produktbild | DA-16/17 Suche, Ablage, Endpunkte | DA-25 Bildvorschau und Dateiauswahl |
| Freigabe | DA-15 Übernahme in den Speicher | DA-26 Schaltflächen und Rückfrage |
| Prüfsitzung | DA-14 Aggregat und Fortschrittsabfrage | DA-27 Fortschritt und Abschlussbericht |
| Shop-Anbindung | DA-18 Übertragung und Fehlerprotokoll | DA-28 Stand je Produkt sichtbar machen |

**Faustregel:** Sprint 1 und 2 machen etwas *möglich*, Sprint 3 macht es
*bedienbar*.
