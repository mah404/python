from pathlib import Path  # import path to work with folders and files
from datetime import datetime  # import datetime to show date and time
import subprocess  # import subprocess to run a small system command


# 2. aufgabe 1: grundgeruest und menue
def show_menu():  # this function prints the menu
    print()  # print an empty line
    print("Systemcheck Tool")  # print the program name
    print("1 Aktuelles Verzeichnis anzeigen")  # print option one
    print("2 Ordner analysieren")  # print option two
    print("3 Systembefehl ausfuehren")  # print option three
    print("4 Systemreport speichern")  # print option four
    print("5 Programm beenden")  # print option five


# 3. aufgabe 2: aktuelles verzeichnis und datum anzeigen
def show_current_folder():  # this function shows folder and time
    zeitpunkt = datetime.now()  # save the current date and time
    print("Aktuelles Verzeichnis:", Path.cwd())  # show the current folder
    print("Zeitpunkt:", zeitpunkt)  # show date and time


# 4. aufgabe 3: ordner analysieren
def analyse_folder():  # this function checks a folder
    pfad_text = input("Ordnerpfad eingeben: ")  # ask the user for a folder path
    pfad = Path(pfad_text)  # make a path object from the text

    try:  # start error handling for the folder check
        print("Pfad existiert:", pfad.exists())  # show if the path exists
        print("Ist ein Ordner:", pfad.is_dir())  # show if the path is a folder

        if pfad.exists() and pfad.is_dir():  # check the folder like in the example
            print("Ordner gefunden")  # tell the user the folder was found

            dateien = 0  # start the file counter
            ordner = 0  # start the folder counter
            txt_dateien = []  # make an empty list for txt files

            for element in pfad.iterdir():  # go through every item in the folder
                if element.is_file():  # check if the item is a file
                    dateien = dateien + 1  # add one to the file counter
                    if element.suffix == ".txt":  # check if the file ends with .txt
                        txt_dateien.append(element.name)  # save the txt file name
                elif element.is_dir():  # check if the item is a folder
                    ordner = ordner + 1  # add one to the folder counter

            print("Dateien:", dateien)  # show how many files are inside
            print("Unterordner:", ordner)  # show how many folders are inside
            print("Txt Dateien:")  # print a heading for txt files

            if len(txt_dateien) == 0:  # check if no txt file was found
                print("Keine txt Dateien gefunden")  # tell the user no txt files were found
            else:  # run this part when txt files were found
                for datei_name in txt_dateien:  # go through every txt file name
                    print(datei_name)  # print the txt file name
        else:  # run this part when the folder was not found
            print("Ordner nicht gefunden")  # tell the user the folder was not found

    except Exception as error:  # catch unexpected folder errors
        print("Es ist ein Fehler aufgetreten:", error)  # show the error without crashing


# 5. aufgabe 4: systembefehl ausfuehren
def run_system_command():  # this function runs one safe command
    try:  # start error handling for the command
        result = subprocess.run(["whoami"], capture_output=True, text=True)  # run the whoami command
        print("Ergebnis des Befehls whoami:")  # print a small heading
        print(result.stdout)  # print the command output
    except Exception as error:  # catch command errors
        print("Es ist ein Fehler aufgetreten:", error)  # show the error without crashing


# 6. aufgabe 5: systemreport speichern
def create_report():  # this function writes the report file
    try:  # start error handling for the report
        zeitpunkt = datetime.now()  # save the current date and time
        result = subprocess.run(["whoami"], capture_output=True, text=True)  # run the whoami command

        with open("system_report.txt", "w", encoding="utf-8") as file:  # open the report file for writing
            file.write("Systemreport\n")  # write the report title
            file.write("Datum und Uhrzeit: " + str(zeitpunkt) + "\n")  # write date and time
            file.write("Aktuelles Verzeichnis: " + str(Path.cwd()) + "\n")  # write the current folder
            file.write("Ergebnis von whoami: " + result.stdout.strip() + "\n")  # write the command result
            file.write("Der Report wurde erfolgreich erstellt.\n")  # write the final message

        print("Report wurde gespeichert")  # tell the user the report is saved
    except Exception as error:  # catch report errors
        print("Es ist ein Fehler aufgetreten:", error)  # show the error without crashing


print("Willkommen beim Systemcheck Tool")  # greet the user

# 2. aufgabe 1: while schleife fuer das menue
while True:  # keep the menu running
    show_menu()  # show the menu
    choice = input("Auswahl eingeben: ")  # ask the user for a choice

    if choice == "1":  # check if the user picked option one
        show_current_folder()  # show the current folder and time
    elif choice == "2":  # check if the user picked option two
        analyse_folder()  # analyse a folder
    elif choice == "3":  # check if the user picked option three
        run_system_command()  # run the system command
    elif choice == "4":  # check if the user picked option four
        create_report()  # create the report file
    elif choice == "5":  # check if the user picked option five
        print("Programm wird beendet")  # print the goodbye message
        break  # stop the while loop
    else:  # run this when the choice is wrong
        print("Ungueltige Auswahl")  # tell the user the choice is not valid
