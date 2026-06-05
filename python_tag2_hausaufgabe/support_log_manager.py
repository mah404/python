# Aufgabe 7 / Zusatzaufgabe: Ich importiere datetime, damit ich Datum und Uhrzeit speichern kann.
from datetime import datetime


# Aufgabe 2: Hier mache ich eine leere Liste fuer die Tickets.
tickets = []


# Aufgabe 3: Diese Funktion macht ein neues Ticket.
def ticket_erstellen():
    # Hier schreibe ich eine Ueberschrift in die Konsole.
    print("\nNeues Ticket erstellen")

    # Hier fragt das Programm nach dem Namen.
    name = input("Name: ")

    # Aufgabe 8: Wenn der Name leer ist, soll das Programm nicht weiter machen.
    if name == "":
        # Hier sage ich dem Benutzer, dass der Name fehlt.
        print("Name darf nicht leer sein.")
        # Hier gehe ich aus der Funktion raus.
        return

    # Hier fragt das Programm nach der Abteilung.
    abteilung = input("Abteilung: ")

    # Hier fragt das Programm nach dem Problem.
    problem = input("Problem: ")

    # Aufgabe 8: Wenn das Problem leer ist, soll das Programm nicht weiter machen.
    if problem == "":
        # Hier sage ich dem Benutzer, dass das Problem fehlt.
        print("Problem darf nicht leer sein.")
        # Hier gehe ich aus der Funktion raus.
        return

    # Zusatzaufgabe: Hier frage ich nach der Prioritaet.
    prioritaet = input("Prioritaet (hoch/mittel/niedrig): ")

    # Hier entferne ich Leerzeichen am Anfang und am Ende.
    prioritaet = prioritaet.strip()

    # Zusatzaufgabe: Hier pruefe ich, ob die Prioritaet richtig ist.
    if prioritaet != "hoch" and prioritaet != "mittel" and prioritaet != "niedrig":
        # Hier sage ich, dass die Prioritaet falsch ist.
        print("Prioritaet ist falsch, ich nehme automatisch mittel.")
        # Hier setze ich die Prioritaet auf mittel.
        prioritaet = "mittel"

    # Hier fragt das Programm nach dem Status.
    status = input("Status: ")

    # Hier entferne ich Leerzeichen am Anfang und am Ende.
    status = status.strip()

    # Hier pruefe ich, ob Status leer ist.
    if status == "":
        # Wenn Status leer ist, nehme ich offen.
        status = "offen"

    # Zusatzaufgabe: Hier hole ich Datum und Uhrzeit.
    datum = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Aufgabe 3: Hier speichere ich ein Ticket als Dictionary.
    ticket = {
        # Hier speichere ich den Namen im Dictionary.
        "name": name,
        # Hier speichere ich die Abteilung im Dictionary.
        "abteilung": abteilung,
        # Hier speichere ich das Problem im Dictionary.
        "problem": problem,
        # Hier speichere ich die Prioritaet im Dictionary.
        "prioritaet": prioritaet,
        # Hier speichere ich den Status im Dictionary.
        "status": status,
        # Hier speichere ich Datum und Uhrzeit im Dictionary.
        "datum": datum,
    }

    # Aufgabe 2: Hier fuege ich das Ticket zur Liste hinzu.
    tickets.append(ticket)

    # Aufgabe 4: Hier oeffne ich die Datei tickets.txt zum Anhaengen.
    with open("tickets.txt", "a", encoding="utf-8") as file:
        
        # opens the file tickets.txt in append mode ("a"), so new data is added to the end of the file without deleting the existing content. The encoding="utf-8" ensures that special characters are saved correctly. The keyword with automatically closes the file after the block of code is finished, and as file creates a variable called file that I can use to write data into the file.
        
        # Hier schreibe ich den Namen in die Datei.
        print("Name:", ticket["name"], file=file)
        # Hier schreibe ich die Abteilung in die Datei.
        print("Abteilung:", ticket["abteilung"], file=file)
        # Hier schreibe ich das Problem in die Datei.
        print("Problem:", ticket["problem"], file=file)
        # Hier schreibe ich die Prioritaet in die Datei.
        print("Prioritaet:", ticket["prioritaet"], file=file)
        # Hier schreibe ich den Status in die Datei.
        print("Status:", ticket["status"], file=file)
        # Hier schreibe ich das Datum in die Datei.
        print("Datum:", ticket["datum"], file=file)
        # Hier mache ich eine Trennlinie zwischen den Tickets.
        print("---", file=file)

    # Hier sage ich, dass das Ticket gespeichert wurde.
    print("Ticket wurde gespeichert.")


