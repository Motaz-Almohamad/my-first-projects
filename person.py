import json
personen = []
from  defpersonen import add ,show,search,delet
with open('pers.json') as pers_file:
        personen = json.load(pers_file)
while 1 :
    try:
        p = int(input("\n0.Code stoppen\n1.Person Hinzufügen\n2.Person Anzeigen\n3.Person suchen\n4.Person Löschen\nYour nummber: "))
    except ValueError:
        print("Ungültige Eingabe. Bitte gib eine Zahl ein.")
        continue
    match p :
        
        case 0:
            print("Exit...")
            break
        
        case 1:
            add(personen)
            with open("pers.json","w") as f:
                json.dump(personen , f)
        case 2:
           show(personen)
        case 3:
            search(personen)
        case 4:
            delet(personen)
            with open("pers.json","w") as f:
                json.dump(personen , f)
        case _:
            print("Gib bitte ein zahl zwichen 1 und 4.")