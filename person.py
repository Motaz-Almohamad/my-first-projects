personen = []

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
            name = input("Gib den namen der person: ")
            nachname = input("Gib den nachname des person: ")
            alter = input("Gib den alter einer person: ")
            beruf = input("Gib den Beruf Des person: ")
            personen.append({
                'name' : name,
                'nachname' : nachname,
                'alter' : alter,
                'beruf' : beruf,
            })
            print("Person erfolgreich hinzugefügt.")
        case 2:
            print("***************************************************************")
            print(f"{'#':<3}{'Name':<15}{'Nachname':<15}{'Alter':<15}{'Beruf':<15}")
            nummer = 0
            for person in personen :
                print(f"{nummer:<3}{person['name']:<15}{person['nachname']:<15}{person['alter']:<15}{person['beruf']:<15}")
                nummer = nummer + 1
        case 3:
            try:
                suche = int(input("Du hast person suchen genommen.\n Wähl nach was du suchen willst:\n0.Züruck\n1.Name\n2.Nachname\n3.Alter\n4.Beruf\nYour nummber: ")) 
            except ValueError:
                print("Ungültige Eingabe. Bitte gib eine Zahl ein.")
                continue
            match suche :
                case 0:
                        print("es werd züruck gegangen")
                case 1:
                    gefunden = False
                    nummer = 0
                    gesucht = input("Gib die person name die du suchts: ")
                    print("***************************************************************")
                    print(f"{'#':<3}{'Name':<15}{'Nachname':<15}{'Alter':<15}{'Beruf':<15}")
                    for person in personen:
                        if gesucht == person['name']:
                            print(f"{nummer:<3}{person['name']:<15}{person['nachname']:<15}{person['alter']:<15}{person['beruf']:<15}")
                            gefunden = True
                        nummer += 1
                    if not gefunden:
                        print(f"Niemand mit dem Namen {gesucht} gefunden")   
                case 2:
                    gefunden = False
                    gesucht = input("Gib die person Nachname die du suchts: ")
                    print("***************************************************************")
                    print(f"{'#':<3}{'Name':<15}{'Nachname':<15}{'Alter':<15}{'Beruf':<15}")
                    nummer = 0
                    for person in personen:
                        if gesucht == person['nachname']:
                            print(f"{nummer:<3}{person['name']:<15}{person['nachname']:<15}{person['alter']:<15}{person['beruf']:<15}")
                            gefunden = True
                        nummer += 1
                    if not gefunden:
                        print(f"Niemand mit dem Nachname {gesucht} gefunden")
                case 3:
                    gefunden = False
                    gesucht = input("Gib die person Alter die du suchts: ")
                    print("***************************************************************")
                    print(f"{'#':<3}{'Name':<15}{'Nachname':<15}{'Alter':<15}{'Beruf':<15}")
                    nummer = 0
                    for person in personen:
                        if gesucht == person['alter']:
                            print(f"{nummer:<3}{person['name']:<15}{person['nachname']:<15}{person['alter']:<15}{person['beruf']:<15}")
                            gefunden = True
                        nummer += 1
                    if not gefunden:
                        print(f"Niemand mit dem Alter {gesucht} gefunden")
                case 4:
                    gefunden = False
                    gesucht = input("Gib die person Beruf die du suchts: ")
                    print("***************************************************************")
                    print(f"{'#':<3}{'Name':<15}{'Nachname':<15}{'Alter':<15}{'Beruf':<15}")
                    nummer = 0
                    for person in personen:
                        if gesucht == person['beruf']:
                            print(f"{nummer:<3}{person['name']:<15}{person['nachname']:<15}{person['alter']:<15}{person['beruf']:<15}")
                            gefunden = True
                        nummer += 1
                    if not gefunden:
                        print(f"Niemand mit dem Beruf {gesucht} gefunden")
                case _:
                    print("Gib bitte ein zahl zwischen 1 und 4.")
        case 4:
            gesucht = input("Gib die person name die du löschen willst: ")
            nachnamee = input("Gib den nachname auch: ")
            for person in personen :
                if gesucht == person['name'] and nachnamee == person['nachname']:
                    personen.remove(person)
                    
        case _:
            print("Gib bitte ein zahl zwichen 1 und 4.")