# Aufgabe 5: Diese Funktion zeigt alle Tickets aus der Datei.
def tickets_anzeigen():
    # Hier schreibe ich eine Ueberschrift.
    print("\nAlle Tickets anzeigen")

    # Aufgabe 8: Hier benutze ich try, weil die Datei vielleicht fehlt.
    try:
        # Hier oeffne ich tickets.txt zum Lesen.
        with open("tickets.txt", "r", encoding="utf-8") as file:
            # Hier lese ich den ganzen Inhalt der Datei.
            inhalt = file.read()
            # Hier pruefe ich, ob die Datei leer ist.
            if inhalt == "":
                # Hier sage ich, dass es keine Tickets gibt.
                print("Es wurden noch keine Tickets gespeichert.")
            # Sonst gibt es Inhalt.
            else:
                # Hier zeige ich den Inhalt in der Konsole.
                print(inhalt)
    # Aufgabe 8: Hier fange ich den Fehler ab, wenn tickets.txt fehlt.
    except FileNotFoundError:
        # Hier sage ich, dass es noch keine Tickets gibt.
        print("Es wurden noch keine Tickets gespeichert.")


# Aufgabe 6: Diese Funktion erzeugt die Beispiel-Logdatei.
def beispiel_logdatei_erzeugen():
    # Hier oeffne ich server.log zum Schreiben.
    with open("server.log", "w", encoding="utf-8") as file:
        # Hier schreibe ich die erste Logzeile.
        print("2026-05-31 09:00 INFO System gestartet", file=file)
        # Hier schreibe ich die zweite Logzeile.
        print("2026-05-31 09:15 WARNING Speicher fast voll", file=file)
        # Hier schreibe ich die dritte Logzeile.
        print("2026-05-31 09:20 ERROR Druckdienst nicht erreichbar", file=file)
        # Hier schreibe ich die vierte Logzeile.
        print("2026-05-31 09:30 INFO Benutzer angemeldet", file=file)
        # Hier schreibe ich die fuenfte Logzeile.
        print("2026-05-31 09:45 ERROR Netzwerkverbindung unterbrochen", file=file)

    # Hier sage ich, dass server.log erstellt wurde.
    print("server.log wurde erzeugt.")


# Aufgabe 6: Diese Funktion durchsucht die Logdatei.
def logdatei_durchsuchen():
    # Hier fragt das Programm nach dem Suchwort.
    suchwort = input("Suchwort eingeben: ")

    # Aufgabe 8: Hier pruefe ich, ob das Suchwort leer ist.
    if suchwort == "":
        # Hier sage ich, dass das Suchwort nicht leer sein darf.
        print("Suchwort darf nicht leer sein.")
        # Hier gehe ich aus der Funktion raus.
        return

    # Zusatzaufgabe: Hier zaehle ich die gefundenen Zeilen.
    anzahl = 0

    # Zusatzaufgabe: Hier mache ich eine Liste fuer gefundene Zeilen.
    gefundene_zeilen = []

    # Aufgabe 8: Hier benutze ich try, weil server.log vielleicht fehlt.
    try:
        # Hier oeffne ich server.log zum Lesen.
        with open("server.log", "r", encoding="utf-8") as file:
            # Hier gehe ich jede Zeile in der Datei durch.
            for zeile in file:
                # Hier pruefe ich, ob das Suchwort in der Zeile steht.
                if suchwort in zeile:
                    # Hier zeige ich die passende Zeile ohne Leerzeile am Ende.
                    print(zeile.strip())
                    # Hier erhoehe ich den Zaehler um 1.
                    anzahl = anzahl + 1
                    # Hier speichere ich die gefundene Zeile in der Liste.
                    gefundene_zeilen.append(zeile.strip())
    # Aufgabe 8: Hier fange ich den Fehler ab, wenn server.log fehlt.
    except FileNotFoundError:
        # Hier sage ich, dass die Logdatei fehlt.
        print("server.log existiert nicht.")
        # Hier gehe ich aus der Funktion raus.
        return

    # Hier pruefe ich, ob nichts gefunden wurde.
    if anzahl == 0:
        # Hier zeige ich eine klare Nachricht, wenn nichts gefunden wurde.
        print("Keine passenden Zeilen gefunden.")
        # Hier gehe ich aus der Funktion raus.
        return

    # Zusatzaufgabe: Hier speichere ich die Suchergebnisse in eine Datei.
    with open("log_suche_ergebnis.txt", "w", encoding="utf-8") as file:
        # Hier gehe ich jede gefundene Zeile durch.
        for zeile in gefundene_zeilen:
            # Hier schreibe ich die Zeile in die Ergebnisdatei.
            print(zeile, file=file)

    # Hier zeige ich, wie viele Zeilen gefunden wurden.
    print("Gefundene Zeilen:", anzahl)

    # Hier sage ich, dass die Ergebnisdatei geschrieben wurde.
    print("Ergebnis wurde in log_suche_ergebnis.txt gespeichert.")


