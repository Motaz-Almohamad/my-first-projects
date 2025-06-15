def add(personen_list):
    name = input("Gib den namen der person: ")
    nachname = input("Gib den nachname des person: ")
    alter = input("Gib den alter einer person: ")
    beruf = input("Gib den Beruf Des person: ")
    personen_list.append({
        'name' : name,
        'nachname' : nachname,
        'alter' : alter,
        'beruf' : beruf,
    })
    print("Person erfolgreich hinzugefügt.")

def show(showen):
    print("***************************************************************")
    print(f"{'#':<3}{'Name':<15}{'Nachname':<15}{'Alter':<15}{'Beruf':<15}")
    nummer = 0
    for person in showen :
        print(f"{nummer:<3}{person['name']:<15}{person['nachname']:<15}{person['alter']:<15}{person['beruf']:<15}")
        nummer = nummer + 1

def search(searching):
    while True: 
        while True :   
            try:
                suche = int(input("Du hast person suchen genommen.\n Wähl nach was du suchen willst:\n0.Züruck\n1.Name\n2.Nachname\n3.Alter\n4.Beruf\nYour nummber: ")) 
                break
            except ValueError:
                print("Ungültige Eingabe. Bitte gib eine Zahl ein.")
            
        match suche :
            case 0:
                print("es werd züruck gegangen")
                break
            case 1:
                gefunden = False
                nummer = 0
                gesucht = input("Gib die person name die du suchts: ")
                print("***************************************************************")
                print(f"{'#':<3}{'Name':<15}{'Nachname':<15}{'Alter':<15}{'Beruf':<15}")
                for person in searching:
                    if gesucht == person['name']:
                        print(f"{nummer:<3}{person['name']:<15}{person['nachname']:<15}{person['alter']:<15}{person['beruf']:<15}")
                        gefunden = True
                        nummer += 1
                if not gefunden:
                    print(f"Niemand mit dem Namen {gesucht} gefunden")   
                break
            case 2:
                gefunden = False
                gesucht = input("Gib die person Nachname die du suchts: ")
                print("***************************************************************")
                print(f"{'#':<3}{'Name':<15}{'Nachname':<15}{'Alter':<15}{'Beruf':<15}")
                nummer = 0
                for person in searching:
                    if gesucht == person['nachname']:
                        print(f"{nummer:<3}{person['name']:<15}{person['nachname']:<15}{person['alter']:<15}{person['beruf']:<15}")
                        gefunden = True
                        nummer += 1
                if not gefunden:
                    print(f"Niemand mit dem Nachname {gesucht} gefunden")
                break
            case 3:
                gefunden = False
                gesucht = input("Gib die person Alter die du suchts: ")
                print("***************************************************************")
                print(f"{'#':<3}{'Name':<15}{'Nachname':<15}{'Alter':<15}{'Beruf':<15}")
                nummer = 0
                for person in searching:
                    if gesucht == person['alter']:
                        print(f"{nummer:<3}{person['name']:<15}{person['nachname']:<15}{person['alter']:<15}{person['beruf']:<15}")
                        gefunden = True
                        nummer += 1
                if not gefunden:
                    print(f"Niemand mit dem Alter {gesucht} gefunden")
                break
            case 4:
                gefunden = False
                gesucht = input("Gib die person Beruf die du suchts: ")
                print("***************************************************************")
                print(f"{'#':<3}{'Name':<15}{'Nachname':<15}{'Alter':<15}{'Beruf':<15}")
                nummer = 0
                for person in searching:
                    if gesucht == person['beruf']:
                        print(f"{nummer:<3}{person['name']:<15}{person['nachname']:<15}{person['alter']:<15}{person['beruf']:<15}")
                        gefunden = True
                        nummer += 1
                if not gefunden:
                    print(f"Niemand mit dem Beruf {gesucht} gefunden")
                break
            case _:
                print("Gib bitte ein zahl zwischen 1 und 4.")
def delet(delett):
    gefunden = False
    gesucht = input("Gib die person name die du löschen willst: ")
    nachnamee = input("Gib den nachname auch: ")
    for person in delett :
        if gesucht == person['name'] and nachnamee == person['nachname']:
            delett.remove(person)
            print(f"{gesucht} {nachnamee} erfolgreich")
            gefunden = True
        if not gefunden :
            print (f"Niemand mit dem Namen {gesucht} {nachnamee} gefunden")
        