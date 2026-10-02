# PIMFLOW

**Where Product Information Management meets artificial intelligence Flow.**

**TBZ Höhere Fachschule für Technik Zürich**
**Diplomand:** David Unterguggenberger | **Klasse:** ITCNE24 · dipl. Informatiker HF, Cloud-native Engineer
**Zeitraum:** September – Dezember 2026
**Firmenexperte:** Andrej Birka (CTO, Ambit IQ) | **Schulexperte:** Corrado Parisi (TBZ)

---

> **Ein Wort zum Schreibstil**
>
> Corrado hat mir vor zwei Arbeiten einen Hinweis gegeben, den ich seither befolge: keine grossen Textblöcke. Eine Doku voller Textwände liest niemand gern.
>
> Was ich diesmal zusätzlich mitnehme, ist der zweite wiederkehrende Punkt aus beiden Rückmeldungen: Worte wie „funktional" oder „stabil" sind keine Nachweise. Wo in dieser Arbeit eine Aussage über Qualität steht, steht eine Zahl daneben und dazu, wie sie entstanden ist.

---

## Wichtige Links

- **Testdatensatz:** [demo/test.pdf](demo/test.pdf) — das mit dem Kunden vereinbarte Test-PDF
- **Product Backlog:** [product-backlog.md](product-backlog.md) — alle 33 Tickets, drei Sprints
- **Issue-Tracking:** Linear, Team *Diplomarbeit*, Tickets `DA-1` bis `DA-33`
- **Quellcode:** Backend und Frontend liegen in privaten Repositories des Kundenprojekts. Aus Vertraulichkeitsgründen besteht während der Projektlaufzeit kein Zugriff; der vollständige Quellcode wird den Experten mit der Abgabe als ZIP-Archiv übergeben (siehe [Zugang zum Quellcode](#zugang-zum-quellcode)).

---

## Inhaltsverzeichnis

**Projekt-Übersicht**
- [Management Summary](#management-summary)
- [Einführung](#einführung)
- [Problemstellung](#problemstellung)
- [Projektziele](#projektziele)
- [Abgrenzung](#abgrenzung)
- [Architektur](#architektur)
- [Tech-Stack und Technologieentscheide](#tech-stack-und-technologieentscheide)

**Projektmanagement**
- [Theoretische Grundlagen](#theoretische-grundlagen)
- [Sprints und Meilensteine](#sprints-und-meilensteine)
- [Abweichung von der Projektbeschreibung](#abweichung-von-der-projektbeschreibung)
- [Risikomanagement](#risikomanagement)
- [SWOT-Analyse](#swot-analyse)
- [Definition of Done](#definition-of-done)
- [Arbeitsweise mit Linear](#arbeitsweise-mit-linear)
- [Kommunikation mit den Experten](#kommunikation-mit-den-experten)
- [Abdeckung des Bewertungsrasters](#abdeckung-des-bewertungsrasters)

**Sprint 1 — Fundament und Extraktion**
- [Sprint 1 Planung](#sprint-1-planung)
- [Sprint 1 Durchführung](#sprint-1-durchführung)
- [Sprint 1 Testing](#sprint-1-testing)
- [Sprint 1 Review](#sprint-1-review)
- [Zwischenpräsentation 1](#zwischenpräsentation-1)
- [Sprint 1 Retrospektive](#sprint-1-retrospektive)
- [Sprint 1 Fazit](#sprint-1-fazit)

---

## Management Summary

Im Schweizer Retail werden Produktstammdaten bis heute überwiegend von Hand erfasst. Lieferanten schicken Datenblätter und Kataloge als PDF, Mitarbeitende tippen Produktname, EAN, Gewicht und Masse Feld für Feld ab. Bei grossen Händlern ist das keine Nebentätigkeit, sondern eine eigene Abteilung. Der Aufwand wächst mit dem Sortiment, die Fehlerquote bleibt, und die investierte Zeit erzeugt keinen Wert über die reine Übertragung hinaus.

PIMFLOW automatisiert diesen Schritt, ohne die Verantwortung dafür abzugeben. Ein Sprachmodell liest das Lieferantendokument und schlägt die enthaltenen Produktdaten strukturiert vor. Zu jedem Wert wird die Stelle im Dokument mitgeliefert, aus der er stammt. Ein Fachanwender prüft, korrigiert und gibt frei. Erst dann entsteht ein Produkt.

Der Satz, der die ganze Architektur trägt: **Das System schlägt vor, der Mensch entscheidet.** Nichts erreicht den Stammdatenspeicher ohne ausdrückliche Freigabe einer namentlich erfassten Person. Das ist zugleich die Antwort auf die Schwäche jedes Sprachmodells — es kann sich irren, und deshalb darf es nicht das letzte Wort haben.

**Ergebnis nach Sprint 1:** Ein Lieferantendokument kann über die API hochgeladen und ausgelesen werden. Am gemeinsam mit dem Kunden definierten Testdatensatz wurden **66 von 66 erwarteten Attributwerten korrekt erkannt**, das sind 100 % bei einem Zielwert von 99 %. Kein Wert wurde erfunden. Zu 96,97 % der Werte konnte die Fundstelle im Dokument nachgewiesen werden; die beiden Ausnahmen sind genau die zwei Felder, die im Dokument nicht vorkommen und korrekt als fehlend gemeldet wurden.

Das Fundament steht damit, und es steht belegt.

---

## Einführung

Ich arbeite als Software Engineer bei Ambit IQ. Davor war ich bei brack.ch, einem der grössten Schweizer Retailer. Dort habe ich zum ersten Mal gesehen, wie Produktdaten tatsächlich ins System kommen: nicht über eine Schnittstelle, sondern über Menschen, die PDFs öffnen und abtippen.

Das hat mich damals erstaunt. Nicht weil es dumm gemacht wäre, sondern weil es keine bessere Lösung gab. Lieferanten liefern keine strukturierten Daten. Sie liefern Kataloge, die für Menschen gemacht sind: Tabellen über zwei Seiten, Masse in einer einzigen Zelle, Gewichte mal in Gramm und mal in Kilogramm, Preise mit und ohne Währung.

Klassische Software scheitert daran, weil sie eine feste Struktur braucht. Ein Sprachmodell scheitert nicht daran, weil es Layout lesen kann. Aber es bringt ein neues Problem mit: Es kann etwas behaupten, das nicht dasteht.

Genau an dieser Stelle setzt diese Arbeit an. Die interessante Frage ist nicht, ob ein Modell ein PDF lesen kann. Das kann es. Die interessante Frage ist, **wie man einem ausgelesenen Wert ansieht, ob er stimmt.**

Dieselben Probleme finden sich bei den Kunden von Ambit IQ wieder. Deshalb entsteht diese Arbeit nicht im luftleeren Raum, sondern innerhalb eines laufenden Kundenprojekts, mit echten Dokumenten und echten Anforderungen.

---

## Problemstellung

### Wie Produktdaten heute entstehen

```
Lieferant                 Händler
   │                         │
   ├── PDF-Katalog  ────────▶ Mitarbeiter öffnet PDF
   ├── Datenblatt            │
   └── Preisliste            ├── liest Produktname ab, tippt ihn ein
                             ├── liest EAN ab, tippt sie ein
                             ├── liest Gewicht ab, rechnet kg in g um, tippt es ein
                             ├── liest Masse ab, zerlegt sie, tippt sie ein
                             ├── sucht ein Produktbild auf der Herstellerseite
                             └── wiederholt das je Produkt
```

Bei einem Katalog mit 200 Produkten und elf Feldern sind das 2200 Übertragungen von Hand. Jede einzelne davon kann schiefgehen.

### Was daran teuer ist

| Problem | Wirkung |
|---|---|
| Aufwand skaliert linear | Doppeltes Sortiment heisst doppelter Personalaufwand |
| Fehlerquote bleibt konstant | Mehr Produkte heisst mehr Fehler, nicht weniger |
| Kein fachlicher Mehrwert | Abtippen ist keine Fachleistung, wird aber von Fachkräften erledigt |
| Bildrecherche kommt dazu | Jedes Produkt braucht ein Bild, das jemand suchen und zuordnen muss |

### Warum es nicht längst gelöst ist

Der naheliegende Gedanke ist ein Parser. Der scheitert daran, dass jeder Lieferant ein eigenes Layout hat, und diese Layouts sich ändern. Ein Parser je Lieferant ist teurer als das Abtippen.

Der zweite Gedanke ist ein Sprachmodell. Das löst das Layout-Problem, schafft aber ein Vertrauensproblem: Ein Modell liefert zu jeder Frage eine Antwort, auch zu einer, die das Dokument nicht beantwortet. Ein erfundenes Gewicht ist schlimmer als ein fehlendes, weil niemand danach sucht.

**Die eigentliche Aufgabe dieser Arbeit ist deshalb nicht die Extraktion, sondern deren Überprüfbarkeit.**

---

## Projektziele

| # | Ziel | Messbar woran |
|---|---|---|
| 1 | KI-gestützte Dokumentenextraktion | Correctness ≥ 99 % am definierten Testdatensatz |
| 2 | Nachweis der Fundstelle | Zu jedem Wert Seite und Rechteck im Dokument |
| 3 | Produktbild-Recherche | Bild ausschliesslich von der offiziellen Herstellerseite, mit Quellenangabe |
| 4 | Human-in-the-Loop Review | Jedes Attribut korrigierbar, jede Freigabe protokolliert |
| 5 | Shopify-Integration | Freigegebenes Produkt inklusive Bild im Shop angelegt |

**Correctness** ist definiert als der Anteil korrekt extrahierter Attributwerte an allen erwarteten Attributwerten, gemessen gegen einen Testdatensatz mit bekannten Sollwerten.

Ziele 1 und 2 sind Gegenstand von Sprint 1 und in dieser Fassung der Dokumentation belegt. Ziele 3 bis 5 folgen in Sprint 2 und 3.

---

## Abgrenzung

Was diese Arbeit **nicht** leistet, und warum:

| Nicht Gegenstand | Begründung |
|---|---|
| Authentifizierung, Benutzerverwaltung, Rollen | Ersetzt durch eine namentliche Erfassung, die dieselbe Stelle im Request belegt. Echte Authentifizierung wäre später ein Eingriff in eine Middleware, nicht in jeden Handler. |
| Mandantenfähigkeit | Ein Kunde. |
| Rückkanal aus Shopify | Der Stammdatenspeicher ist die Quelle, Shopify ein Ziel. Zwei Wahrheiten wären schlimmer als eine unvollständige. |
| Beliebige Dokumentformate | PDF. Word, Excel und Scans sind als Ausbaustufe untersucht, aber nicht Teil dieser Arbeit. |
| Oberflächencode in Sprint 1 und 2 | Siehe [Abweichung von der Projektbeschreibung](#abweichung-von-der-projektbeschreibung). |

---

## Architektur

![Schichten und Abhängigkeiten](docs/images/architektur.svg)

Vier Schichten, und alle Abhängigkeiten zeigen nach innen. Die Domäne kennt weder Datenbank noch HTTP noch Claude — sie definiert Traits in `domain/ports.rs`, und die Infrastruktur erfüllt sie.

Das ist keine Stilfrage. Es ist der Grund, weshalb 324 Unit-Tests ohne laufende Datenbank durchlaufen, in 0,10 Sekunden. Läge die Fachlogik in den Handlern, bräuchte jeder dieser Tests einen HTTP-Server und eine Datenbank, und niemand würde sie mehr bei jedem Speichern laufen lassen.

```
src/
├── main.rs           Zusammenbau, Start
├── config.rs         typisierte Konfiguration, einmal beim Start geprüft
├── api/              HTTP: Routen, DTOs, Fehler auf Statuscodes
├── application/      Anwendungsfälle, gegen Ports formuliert
├── domain/           Entitäten, Wertobjekte, Regeln, Ports — kein I/O
└── infrastructure/   PostgreSQL, Claude, pdfium, Dateiablage
```

### Zwei getrennte Datenbanken

`pimflow_db` ist der Stammdatenspeicher und gehört PIMFLOW. `pimflow_mock_db` steht für die bestehenden Produktdaten des Kunden und wird ausschliesslich gelesen.

Getrennte Datenbanken statt getrennter Schemas, weil die Mock-Datenbank wegwerfbar sein muss. Wird das echte Kundensystem angebunden, verschwindet sie, und nichts im Stammdatenspeicher bricht. Fremdschlüssel über Datenbankgrenzen sind in PostgreSQL nicht möglich — und genau das ist hier erwünscht, denn ein Verweis auf ein fremdes System ist auch in Wirklichkeit kein Fremdschlüssel.

### Der Speicher wird nur beschrieben, nie überschrieben

Ein Produkt entsteht durch Freigabe. Es gibt keinen Weg, eines danach zu ändern. Korrekturen passieren, solange die Werte noch Vorschläge sind.

Das klingt nach einer Einschränkung und ist eine Zusicherung: Jeder Datensatz im Speicher lässt sich auf genau eine Entscheidung einer genau benannten Person zurückführen. Ein nachträgliches Update würde diese Kette zerreissen.

### Was das Modell extrahiert hat, bleibt erhalten

Eine Korrektur des Prüfers wird **neben** den ursprünglichen Wert geschrieben, nicht darüber. Das kostet etwas Schema-Komplexität und bringt zwei Dinge: eine vollständige Nachvollziehbarkeit, und messbare Daten darüber, wie oft und wo das Modell falsch lag. Letzteres ist die Grundlage für die Auswertung in Sprint 2.

---

## Tech-Stack und Technologieentscheide

| Bereich | Gewählt | Verworfen | Begründung |
|---|---|---|---|
| Backend | Rust mit axum | Node.js, Python | Starkes Typsystem, keine Laufzeitüberraschungen bei der Datenkonvertierung. Ungültige Zustände lassen sich im Typ ausschliessen statt im Test suchen. |
| Datenbank | PostgreSQL mit sqlx | Diesel, SeaORM | `sqlx` prüft SQL zur Kompilierzeit gegen das echte Schema. Ein Tippfehler in einer Abfrage bricht den Build, nicht die Produktion. |
| Sprachmodell | Claude API direkt über `reqwest` | Anthropic-Crate von crates.io | Es gibt kein offizielles Rust-SDK. Die verfügbaren Crates sind unfertig oder seit 2024 unverändert. Der benötigte Umfang sind rund 200 Zeilen eigener Code; ein veralteter Wrapper würde nur neue API-Felder blockieren. |
| PDF-Vermessung | pdfium über `pdfium-render` | `lopdf`, `pdf-extract` | Es geht nicht um Text, sondern um Koordinaten. pdfium ist die Bibliothek, die auch Chrome verwendet. |
| Dokumentenlesen | PDF als `document`-Block an Claude | lokale Textextraktion | Claude liest Layout und Tabellen. Ein Textextraktor liefert eine Zeichenfolge ohne Struktur, und die Struktur ist genau das, worauf es bei einem Katalog ankommt. |

### Zu Rust

Die Wahl war nicht neutral: Rust ist die Sprache, in der bei Ambit IQ entwickelt wird, und ich hatte sie bereits in zwei Arbeiten eingesetzt. Aber sie passt hier auch fachlich. Ein Gewicht ist keine Zahl, sondern `Grams`. Ein Preis ist kein Float, sondern `Money` in ganzen Rappen. Eine Produkt-ID ist keine UUID, sondern `ProductId`. Drei nackte UUIDs als Funktionsargumente sind ein Vertauschungsfehler, der auf seine Gelegenheit wartet; drei verschiedene Newtypes sind es nicht.

### Zu pdfium und dem Vendoring

pdfium wird von keinem Paketmanager ausgeliefert, und die `static`-Variante von `pdfium-render` erzeugt nur die Bindings, nicht die Bibliothek selbst. Sie liegt deshalb unter `vendor/pdfium/` im Repository.

Ein Detail, das mich Zeit gekostet hat: pdfium initialisiert prozessweiten Zustand und verweigert eine zweite Bindung. Die Instanz läuft deshalb als Singleton hinter einem Mutex. Beim ersten parallelen Test war das nicht so, und der Fehler sah aus wie ein Speicherproblem.

---

## Theoretische Grundlagen

### Scrum

Scrum ist ein Rahmenwerk für die iterative Entwicklung in Sprints fester Länge. Es definiert drei Verantwortlichkeiten (Product Owner, Scrum Master, Entwickler), fünf Ereignisse und drei Artefakte.[^scrum]

In einer Einzelarbeit fallen die drei Rollen zusammen. Was bleibt und was ich tatsächlich nutze, sind die Ereignisse: Sprint Planning zu Beginn, Review am Ende, Retrospektive danach. Die Zwischenpräsentationen der Diplomarbeit sind als Sprint Reviews ausgestaltet, was gut passt, weil ein Review genau das ist — das Ergebnis den Stakeholdern zeigen und Rückmeldung einholen.

Was ich bewusst weglasse: Daily Scrums mit mir selbst. Ein Ereignis, dessen Zweck die Abstimmung im Team ist, hat ohne Team keinen Zweck. An seiner Stelle steht das Projektjournal.

### Story Points und Fibonacci

Story Points schätzen Aufwand relativ statt absolut. Die Fibonacci-Reihe (1, 2, 3, 5, 8) bildet ab, dass die Schätzgenauigkeit mit der Grösse abnimmt: Zwischen 1 und 2 ist der Unterschied noch beurteilbar, zwischen 20 und 21 nicht mehr.[^cohn]

**Keine Story in diesem Projekt ist grösser als 8 Punkte.** Das ist eine direkte Folge der Rückmeldung zur letzten Arbeit, wo eine 13-Punkte-Story deutlich länger dauerte als geschätzt und sich im Nachhinein als drei Aufgaben herausstellte. Grössere Themen sind hier vorab zerlegt.

### Definition of Done

Eine geteilte Festlegung, wann eine Aufgabe fertig ist. Ohne sie bedeutet „erledigt" bei jedem Ticket etwas anderes, und der Sprint-Fortschritt wird unvergleichbar.[^scrum] Meine Fassung steht unter [Definition of Done](#definition-of-done).

### Risikomanagement

Risiken werden nach Eintrittswahrscheinlichkeit und Auswirkung bewertet und mit einer Massnahme versehen. Der Nutzen liegt weniger in der Bewertung als im Zwang, vor dem Projekt zu benennen, was schiefgehen kann — und nach dem Projekt nachzusehen, ob man richtig lag.

[^scrum]: Schwaber, K. & Sutherland, J. (2020): *The Scrum Guide*. https://scrumguides.org/
[^cohn]: Cohn, M. (2005): *Agile Estimating and Planning*. Prentice Hall.

---

## Sprints und Meilensteine

![Sprints und Meilensteine](docs/images/sprints.svg)

| Sprint | Zeitraum | Dauer | Story Points | Tickets | Zwischenpräsentation |
|---|---|---|---|---|---|
| 1 — Fundament und Extraktion | 14.09. – 11.10.2026 | 4 Wochen | 51 | 11 | ZP1: 19.10.2026 |
| 2 — Qualität, Bilder und Shop | 12.10. – 08.11.2026 | 4 Wochen | 55 | 10 | ZP2: 16.11.2026 |
| 3 — PIMFLOW Oberfläche | 09.11. – 06.12.2026 | 4 Wochen | 59 | 12 | ZP3: 14.12.2026 |
| Abgabephase | 07.12. – 18.12.2026 | 2 Wochen | — | — | Abgabe: 18.12.2026 |

**Alle drei Sprints sind exakt gleich lang.** Das ist die Voraussetzung dafür, die Velocity über den Projektverlauf zu vergleichen: Bei ungleich langen Sprints sagt eine höhere Punktzahl nur, dass mehr Zeit zur Verfügung stand. Auch das ist eine Konsequenz aus der letzten Rückmeldung.

Die Punkteverteilung 51 / 55 / 59 liegt innerhalb von ±7 % um den Mittelwert. Eine weitere Angleichung würde die fachliche Reihenfolge zerreissen — die Messung der Extraktionsgüte setzt die Extraktion voraus, die Anzeige der Fundstelle deren Berechnung.

Die Zwischenpräsentationen liegen jeweils acht Tage nach Sprint-Ende. Der Abstand ist eingeplant: Der Sprint ist zum Zeitpunkt der Präsentation abgeschlossen, die Zahlen stehen fest, und der Burndown lässt sich auswerten statt hochrechnen.

---

## Abweichung von der Projektbeschreibung

Die unterschriebene Projektbeschreibung sieht die Oberfläche in Sprint 2 und die Shopify-Integration in Sprint 3 vor. Das Board dreht das um: **Sprint 1 und 2 bauen ausschliesslich Backend, KI und Shopify.** Die Oberfläche folgt in Sprint 3.

**Begründung:** Der fachliche Kern dieser Arbeit ist die Extraktion. Das ist auch der Teil mit dem echten Risiko — ob ein Modell einen Lieferantenkatalog zuverlässig liest, weiss man erst, wenn man es gemessen hat. Steht dieser Teil früh und ist belegt, bleibt für die Oberfläche ein voller Sprint mit bekannter Datenlage. Umgekehrt hätte ich eine Oberfläche über einer Extraktion gebaut, von der ich nicht weiss, ob sie trägt.

Praktisch heisst das: Zur ZP1 und ZP2 wird über `curl` gegen die API und über den Shopify-Shop vorgeführt, nicht über eine eigene Weboberfläche. Jede Anforderung dieser beiden Sprints gilt als erfüllt, wenn sie über die HTTP-API nachweisbar ist.

Die Abweichung ist mit dem Firmenexperten abgestimmt und wird in jedem Sprint Review angesprochen.

---

## Risikomanagement

![Risikomatrix](docs/images/risikomatrix.svg)

| # | Risiko | Wahrscheinlichkeit | Auswirkung | Massnahme |
|---|---|---|---|---|
| R1 | Extraktion ungenau oder unvollständig | mittel | hoch | Human-in-the-Loop als Grundprinzip, Regeln über der Modellantwort, messbare Prompt-Iteration |
| R2 | Anforderungsänderungen im Kundenprojekt | mittel | mittel | Iteratives Vorgehen, Sprint-Umfang während des Sprints stabil |
| R3 | Technische Überraschungen | mittel | mittel | MVP zuerst, Kernfunktionen priorisiert |
| R4 | Kein eindeutiges Produktbild auffindbar | hoch | hoch | Nur eindeutig zuordenbare Bilder von offiziellen Herstellerseiten; sonst kein Vorschlag, manueller Upload möglich |
| R5 | Zeitkonflikt mit dem Kundenprojekt | niedrig | mittel | Regelmässige Abstimmung, Fortschrittskontrolle an Sprintzielen |

**Eingetreten in Sprint 1:** R3, in einer Form, die ich nicht auf dem Zettel hatte — pdfium verweigert eine zweite Bindung im selben Prozess. Details unter [Durchführung](#da-7--fundstelle-im-dokument-belegen).

**R1 hat sich bisher nicht bestätigt.** Die Messung ergab 100 % am Testdatensatz. Das entwertet das Risiko nicht: Ein Dokument ist ein Dokument, und die Bewertung bleibt bis zur breiteren Messung in Sprint 2 unverändert.

---

## SWOT-Analyse

| | |
|---|---|
| **Stärken** | Fachliche Vorerfahrung aus dem Retail (brack.ch)<br>Rust und Clean Architecture bereits erprobt<br>Echtes Kundenprojekt mit echten Dokumenten<br>Fachliche Betreuung durch den CTO vor Ort |
| **Schwächen** | Einzelentwickler, kein Review durch Zweite<br>Keine Erfahrung mit pdfium vor Projektbeginn<br>Qualität der Extraktion hängt an einem externen Dienst |
| **Chancen** | Das Problem existiert branchenweit, nicht nur bei einem Kunden<br>Die Extraktion ist als Baustein für weitere Anwendungsfälle nutzbar<br>Lösung soll nach der Diplomarbeit weiterentwickelt werden |
| **Risiken** | Modellverhalten kann sich mit einer neuen Version ändern<br>Lieferantendokumente sind beliebig unterschiedlich<br>Produktbilder auf Herstellerseiten nicht immer eindeutig zuordenbar |

---

## Definition of Done

Gilt einheitlich für jedes Ticket:

- [ ] Code oder Konfiguration funktioniert und ist getestet
- [ ] `cargo fmt --check`, `cargo clippy -- -D warnings` und `cargo test` sind sauber
- [ ] In Git committed und gepusht, in atomaren Commits
- [ ] Dokumentation erstellt oder aktualisiert
- [ ] Keine bekannten Fehler offen

Ein Ticket ohne alle fünf Haken ist nicht erledigt, auch wenn es funktioniert.

---

## Arbeitsweise mit Linear

Die drei Sprints sind als **Cycles** im Team *Diplomarbeit* abgebildet. Linear zeichnet daraus Burndown und Velocity automatisch.

**Workflow:** `Backlog → Todo → In Progress → In Review → Done`

Zwei Einstellungen, die bewusst so gesetzt sind:

- **Cycle-Länge vier Wochen, kein Cooldown.** Die Sprints schliessen lückenlos aneinander an.
- **Die Automatik „Completed issues" ist ausgeschaltet.** Sonst wandert ein nachträglich abgeschlossenes Ticket in den nächsten Cycle und verfälscht beide Burndown-Charts.

Der Sprint-Umfang bleibt während des laufenden Sprints stabil. Kommt etwas dazu, geht es in den nächsten Sprint.

> **Einzufügen:** Screenshot des Linear-Boards am Sprint-1-Start (14.09.2026) und am Sprint-1-Ende (11.10.2026). Corrado hat das in der Rückmeldung zur SA5 ausdrücklich gewünscht, damit Commitment und tatsächlicher Fortschritt nebeneinander sichtbar werden.

---

## Kommunikation mit den Experten

| Weg | Wofür | Rhythmus |
|---|---|---|
| Microsoft Teams | Projektjournal, organisatorische Abstimmung | laufend |
| Zwischenpräsentationen | Sprint Review mit beiden Experten | 3× je Sprint |
| Abstimmung vor Ort | fachliche Fragen mit dem Firmenexperten | nach Bedarf |

**Zum Verzicht auf wöchentliche Statusberichte:** Merkblatt A führt sie als eigenes Bewertungskriterium. Die unterschriebene Projektbeschreibung sieht vor, darauf zu verzichten. An ihre Stelle treten das fortlaufende Projektjournal (DA-33) und die drei Zwischenpräsentationen.

Das ist kein Weglassen, sondern ein Ersatz mit einer anderen Eigenschaft: Ein Journaleintrag entsteht, wenn etwas entschieden oder verworfen wurde, nicht nach Kalender. Ein Wochenbericht in einer Woche ohne Entscheidung beschreibt nichts; ein Journal überspringt sie einfach. Was nachträglich rekonstruiert wird, ist ohnehin keine Beobachtung mehr, sondern eine Erinnerung.

### Zugang zum Quellcode

Backend und Frontend liegen in privaten Repositories des Kundenprojekts. Aufgrund interner Sicherheits- und Vertraulichkeitsvorgaben besteht während der Projektlaufzeit kein direkter Zugriff für Dritte.

Nachvollziehbarkeit ist stattdessen so hergestellt:

- **Diese Dokumentation** nennt zu jeder Aussage die betroffenen Dateien mit Pfad
- **Linear** ist für beide Experten einsehbar, Tickets `DA-1` bis `DA-33`
- **Die Zwischenpräsentationen** führen den jeweiligen Stand live vor
- **Mit der Abgabe** wird der vollständige Quellcode als ZIP-Archiv übergeben

Dieses Vorgehen ist in der Projektbeschreibung festgehalten und mit beiden Experten abgestimmt.

---

## Abdeckung des Bewertungsrasters

Merkblatt A bewertet in sieben Bereichen. Diese Zuordnung zeigt, worin sie in dieser Arbeit sichtbar werden.

| Bereich | Kriterium | Abgedeckt durch |
|---|---|---|
| 1 Wissen | Fachwissen, Hintergründe, neu erarbeitetes Wissen | DA-6, DA-7 (Modellanbindung, pdfium), Technologieentscheide |
| 2 Praktische Arbeiten | Infrastruktur, technische Umsetzung | DA-1, DA-4 |
| 2 Praktische Arbeiten | Schulung und Schulungsunterlagen | DA-31 (Sprint 3) |
| 3 Intellektuelle Fähigkeiten | Problemdiagnose, Zusammenhänge, Urteilsvermögen | DA-8, DA-19, DA-32 |
| 4 Organisatorische Fähigkeiten | Projektabwicklung, Steuerung | Linear-Cycles, Burndown je Sprint |
| 4 Organisatorische Fähigkeiten | Wöchentlicher Statusbericht | ersetzt durch DA-33 und die drei Zwischenpräsentationen |
| 4 Organisatorische Fähigkeiten | Zwischenpräsentationen | ZP1 bis ZP3 |
| 5 Soziale Kompetenzen | Zusammenarbeit, Ausdauer | Zusammenarbeit mit dem Firmenexperten, DA-33 |
| 6 Präsentation & Dokumentation | Dokumentation, Kolloquium, Management Summary | diese Dokumentation, DA-30 |
| 7 Zielerreichung | Umsetzung der definierten Ziele | DA-19 (Correctness ≥ 99 %), Sprint Goals |

---
---

# Sprint 1 — Fundament und Extraktion

**14.09. – 11.10.2026 · 4 Wochen · 11 Tickets · 51 Story Points**

## Sprint 1 Planung

**Sprint Goal**

> Ein Lieferantendokument kann hochgeladen werden, wird von einem Sprachmodell gelesen und liefert strukturierte Produktvorschläge, bei denen jeder Wert auf die Stelle im Dokument zeigt, aus der er stammt.

**Umfang:** ausschliesslich Backend und KI. Kein Oberflächencode.

### Was ich mir vorgenommen habe

Drei Fragen standen am Anfang:

1. Wie schneide ich die Architektur, damit die Fachlogik ohne Datenbank testbar bleibt?
2. Kann ein Sprachmodell einen echten Lieferantenkatalog zuverlässig genug lesen?
3. Und, die eigentliche Frage: Wie belege ich, dass ein ausgelesener Wert wirklich im Dokument steht?

Die dritte Frage ist der Kern. Ohne sie wäre PIMFLOW ein Werkzeug, das plausible Vermutungen produziert.

### User Stories

| Ticket | Story | Priorität | SP | Status |
|---|---|---|---|---|
| DA-1 | Projektfundament aufsetzen | Must | 3 | Erledigt |
| DA-2 | Schichtenarchitektur festlegen | Must | 3 | Erledigt |
| DA-3 | Produktdaten als Typen modellieren | Must | 5 | Erledigt |
| DA-4 | Produktdaten dauerhaft speichern | Must | 5 | Erledigt |
| DA-5 | Lieferantendokument hochladen | Must | 5 | Erledigt |
| DA-6 | Produktdaten mit einem Sprachmodell auslesen | Must | 8 | Erledigt |
| DA-7 | Fundstelle im Dokument belegen | Must | 8 | Erledigt |
| DA-8 | Werte vereinheitlichen und prüfen | Must | 5 | Erledigt |
| DA-9 | Jede Handlung nachvollziehbar protokollieren | Must | 3 | Erledigt |
| DA-10 | Fehler an der HTTP-Grenze abbilden | Must | 3 | Erledigt |
| DA-33 | Projektjournal führen | Must | 3 | Erledigt |

**Total: 51 Story Points**

Beispielhaft die Story-Form, in der alle Tickets im Backlog stehen:

> **DA-7 · Fundstelle im Dokument belegen**
>
> **Als** Software Engineer
> **möchte ich** zu jedem ausgelesenen Wert die Fundstelle im Dokument als Koordinaten ermitteln
> **damit** später belegt werden kann, woher der Wert stammt.
>
> **Akzeptanzkriterien**
> - Zu jedem Feld mit Zitat werden Seite und Rechteck ermittelt
> - Koordinaten seitenrelativ in Prozent, unabhängig von einer späteren Darstellungsgrösse
> - Ein nicht auffindbares Zitat erzeugt einen Befund, keinen leeren Bereich
> - Die Suche toleriert abweichende Leerzeichen und Zeilenumbrüche
> - Unit-Tests belegen Treffer, Fehltreffer und mehrseitige Dokumente

Alle Akzeptanzkriterien zu allen elf Tickets stehen im [Product Backlog](product-backlog.md).

![Burndown Sprint 1](docs/images/burndown-sprint1.svg)

> **Einzufügen:** Burndown-Chart aus Linear (Cycle 1). Die hier gezeigten Verlaufswerte sind aus dem Arbeitsfortschritt rekonstruiert und durch den Export aus Linear zu ersetzen.

---

## Sprint 1 Durchführung

### DA-1 bis DA-4 · Das Fundament

**Unspektakulär und unverzichtbar.**

Rust-Projekt mit axum, PostgreSQL in Docker, und eine Konfiguration, die beim Start einmal aus der Umgebung gelesen und geprüft wird. Fehlt `ANTHROPIC_API_KEY`, bricht der Prozess sofort ab und nennt die Variable — statt eine Stunde später beim ersten Extraktionsversuch.

Zwei Entscheidungen, die sich später ausgezahlt haben:

**Fachwerte sind eigene Typen.** `Grams`, `Millimetres`, `Money` in ganzen Rappen, `ProductId`, `ProposalId`. Der Aufwand dafür ist einmalig, der Nutzen dauerhaft: Ein Preis kann nicht versehentlich als Fliesskommazahl gerundet werden, und zwei IDs lassen sich nicht vertauschen. `Money` rechnet ausschliesslich in ganzen Rappen — Fliesskomma hat in Geldbeträgen nichts verloren.

**Ports in der Domäne, Implementierung aussen.** `domain/ports.rs` definiert, was der Anwendungsfall braucht; `infrastructure/db/` liefert es. Beim Testen tritt ein Test-Double an dieselbe Stelle.

Die Ports haben mich zwei Anläufe gekostet. Der erste Schnitt war zu fein — je Tabelle ein Trait mit fünfzehn Methoden, von denen die Anwendungsfälle drei brauchten. Der zweite Schnitt fragt: Was braucht dieser Anwendungsfall? Und genau das steht im Trait.

**Betroffen:** `src/config.rs`, `src/domain/ids.rs`, `money.rs`, `measurement.rs`, `src/domain/ports.rs`, `src/infrastructure/db/`, `migrations/pimflow/`

### DA-5 · Lieferantendokument hochladen

**Ein Upload ist mehr Prüfung als Übertragung.**

Der Dateityp wird an den Magic Bytes erkannt (`%PDF-`), nicht am gemeldeten Content-Type. Ein Content-Type ist eine Behauptung des Clients, die ersten fünf Bytes sind es nicht.

Eine inhaltsgleiche Datei wird über SHA-256 erkannt und mit HTTP 409 abgewiesen, unter Nennung des bestehenden Dokuments. Das ist beim Schreiben dieser Dokumentation praktisch aufgefallen: Beim Versuch, das Test-PDF erneut hochzuladen, kam

```json
{"error":{"code":"conflict","message":"this document was already uploaded as diplomarbeit-test.pdf"}}
```

Genau so soll es sein. Der Prüfer erfährt, dass die Datei schon da ist, und wo.

**Drei Fallen bei Multipart in axum**, jede davon hat mich Zeit gekostet:

- Der `Multipart`-Extraktor hat ein Standardlimit von 2 MB. Das weist die meisten Lieferantendokumente ab. Das Limit wird je Route auf 25 MB angehoben, unterhalb der 32-MB-Grenze der Claude API.
- `Multipart` muss der **letzte** Handler-Parameter sein, weil er den Body verbraucht. `State` und `Path` kommen davor.
- `field.bytes().await` lädt das gesamte Feld in den Speicher. `Field` implementiert `Stream`, also wird direkt auf die Platte geschrieben. Sonst bestimmen parallele Uploads grosser PDFs die Speicherobergrenze.

Das Limit wird nie ganz abgeschaltet. Ein unbegrenzter Body ist ein sehr einfacher Weg, den Dienst umzubringen.

**Betroffen:** `src/application/upload_document.rs`, `src/api/handlers/documents.rs`

### DA-6 · Produktdaten mit einem Sprachmodell auslesen

**Die Antwort wird erzwungen, nicht erhofft.**

Das PDF geht als `document`-Block an die Claude API. Die Antwortform ist über ein Schema festgelegt, damit nicht Freitext zurückkommt, den ich anschliessend parsen müsste. Zu jedem Wert meldet das Modell zwei Dinge: seine Konfidenz und **den wörtlichen Textausschnitt, aus dem es den Wert gelesen hat**.

Dieses Zitat ist der Schlüssel zu DA-7. Ohne es wäre die Fundstelle nicht bestimmbar.

Ausgelesen werden elf Felder: Produktname, Beschreibung, EAN, Hersteller-Nummer, Lieferanten-Nummer, Marke, Gewicht, Länge, Breite, Höhe, Preis. Was in keine dieser Kategorien fällt, wird als freies Attribut übernommen statt verworfen.

Jeder ausgehende Aufruf hat ein Zeitlimit. Bei 429 und 5xx wird mit wachsendem Abstand wiederholt. Verbrauchte Token, Anzahl Aufrufe und Dauer werden je Extraktion gespeichert — das ist die Grundlage für die Wirtschaftlichkeitsbetrachtung in Sprint 2.

**Betroffen:** `src/infrastructure/claude/`, `src/application/extract_document.rs`

### DA-7 · Fundstelle im Dokument belegen

**Das ist das Herzstück der Arbeit.**

![Woher die Koordinaten kommen](docs/images/anchor.svg)

Das Modell sagt: „Ich habe 141 g gelesen, und zwar aus dem Text `141 g`." Was es **nicht** sagt, ist, wo das steht. Diese Frage beantwortet pdfium: Es sucht den Wortlaut im Dokument und vermisst das umschliessende Rechteck.

Der Unterschied ist grundlegend. Würde ich das Modell nach Koordinaten fragen, bekäme ich plausible Zahlen, die ich nicht prüfen kann. So stammt der Wert vom Modell und die Geometrie aus dem Dokument — zwei unabhängige Quellen, und die zweite überprüft die erste.

**Ein Zitat, das sich nicht finden lässt, wird zum Befund.** Das ist der eigentliche Gewinn: Ein Wert, auf den das Modell nicht zeigen kann, stand möglicherweise nie auf der Seite. Statt ihn stillschweigend zu übernehmen, wird er markiert.

Die Koordinaten sind seitenrelativ in Prozent gespeichert, dazu das Seitenverhältnis. So bleibt die Fläche unabhängig davon, in welcher Grösse ein Dokument später dargestellt wird — die grafische Hervorhebung ist DA-23 in Sprint 3.

**Was mich Zeit gekostet hat:**

Die Textsuche darf nicht exakt sein. Ein PDF bricht Zeilen um und setzt Leerzeichen, wo im Layout welche gebraucht werden, nicht wo im Text welche stehen. Ein Zitat wie `12,5 x 8,4 x 5,1 cm` kann im Dokument über einen Zeilenumbruch verteilt sein. Die Suche normalisiert deshalb Leerraum, bevor sie vergleicht.

Und die pdfium-Sache: Die Bibliothek initialisiert prozessweiten Zustand und verweigert eine zweite Bindung. Im ersten Anlauf band jeder Aufruf neu, was im Einzeltest funktionierte und beim parallelen Testlauf abstürzte. Die Fehlermeldung deutete auf ein Speicherproblem, was in die Irre führte. Die Lösung ist ein Singleton hinter einem Mutex — und die Erkenntnis, dass eine C-Bibliothek eigene Regeln mitbringt, egal wie sicher die Sprache darüber ist.

**Betroffen:** `src/application/pipeline/anchor.rs`, `src/infrastructure/pdf/anchor.rs`

### DA-8 · Werte vereinheitlichen und prüfen

**Zwei Schritte ohne Modell.**

Nach der Extraktion greifen Regeln. Erst Vereinheitlichung: Kilogramm zu Gramm, Zentimeter zu Millimeter, Preise zu ganzen Rappen. Dann Prüfung: EAN-13-Prüfziffer rechnen, Plausibilitätsgrenzen, Pflichtfelder.

Eine kombinierte Massangabe wie `12,5 x 8,4 x 5,1 cm` steht im Katalog in einer einzigen Zelle und wird per Regel in Länge, Breite und Höhe zerlegt. Das ist bewusst keine Aufgabe für das Modell: Eine Zeichenkette an `x` zu trennen und in Millimeter umzurechnen ist deterministisch, und was deterministisch geht, sollte nicht geraten werden.

Der Grundsatz dahinter:

> **Ein Regelergebnis schlägt die Selbsteinschätzung des Modells — in beide Richtungen.**

Sagt das Modell „hohe Konfidenz" und die EAN-Prüfziffer stimmt nicht, gilt die Prüfziffer. Sagt das Modell „unsicher" und alle Regeln greifen sauber, steigt die Konfidenz. Damit hat die Konfidenz eine überprüfbare Grundlage statt einer behaupteten.

Befunde tragen einen Schweregrad: `Rejected` für unbrauchbar, `Suspect` für fragwürdig. Ein unlesbarer Wert wird gemeldet und **bleibt erhalten**, statt verworfen zu werden — der Prüfer soll sehen, was dastand.

**Betroffen:** `src/application/pipeline/normalise.rs`, `validate.rs`, `split_dimensions.rs`

### DA-9 und DA-10 · Protokoll und Fehlerbehandlung

Das Protokoll hält nicht nur fest, **wer** gehandelt hat, sondern auch **ob die Person selbst gehandelt hat oder ein Modell in ihrem Auftrag**. Ein vom Modell gelesener Wert ist keine Entscheidung der Person, und ein Protokoll, das beides gleich behandelt, wäre irreführend. Bei maschinellen Handlungen wird zusätzlich das Modell vermerkt.

An der HTTP-Grenze hat jede Fehlerantwort dieselbe Form:

```json
{ "error": { "code": "conflict", "message": "this document was already uploaded as diplomarbeit-test.pdf" } }
```

Statuscodes sind bewusst gewählt: 400, 404, 409, 413, 422, 500, 503. Interne Details werden geloggt, nie ausgeliefert. Die Ursachenkette bleibt über `#[source]` erhalten, damit im Log die vollständige Kette steht und beim Aufrufer nur, was er verwerten kann.

Im anfragebearbeitenden Code gibt es kein `unwrap()` und kein `expect()`. Beides ist in Tests erlaubt und beim Start, wo ein Fehlschlag den Prozess tatsächlich beenden soll.

**Betroffen:** `src/infrastructure/db/audit_log.rs`, `src/api/error.rs`

### Die Pipeline im Ganzen

![Die Extraktions-Pipeline](docs/images/pipeline.svg)

Die sechs Schritte sind feste Knoten, keine Agentenschleife. Das war eine bewusste Entscheidung: Die Reihenfolge steht vorher fest, und wo die Reihenfolge feststeht, ist eine Schleife, die sich selbst überlegt, was als Nächstes kommt, nur eine teurere Art, dasselbe zu tun.

| Knoten | Modell? | Warum |
|---|---|---|
| extract | ja | Layout und Tabellen lesen braucht ein Sprachmodell |
| anchor | nein | ein Zitat im PDF finden ist Textsuche |
| normalise | nein | Einheiten umrechnen ist Zeichenkettenverarbeitung |
| validate | nein | Prüfziffern und Grenzwerte sind Arithmetik |
| repair | nur bei Bedarf | läuft nur auf dem, was die Regeln nicht klären konnten |
| score | nein | verbindet Modellangabe mit Regelergebnis |

**Ein sauberes Dokument kostet genau einen Modellaufruf.** Das ist bei der Messung unten belegt.

---

## Sprint 1 Testing

Aus der Rückmeldung zur letzten Arbeit: *„Ab einer gewissen Komplexität erwarte ich Unit- und Integrationstests."* Das war berechtigt, und hier ist es von Anfang an berücksichtigt.

### Testsetup

Damit die Zahlen reproduzierbar sind, hier das vollständige Setup:

```bash
docker compose up -d       # PostgreSQL: 5442 Betrieb, 5443 Mock, 5444 Test

cargo fmt --check
cargo clippy --all-targets --all-features -- -D warnings
PIMFLOW_TEST_DATABASE_URL=postgres://pimflow:pimflow@localhost:5444/pimflow_test cargo test
```

Die Testdatenbank liegt auf `tmpfs` und **jeder Test legt sein eigenes Schema an**. Die Tests sind damit voneinander unabhängig, in beliebiger Reihenfolge lauffähig und hinterlassen nichts. Ohne gesetzte `PIMFLOW_TEST_DATABASE_URL` überspringen sich die Integrationstests selbst und nur die Unit-Tests laufen.

### Ergebnis

Ausgeführt am 15.09.2026, Rust 1.97.1, macOS 15.6:

| Prüfung | Ergebnis | Dauer |
|---|---|---|
| `cargo fmt --check` | sauber | — |
| `cargo clippy -- -D warnings` | sauber, keine Warnung | — |
| Unit-Tests | **324 bestanden**, 0 fehlgeschlagen | 0,10 s |
| Integrationstests | **19 bestanden**, 0 fehlgeschlagen | 0,94 s |
| **Total** | **343 Tests, alle grün** | 1,04 s |

Verteilt über 39 Dateien. Die Schwerpunkte liegen dort, wo Fehler wehtun:

| Bereich | Tests |
|---|---|
| `domain/` (Regeln, Wertobjekte) | 100 |
| `application/` (Anwendungsfälle, Pipeline) | 98 |
| `infrastructure/claude/` (Modellanbindung) | 73 |
| `infrastructure/shopify/` (Vorarbeit Sprint 2) | 24 |
| `infrastructure/pdf/` (Fundstellensuche) | 12 |
| `config.rs` (Konfigurationsprüfung) | 9 |
| `infrastructure/storage/` (Dateiablage) | 7 |
| Integrationstests über HTTP | 19 |

**Dass 324 Unit-Tests in einer Zehntelsekunde durchlaufen, ist kein Zufall, sondern das Ergebnis der Architektur.** Sie brauchen weder Datenbank noch Netzwerk, weil die Fachlogik keines von beidem kennt. Wären die Regeln in den Handlern, bräuchte jeder dieser Tests einen Server.

### Was getestet wird

- **Grenzfälle statt Normalfälle.** Leere Eingabe, negatives Gewicht, überlanger Name, Komma statt Punkt, EAN mit falscher Prüfziffer.
- **Verhalten, nicht Implementierung.** Die Tests fragen, was herauskommt, nicht wie es zustande kam.
- **Feste Daten.** Keine Abhängigkeit von Uhrzeit oder Zufallsreihenfolge.
- **Die Modellantwort wird gegen eine aufgezeichnete Antwort geprüft**, nicht gegen einen Live-Aufruf. Ein Test, der die API ruft, prüft das Netz mit.

---

## Sprint 1 Review

### Die Messung

Der mit dem Kunden vereinbarte Testdatensatz ([demo/test.pdf](demo/test.pdf), SHA-256 `7930a9cf…5efd9`) enthält sechs Produkte mit je elf Feldern. **Die Sollwerte wurden von Hand aus dem Dokument abgelesen, nicht maschinell erzeugt** — ein Massstab, den das Modell selbst erstellt hat, würde das Modell an sich selbst messen.

Zwei der 66 Felder sind bewusst leer: Sie stehen im Dokument nicht und müssen als fehlend erkannt werden, nicht erfunden.

Die Fixture wird über die Prüfsumme der Datei erkannt, nicht über den Dateinamen. Ein Name lässt sich jedem Upload geben, eine Prüfsumme nicht — so kann keine Messung gegen ein Dokument entstehen, für das niemand Sollwerte hinterlegt hat.

![Messung am Testdatensatz](docs/images/messung.svg)

**Gemessen am 15.09.2026** über `GET /api/documents/{id}/accuracy`:

| Kennzahl | Ergebnis |
|---|---|
| Erwartete Attributwerte | 66 |
| Korrekt extrahiert | **66** |
| Falsch | 0 |
| Fehlend | 0 |
| Erfunden | 0 |
| **Correctness** | **100,0 %** (Ziel: 99 %) |
| Produkte erwartet / erkannt | 6 / 6 |
| Werte mit belegter Fundstelle | 64 von 66 (96,97 %) |
| Modellaufrufe | 1 |
| Modell | `claude-haiku-4-5` |
| Tokens | 6 445 Eingabe, 3 041 Ausgabe |
| Dauer | 40,7 s |

Je Produkt:

| Produkt | Korrekt | Mit Fundstelle |
|---|---|---|
| Logitech MX Master 3S | 11 / 11 | 11 / 11 |
| Logitech MX Keys S | 11 / 11 | 11 / 11 |
| Logitech Brio 4K | 11 / 11 | 10 / 11 |
| Anker 737 Power Bank | 11 / 11 | 11 / 11 |
| Samsung T9 SSD 2TB | 11 / 11 | 10 / 11 |
| TP-Link Deco X50 | 11 / 11 | 11 / 11 |

**Die beiden Werte ohne Fundstelle sind genau die zwei Felder, die im Dokument nicht vorkommen** — `supplier_sku` bei der Brio 4K und `weight_grams` bei der Samsung T9. Beide wurden korrekt als fehlend gemeldet. Ein Feld, das nicht dasteht, hat nichts zu verankern.

Das ist mir das liebste Einzelergebnis der Messung. Nicht die 100 %, sondern diese zwei Lücken: Genau dort, wo ein Sprachmodell erfahrungsgemäss etwas Plausibles erfindet, hat es nichts geliefert.

### Was die Zahl nicht sagt

Ein ehrlicher Vorbehalt, und ich möchte ihn lieber selbst formulieren als im Kolloquium dazu gefragt werden:

**100 % an einem Dokument sind nicht 100 % im Betrieb.** Der Testdatensatz ist realistisch aufgebaut, aber es ist ein Dokument. Ein Katalog mit anderem Layout, schlechterem Druck oder einer Sprache, die das Modell seltener gesehen hat, kann zu anderen Ergebnissen führen. Die breitere Messung über mehrere Dokumente ist DA-19 in Sprint 2.

Was die Zahl belegt, ist enger und trotzdem aussagekräftig: Die Pipeline liest einen realistischen Lieferantenkatalog ohne Fehler und ohne zu erfinden, und sie kann für 96,97 % der Werte zeigen, wo sie stehen.

**Bemerkenswert am Rande:** Die Extraktion lief mit `claude-haiku-4-5`, dem kleinsten Modell der Familie. Das war ursprünglich nicht so geplant — das Design sah Opus vor. Dass das kleinste Modell 100 % erreicht, spricht dafür, dass die Arbeit in der Pipeline steckt und nicht in roher Modellstärke. Für die Wirtschaftlichkeitsbetrachtung in Sprint 2 ist das der interessanteste Befund aus diesem Sprint.

### Sprint-Ziele gegen Ergebnis

| Ziel | Ergebnis | Nachweis |
|---|---|---|
| Dokument hochladbar | erreicht | `POST /api/documents`, 19 Integrationstests |
| Produktdaten ausgelesen | erreicht | 6 von 6 Produkten, 66 von 66 Feldern |
| Werte vereinheitlicht und geprüft | erreicht | Gewichte in Gramm, Masse in Millimetern, Preise in Rappen; EAN-Prüfziffer gerechnet |
| Fundstelle nachweisbar | erreicht | 64 von 66 Werten mit Seite und Rechteck |
| Alles über die API vorführbar | erreicht | Vorführung zur ZP1 über `curl` |

**Alle 51 Story Points abgeschlossen. Alle elf Tickets erfüllen die Definition of Done.**

---

## Zwischenpräsentation 1

**Termin:** 19.10.2026, 11:30 – 12:00 Uhr
**Teilnehmende:** Corrado Parisi (Schulexperte), Andrej Birka (Firmenexperte)
**Form:** Sprint Review — Sprint Backlog, Fortschritt und umgesetzte Funktionen gemeinsam durchgehen

**Geplanter Ablauf**

1. Sprint Backlog und Burndown aus Linear
2. Live-Vorführung über `curl`: Upload, Extraktion, Vorschläge mit Konfidenz und Koordinaten als JSON
3. Die Messung: 66 von 66 Werten, mit dem Testsetup dahinter
4. Die Fundstellen-Mechanik an einem Beispiel
5. Abweichung von der Sprint-Reihenfolge ansprechen und begründen
6. Ausblick auf Sprint 2

Die Vorführung kommt bewusst früh. Das ist die Konsequenz aus der Rückmeldung zur letzten Präsentation: *„Ich würde die Demo früher zeigen. Das funktionierende Erlebnis ist dein stärkster Beleg."*

> **Nach dem 19.10.2026 einzufügen:** Rückmeldung beider Experten, daraus abgeleitete Massnahmen und deren Umsetzung in Sprint 2.

---

## Sprint 1 Retrospektive

### Was gut lief

- **Die Architekturentscheidung hat sich sofort ausgezahlt.** 324 Unit-Tests ohne Datenbank in 0,10 Sekunden bedeuten, dass ich sie tatsächlich bei jeder Änderung laufen lasse. Ein Testlauf, der eine Minute dauert, wird übersprungen.
- **Die Trennung von Modell und Regel war richtig.** Alles, was deterministisch geht, geht deterministisch. Das Modell macht genau einen Schritt.
- **Der Fundstellen-Nachweis funktioniert und ist das stärkste Argument der Arbeit.** Er beantwortet die Frage, die bei jedem KI-Projekt zuerst kommt.
- **Testdatensatz und Sollwerte vor der Messung festgelegt.** Damit ist die Messung ein Nachweis und keine nachträgliche Rechtfertigung.

### Was schwierig war

- **pdfium.** Prozessweiter Zustand, keine zweite Bindung, und eine Fehlermeldung, die auf ein Speicherproblem hindeutete. Der Fehler trat nur im parallelen Testlauf auf, was die Suche verlängert hat. Gekostet: etwa ein halber Tag.
- **Der erste Schnitt der Ports war zu fein.** Traits mit fünfzehn Methoden, von denen drei gebraucht wurden. Neu geschnitten aus der Sicht des Anwendungsfalls statt aus der Sicht der Tabelle.
- **Die Textsuche musste unschärfer werden als gedacht.** Ein PDF setzt Leerzeichen und Zeilenumbrüche nach Layout, nicht nach Text. Ohne Normalisierung des Leerraums fand die Suche korrekte Zitate nicht wieder.

### Schätzung gegen Wirklichkeit

| Ticket | Geschätzt | Gefühlter Aufwand | Abweichung |
|---|---|---|---|
| DA-7 Fundstelle belegen | 8 | ~10 | zu niedrig — pdfium war unbekanntes Gebiet |
| DA-2 Schichtenarchitektur | 3 | ~5 | zu niedrig — Ports zweimal geschnitten |
| DA-6 Extraktion | 8 | ~7 | leicht zu hoch — das Schema hat viel abgenommen |
| übrige acht Tickets | 32 | ~32 | zutreffend |

**Muster:** Ich unterschätze konsequent Aufgaben mit einer Technologie, die ich noch nicht kenne, und schätze Vertrautes zuverlässig. Bei pdfium war nicht die Aufgabe schwer, sondern das Verhalten der Bibliothek unbekannt.

**Massnahme für Sprint 2:** Für jede Story mit unbekannter Technologie wird ein Punkt Aufschlag eingeplant, oder eine Zeitbox zur Erkundung vorgeschaltet. Betrifft in Sprint 2 vor allem die Bildrecherche, wo die serverseitige Websuche neu ist.

### Was ich mitnehme

**Wo etwas herkommt, ist wichtiger als wie sicher es wirkt.** Ein Modell mit „hoher Konfidenz" sagt nur, dass es zu seiner Antwort steht. Ein Zitat, das im Dokument wiedergefunden wird, ist ein Beleg. Der ganze Aufbau der Pipeline folgt aus diesem Unterschied.

**Was deterministisch geht, sollte nicht geraten werden.** Eine EAN-Prüfziffer ist Arithmetik. Eine Masszerlegung ist Zeichenkettenverarbeitung. Beides an ein Modell zu geben, kostet Geld und macht das Ergebnis unprüfbar.

**Eine C-Bibliothek bringt eigene Regeln mit**, unabhängig davon, wie sicher die Sprache darüber ist. Rust schützt vor vielem, aber nicht vor prozessweitem Zustand in fremdem Code.

---

## Sprint 1 Fazit

**Das Fundament steht, und es steht belegt.**

Ein Lieferantendokument geht hinein, strukturierte Produktvorschläge kommen heraus, und zu fast jedem Wert lässt sich zeigen, wo er im Dokument steht. Am vereinbarten Testdatensatz wurden 66 von 66 Attributwerten korrekt erkannt, ohne einen erfundenen Wert.

Was mir an diesem Sprint am meisten gefällt, ist nicht die Zahl. Es sind die zwei Felder, die das Modell **nicht** geliefert hat. Genau dort, wo ein Sprachmodell normalerweise etwas Plausibles hinschreibt, kam nichts — weil im Dokument nichts stand.

Sichtbar ist davon bisher nichts. Es gibt keine Oberfläche, nur API-Antworten in JSON. Aber der Teil mit dem echten Risiko ist erledigt und gemessen, und das war der Zweck dieses Sprints.

**Als Nächstes:** Sprint 2 — die Extraktion wird gehärtet, das Produktbild kommt dazu, und ein freigegebenes Produkt findet seinen Weg in den Shopify-Shop.

---