# Aufgabe 7: Diese Funktion zeigt das Menue.
def menue_anzeigen():
    # Hier mache ich eine Leerzeile und die Ueberschrift.
    print("\nIT-Support Log- und Ticket-Manager")
    # Hier zeige ich Menuepunkt 1.
    print("1 Neues Ticket erstellen")
    # Hier zeige ich Menuepunkt 2.
    print("2 Alle Tickets anzeigen")
    # Hier zeige ich Menuepunkt 3.
    print("3 Logdatei durchsuchen")
    # Hier zeige ich Menuepunkt 4.
    print("4 Beispiel-Logdatei erzeugen")
    # Hier zeige ich Menuepunkt 5.
    print("5 Programm beenden")
    # Zusatzaufgabe: Hier zeige ich Menuepunkt 6.
    print("6 Statistik anzeigen")


# Zusatzaufgabe: Diese Funktion zeigt eine kleine Statistik.
def statistik_anzeigen():
    # Hier mache ich einen Zaehler fuer die Tickets.
    anzahl = 0

    # Hier benutze ich try, weil tickets.txt vielleicht fehlt.
    try:
        # Hier oeffne ich tickets.txt zum Lesen.
        with open("tickets.txt", "r", encoding="utf-8") as file:
            # Hier gehe ich jede Zeile in der Datei durch.
            for zeile in file:
                # Hier suche ich nach der Trennlinie von einem Ticket.
                if zeile.strip() == "---":
                    # Hier erhoehe ich den Zaehler um 1.
                    anzahl = anzahl + 1
    # Hier fange ich den Fehler ab, wenn tickets.txt fehlt.
    except FileNotFoundError:
        # Hier bleibt die Anzahl einfach 0.
        anzahl = 0

    # Hier zeige ich, wie viele Tickets in tickets.txt gespeichert sind.
    print("Gespeicherte Tickets:", anzahl)


# Aufgabe 1 und 9: Hier ist das Hauptprogramm.
def main():
    # Aufgabe 1: Die while-Schleife wiederholt das Menue immer wieder.
    while True:
        # Hier rufe ich die Menue-Funktion auf.
        menue_anzeigen()

        # Hier fragt das Programm nach der Auswahl.
        auswahl = input("Auswahl: ")

        # Hier pruefe ich, ob der Benutzer einfach Enter gedrueckt hat.
        if auswahl == "":
            # Hier erklaere ich, was man eingeben soll.
            print("Bitte eine Zahl von 1 bis 6 eingeben.")
            # Hier gehe ich wieder zum Anfang vom Menue.
            continue

        # Hier pruefe ich, ob der Benutzer 1 eingegeben hat.
        if auswahl == "1":
            # Hier wird ein neues Ticket erstellt.
            ticket_erstellen()

        # Hier pruefe ich, ob der Benutzer 2 eingegeben hat.
        elif auswahl == "2":
            # Hier werden alle Tickets angezeigt.
            tickets_anzeigen()

        # Hier pruefe ich, ob der Benutzer 3 eingegeben hat.
        elif auswahl == "3":
            # Hier wird die Logdatei durchsucht.
            logdatei_durchsuchen()

        # Hier pruefe ich, ob der Benutzer 4 eingegeben hat.
        elif auswahl == "4":
            # Hier wird eine Beispiel-Logdatei erzeugt.
            beispiel_logdatei_erzeugen()

        # Hier pruefe ich, ob der Benutzer 5 eingegeben hat.
        elif auswahl == "5":
            # Hier sage ich, dass das Programm beendet wird.
            print("Programm wird beendet.")
            # Hier stoppe ich die while-Schleife.
            break

        # Hier pruefe ich, ob der Benutzer 6 eingegeben hat.
        elif auswahl == "6":
            # Hier wird die Statistik angezeigt.
            statistik_anzeigen()

        # Aufgabe 8: Wenn etwas anderes eingegeben wurde, ist es falsch.
        else:
            # Hier sage ich, dass die Eingabe ungueltig ist.
            print("Ungueltige Eingabe.")


# Hier pruefe ich, ob diese Datei direkt gestartet wird.
if __name__ == "__main__":
    # Hier starte ich das Hauptprogramm.
    main()
