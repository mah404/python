# Python Abschlussprojekt Tag 4

## IT-Support und Systemadmin Diagnose-Tool

Dieses Projekt ist ein Konsolenprogramm fuer den IT-Support. Es kann Tickets
erstellen, vorhandene CSV-Dateien anzeigen, Logdateien durchsuchen, Ordner
analysieren und einen Systemreport schreiben.

## Start

```bash
python main.py
```

Das Programm zeigt danach ein Menue an. Eine Funktion wird durch Eingabe der
passenden Zahl gestartet. Nach jeder Aktion erscheint das Menue erneut.

## Funktionen

- Neues Ticket erstellen und in `tickets/neue_tickets.txt` speichern
- Neue Tickets zusaetzlich in `data/tickets.csv` eintragen
- Bestehende Tickets aus `data/tickets.csv` anzeigen
- Benutzer aus `data/benutzer.csv` anzeigen und inaktive Benutzer markieren
- Inventar aus `data/inventar.csv` anzeigen und problematische Geraete markieren
- Logdatei `logs/server.log` nach Suchwort durchsuchen
- Ordnerpfad analysieren und Dateien/Unterordner zaehlen
- Systemreport in `reports/system_report.txt` erstellen

## Projektstruktur

```text
python_abschlussprojekt_tag4/
  main.py
  README.md
  data/
    inventar.csv
    benutzer.csv
    tickets.csv
  logs/
    server.log
  reports/
    system_report.txt
  tickets/
    neue_tickets.txt
```

## Hinweise

Die Pfade im Programm werden relativ zum Projektordner ermittelt. Deshalb kann
das Projekt auch aus einem anderen Arbeitsverzeichnis heraus gestartet werden.
