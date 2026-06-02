# Aufgabe 7: Ticketaufnahme in das Menü einbauen
# Wenn der Benutzer die 1 auswählt, soll das Programm folgende Daten abfragen:
# Benutzername, Abteilung, Problem, Priorität
# Danach soll das Programm die Ticketübersicht anzeigen und die Priorität bewerten.

# Aufgabe 8: Kleine Systemadmin-Meldungen einbauen
# Menüpunkt 2 und Menüpunkt 3 bekommen einfache Meldungen.
# Echte Systembefehle kommen später.

# Abschlussaufgabe: Fertiges Tag-1-Tool
# Das Programm hat ein Menü mit mindestens vier Punkten.
# Das Menü läuft in einer while-Schleife.
# Der Benutzer kann ein neues Ticket aufnehmen.
# Das Programm nutzt Variablen, input(), if, elif und else.
# Das Programm kann sauber beendet werden.


print("Willkommen im IT-Support-Tool")
print("Dieses Programm hilft bei einfachen Support-Aufgaben.")


while True:
    print()
    print("Menü")
    print("1 - Neues Ticket aufnehmen")
    print("2 - Systemstatus anzeigen")
    print("3 - Benutzer prüfen")
    print("4 - Programm beenden")

    auswahl = input("Bitte Auswahl eingeben: ")

    # Aufgabe 7: Ticketaufnahme
    if auswahl == "1":
        print("Neues Ticket aufnehmen")

        benutzer = input("Benutzername eingeben: ")
        abteilung = input("Abteilung eingeben: ")
        problem = input("Problem eingeben: ")
        prioritaet = input("Priorität eingeben (hoch/mittel/niedrig): ")

        print()
        print("Ticket wurde aufgenommen")
        print("Ticketnummer: 1001")
        print("Benutzer:", benutzer)
        print("Abteilung:", abteilung)
        print("Problem:", problem)
        print("Priorität:", prioritaet)

        if prioritaet == "hoch":
            print("Dieses Ticket muss sofort bearbeitet werden.")
        elif prioritaet == "mittel":
            print("Dieses Ticket sollte heute bearbeitet werden.")
        elif prioritaet == "niedrig":
            print("Dieses Ticket kann später bearbeitet werden.")
        else:
            print("Unbekannte Priorität. Bitte hoch, mittel oder niedrig verwenden.")

    # Aufgabe 8: Systemstatus
    elif auswahl == "2":
        print("Systemstatus")
        print("CPU: Prüfung folgt an Tag 3")
        print("Speicher: Prüfung folgt an Tag 3")
        print("Festplatte: Prüfung folgt an Tag 3")

    # Aufgabe 8: Benutzerprüfung
    elif auswahl == "3":
        username = input("Welcher Benutzer soll geprüft werden? ")
        print("Benutzerprüfung für:", username)
        print("Hinweis: Echte Benutzerprüfung folgt später mit Modulen und Systembefehlen.")

    # Abschlussaufgabe: Programm sauber beenden
    elif auswahl == "4":
        print("Programm wird beendet.")
        break

    # Abschlussaufgabe: ungültige Auswahl behandeln
    else:
        print("Ungültige Auswahl. Bitte 1, 2, 3 oder 4 eingeben.")