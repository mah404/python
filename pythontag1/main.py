print("Willkommen im IT-Support-Tool") 
print("Dieses Programm hilft bei einfachen Support-Aufgaben.") 
print("Python Tag 1") 
ticket_nummer = 1001 
benutzer = input("Benutzername eingeben: ") 
abteilung = input("Abteilung eingeben: ") 
problem = input("Problem eingeben: ") 
prioritaet = input("Priorität eingeben (hoch/mittel/niedrig): ") 

if prioritaet == "hoch": 
    print("Dieses Ticket muss sofort bearbeitet werden.") 
elif prioritaet == "mittel": 
    print("Dieses Ticket sollte heute bearbeitet werden.") 
elif prioritaet == "niedrig": 
    print("Dieses Ticket kann später bearbeitet werden.") 
else: 
    print("Unbekannte Priorität. Bitte hoch, mittel oder niedrig verwenden.") 
    
print("Ticketnummer:", ticket_nummer) 
print("Benutzer:", benutzer) 
print("Abteilung:", abteilung) 
print("Problem:", problem) 
print("Priorität:", prioritaet) 