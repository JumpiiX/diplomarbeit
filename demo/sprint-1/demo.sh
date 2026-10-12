#!/usr/bin/env bash
#
# Sprint 1 — Vorführung über die HTTP-API
#
# Zeigt den Ablauf aus Sprint 1 ohne Oberfläche: Dokument hochladen, auslesen
# lassen, Ergebnis mit Fundstellen anzeigen. Der Backlog hält für Sprint 1 und 2
# fest, dass jede Anforderung über die HTTP-API nachweisbar ist und die
# Vorführung über API-Aufrufe läuft — dieses Skript ist genau das, nur lesbar
# formatiert.
#
# Jeder Schritt druckt den curl-Aufruf, den er tatsächlich absetzt. Das Skript
# fügt der Anwendung nichts hinzu; es ruft dieselben Endpunkte auf, die auch die
# Oberfläche aus Sprint 3 benutzt.
#
# Aufruf:
#   ./demo.sh upload ../test.pdf
#   ./demo.sh extract
#   ./demo.sh show
#   ./demo.sh accuracy
#   ./demo.sh reset

set -euo pipefail

API="${PIMFLOW_API:-http://localhost:8080}"
ACTOR="${PIMFLOW_ACTOR:-David Unterguggenberger}"
STATE="$(dirname "$0")/.letztes-dokument"

bold=$'\033[1m'; dim=$'\033[2m'; reset=$'\033[0m'

zeige_befehl() {
  printf '%s\n' "${dim}\$ $*${reset}"
  echo
}

titel() {
  echo
  printf '%s\n' "${bold}$1${reset}"
  printf '%s\n' "$(printf '─%.0s' $(seq 1 ${#1}))"
  echo
}

pruefe_server() {
  if ! curl -sf "$API/api/health" >/dev/null 2>&1; then
    echo "Der Server antwortet nicht auf $API."
    echo
    echo "  cd ../../../pimflow-backend && cargo run"
    echo
    exit 1
  fi
}

dokument_id() {
  if [ ! -f "$STATE" ]; then
    echo "Kein Dokument vorgemerkt. Zuerst: ./demo.sh upload ../test.pdf" >&2
    exit 1
  fi
  cat "$STATE"
}

befehl_upload() {
  local datei="${1:-}"

  if [ -z "$datei" ]; then
    echo "Aufruf: ./demo.sh upload <datei.pdf>" >&2
    exit 1
  fi

  if [ ! -f "$datei" ]; then
    echo "Datei nicht gefunden: $datei" >&2
    exit 1
  fi

  pruefe_server
  titel "DA-5 · Lieferantendokument hochladen"

  zeige_befehl "curl -X POST $API/api/documents \\
     -H 'X-Actor-Name: $ACTOR' \\
     -F 'file=@$datei'"

  local antwort
  antwort=$(curl -s -X POST "$API/api/documents" \
    -H "X-Actor-Name: $ACTOR" \
    -F "file=@$datei")

  echo "$antwort" | python3 "$(dirname "$0")/formatiere.py" upload

  echo "$antwort" | python3 -c 'import sys,json; print(json.load(sys.stdin)["id"])' > "$STATE"
}

befehl_extract() {
  pruefe_server
  local id; id=$(dokument_id)

  titel "DA-6 · Produktdaten mit einem Sprachmodell auslesen"

  zeige_befehl "curl -X POST '$API/api/documents/$id/extract?images=false' \\
     -H 'X-Actor-Name: $ACTOR'"

  echo "Das Dokument wird gelesen. Das dauert etwa zwanzig Sekunden."
  echo

  curl -s -X POST "$API/api/documents/$id/extract?images=false" \
    -H "X-Actor-Name: $ACTOR" \
    | python3 "$(dirname "$0")/formatiere.py" extract
}

befehl_show() {
  pruefe_server
  local id; id=$(dokument_id)

  titel "DA-7 · Fundstelle im Dokument belegen"

  zeige_befehl "curl '$API/api/documents/$id/proposals'"

  curl -s "$API/api/documents/$id/proposals" \
    | python3 "$(dirname "$0")/formatiere.py" show
}

befehl_accuracy() {
  pruefe_server
  local id; id=$(dokument_id)

  titel "DA-19 · Die Extraktion gegen bekannte Sollwerte messen"

  zeige_befehl "curl '$API/api/documents/$id/accuracy'"

  local status
  status=$(curl -s -o /dev/null -w '%{http_code}' "$API/api/documents/$id/accuracy")

  if [ "$status" = "404" ]; then
    echo "Für dieses Dokument sind keine Sollwerte hinterlegt."
    echo
    echo "Gemessen wird nur gegen den vereinbarten Testdatensatz, erkannt an"
    echo "seiner Prüfsumme. Dafür: ./demo.sh upload ../test.pdf"
    echo
    exit 1
  fi

  curl -s "$API/api/documents/$id/accuracy" \
    | python3 "$(dirname "$0")/formatiere.py" accuracy
}

befehl_reset() {
  pruefe_server
  titel "Testdaten löschen"

  zeige_befehl "curl -X DELETE $API/api/installation/contents \\
     -H 'X-Actor-Name: $ACTOR'"

  curl -s -X DELETE "$API/api/installation/contents" \
    -H "X-Actor-Name: $ACTOR" \
    | python3 "$(dirname "$0")/formatiere.py" reset

  rm -f "$STATE"
}

case "${1:-}" in
  upload)   shift; befehl_upload "${1:-}" ;;
  extract)  befehl_extract ;;
  show)     befehl_show ;;
  accuracy) befehl_accuracy ;;
  reset)    befehl_reset ;;
  *)
    echo "Aufruf: ./demo.sh {upload <datei.pdf>|extract|show|accuracy|reset}"
    exit 1
    ;;
esac
