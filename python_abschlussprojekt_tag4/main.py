import csv
import subprocess
from datetime import datetime
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
LOG_DIR = BASE_DIR / "logs"
REPORT_DIR = BASE_DIR / "reports"
TICKET_DIR = BASE_DIR / "tickets"


# Kleine Hilfsfunktion, damit das Menue nicht sofort weiter springt.
def pause():
    input("\nWeiter mit Enter...")


# Hier pruefe ich, dass der Benutzer nicht einfach leer Enter drueckt.
def read_required(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Die Eingabe darf nicht leer sein.")


# Damit die Ausgaben im Terminal uebersichtlicher aussehen.
def print_heading(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# Diese Funktion benutze ich fuer alle CSV-Dateien, damit ich den Code nicht wiederholen muss.
def read_csv_file(path):
    try:
        with path.open("r", encoding="utf-8-sig", newline="") as file:
            return list(csv.DictReader(file))
    except FileNotFoundError:
        print(f"Datei wurde nicht gefunden: {path}")
    except OSError as error:
        print(f"Datei konnte nicht gelesen werden: {error}")
    return []


# Aufgabe 2: Hier wird ein neues Ticket abgefragt und als Datei gespeichert.
def create_ticket():
    print_heading("Neues Ticket erstellen")
    ticket = {
        "name": read_required("Name: "),
        "abteilung": read_required("Abteilung: "),
        "problem": read_required("Problem: "),
        "prioritaet": read_required("Prioritaet: "),
        "status": read_required("Status: "),
    }

    TICKET_DIR.mkdir(exist_ok=True)
    ticket_file = TICKET_DIR / "neue_tickets.txt"
    with ticket_file.open("a", encoding="utf-8") as file:
        file.write(f"Name: {ticket['name']}\n")
        file.write(f"Abteilung: {ticket['abteilung']}\n")
        file.write(f"Problem: {ticket['problem']}\n")
        file.write(f"Prioritaet: {ticket['prioritaet']}\n")
        file.write(f"Status: {ticket['status']}\n")
        file.write("-" * 40 + "\n")

    append_ticket_to_csv(ticket)
    print(f"\nTicket wurde gespeichert in: {ticket_file}")


# Zusatz zu Aufgabe 2: Das neue Ticket wird auch noch in die CSV-Datei geschrieben.
def append_ticket_to_csv(ticket):
    csv_file = DATA_DIR / "tickets.csv"
    rows = read_csv_file(csv_file)
    next_id = 1001
    if rows:
        try:
            next_id = max(int(row["ticket_id"]) for row in rows) + 1
        except (KeyError, ValueError):
            next_id = len(rows) + 1001

    file_exists = csv_file.exists()
    with csv_file.open("a", encoding="utf-8", newline="") as file:
        fieldnames = ["ticket_id", "name", "abteilung", "problem", "prioritaet", "status"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow({"ticket_id": next_id, **ticket})


# Aufgabe 3: Hier lese ich die vorhandenen Tickets aus der CSV-Datei und zeige sie an.
def show_tickets():
    print_heading("Bestehende Tickets")
    tickets = read_csv_file(DATA_DIR / "tickets.csv")
    if not tickets:
        print("Keine Tickets gefunden.")
        return

    for ticket in tickets:
        print(
            f"#{ticket.get('ticket_id', '-')}: {ticket.get('problem', '-')} | "
            f"{ticket.get('name', '-')} | Prioritaet: {ticket.get('prioritaet', '-')} | "
            f"Status: {ticket.get('status', '-')}"
        )


# Aufgabe 4: Hier zeige ich die Benutzerliste und markiere gesperrte oder inaktive Benutzer.
def show_users():
    print_heading("Benutzerliste")
    users = read_csv_file(DATA_DIR / "benutzer.csv")
    if not users:
        print("Keine Benutzer gefunden.")
        return

    search = input("Nach Username suchen (leer = alle anzeigen): ").strip().lower()
    for user in users:
        username = user.get("username", "")
        if search and search not in username.lower():
            continue

        status = user.get("status", "")
        print(
            f"{username:10} | {user.get('name', '-'):20} | "
            f"{user.get('abteilung', '-'):15} | {user.get('rolle', '-'):15} | {status}"
        )
        if status.lower() != "aktiv":
            print("  Achtung: Dieser Benutzer ist nicht aktiv.")


# Aufgabe 5: Hier zeige ich die Inventarliste und gebe eine Warnung bei Problemen aus.
def show_inventory():
    print_heading("Inventarliste")
    inventory = read_csv_file(DATA_DIR / "inventar.csv")
    if not inventory:
        print("Keine Inventardaten gefunden.")
        return

    search = input("Nach Geraete-ID suchen (leer = alle anzeigen): ").strip().lower()
    warning_statuses = {"defekt", "wartung", "verloren"}
    for item in inventory:
        device_id = item.get("geraete_id", "")
        if search and search not in device_id.lower():
            continue

        status = item.get("status", "")
        print(
            f"{device_id:8} | {item.get('geraet', '-'):10} | "
            f"{item.get('benutzer', '-'):20} | {item.get('standort', '-'):15} | {status}"
        )
        if status.lower() in warning_statuses:
            print("  Warnung: Dieses Geraet braucht Aufmerksamkeit.")


# Aufgabe 6: Hier kann man in der Logdatei nach ERROR, WARN oder einem anderen Wort suchen.
def search_log():
    print_heading("Logdatei durchsuchen")
    search = read_required("Suchwort eingeben (z. B. ERROR, WARN, FAILED): ").lower()
    log_file = LOG_DIR / "server.log"
    matches = []

    try:
        with log_file.open("r", encoding="utf-8") as file:
            for line in file:
                if search in line.lower():
                    matches.append(line.strip())
    except FileNotFoundError:
        print(f"Logdatei wurde nicht gefunden: {log_file}")
        return
    except OSError as error:
        print(f"Logdatei konnte nicht gelesen werden: {error}")
        return

    if matches:
        for line in matches:
            print(line)
    else:
        print("Keine passenden Logeintraege gefunden.")


# Aufgabe 7: Hier pruefe ich einen Ordner und zaehle Dateien und Unterordner.
def analyze_folder():
    print_heading("Ordner analysieren")
    path = Path(read_required("Ordnerpfad eingeben: ")).expanduser()

    if not path.exists() or not path.is_dir():
        print("Der Ordner wurde nicht gefunden.")
        return

    files = 0
    folders = 0
    try:
        for entry in path.iterdir():
            if entry.is_file():
                files += 1
            elif entry.is_dir():
                folders += 1
    except OSError as error:
        print(f"Ordner konnte nicht gelesen werden: {error}")
        return

    print(f"Dateien: {files}")
    print(f"Ordner: {folders}")


# Zusatz fuer Aufgabe 8: Ich zaehle hier automatisch ERROR und WARN in der Logdatei.
def count_log_warnings():
    result = {"ERROR": 0, "WARN": 0}
    log_file = LOG_DIR / "server.log"
    try:
        with log_file.open("r", encoding="utf-8") as file:
            for line in file:
                upper_line = line.upper()
                if "ERROR" in upper_line:
                    result["ERROR"] += 1
                if "WARN" in upper_line:
                    result["WARN"] += 1
    except OSError:
        pass
    return result


# Aufgabe 8: Hier erstelle ich den Systemreport als Textdatei im reports Ordner.
def create_system_report():
    print_heading("Systemreport erstellen")
    REPORT_DIR.mkdir(exist_ok=True)
    report_file = REPORT_DIR / "system_report.txt"
    log_counts = count_log_warnings()
    project_file_count = sum(1 for entry in BASE_DIR.rglob("*") if entry.is_file())

    try:
        command = subprocess.run(
            ["cmd", "/c", "cd"],
            cwd=BASE_DIR,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=10,
        )
        command_output = command.stdout.strip() or command.stderr.strip()
    except (OSError, subprocess.SubprocessError) as error:
        command_output = f"Systembefehl konnte nicht ausgefuehrt werden: {error}"

    with report_file.open("w", encoding="utf-8") as file:
        file.write("Systemreport\n")
        file.write("=" * 40 + "\n")
        file.write(f"Datum und Uhrzeit: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        file.write(f"Aktuelles Arbeitsverzeichnis: {Path.cwd()}\n")
        file.write(f"Projektordner: {BASE_DIR}\n")
        file.write(f"Anzahl Dateien im Projektordner: {project_file_count}\n\n")
        file.write("Log-Zusammenfassung\n")
        file.write(f"ERROR-Eintraege: {log_counts['ERROR']}\n")
        file.write(f"WARN-Eintraege: {log_counts['WARN']}\n\n")
        file.write("Ergebnis Systembefehl 'cd'\n")
        file.write(command_output + "\n")

    print(f"Systemreport wurde erstellt: {report_file}")
    print(f"ERROR: {log_counts['ERROR']} | WARN: {log_counts['WARN']}")


# Aufgabe 1: Das ist das Menue, das beim Start angezeigt wird.
def show_menu():
    print("\nIT-Support und Systemadmin Diagnose-Tool")
    print("1 Neues Ticket erstellen")
    print("2 Bestehende Tickets anzeigen")
    print("3 Benutzerliste anzeigen")
    print("4 Inventarliste anzeigen")
    print("5 Logdatei durchsuchen")
    print("6 Ordner analysieren")
    print("7 Systemreport erstellen")
    print("8 Programm beenden")


# Aufgabe 1: Die while-Schleife sorgt dafuer, dass das Menue immer wieder kommt.
def main():
    actions = {
        "1": create_ticket,
        "2": show_tickets,
        "3": show_users,
        "4": show_inventory,
        "5": search_log,
        "6": analyze_folder,
        "7": create_system_report,
    }

    while True:
        show_menu()
        choice = input("Auswahl eingeben: ").strip()

        if choice == "8":
            print("Programm wird beendet.")
            break

        action = actions.get(choice)
        if action:
            action()
            pause()
        else:
            print("Ungueltige Auswahl. Bitte eine Zahl von 1 bis 8 eingeben.")


if __name__ == "__main__":
    main()
