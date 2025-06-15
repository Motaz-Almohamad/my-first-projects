personen = []
from  defpersonen import add ,show,search,delet
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
        case 2:
           show(personen)
        case 3:
            search(personen)
        case 4:
            delet(personen)
        case _:
            print("Gib bitte ein zahl zwichen 1 und 4.")