import car
from defcar import car
#audi: car = car(brand= "Audi" ,color= "Blue",maxspeed= 250)
audi = car(brand= "Audi" ,color= "Blue",maxspeed= 250)
bmw = car(brand= "Bmw", color= "Black" , maxspeed= 300)
lambo = car(brand= "Lamborghini" ,color="Green", maxspeed= 350)
ferrari = car(brand= "Ferrari",color= "Yellow", maxspeed= 400)
"""
while True:
    first(x)
    match x:
        case 1 :
            second(y)
            match y:
                case 1:
                    audi.warm()
                case 2:
                    audi.run()
                case 3:
                    audi.stop()
                case 4:
                    print("Going back to the Main menu")
"""
while True:
    try:
        x = int(input("\nWhich car do you want\n0.Exiting the code\n1.Audi\n2.Bmw\n3.Lambo\n4.Ferrari\nYour choic: "))
    except ValueError:
        print("ValueError: Please enter numbers only, no letters!")
        continue
    match x:
        case 0 : 
            print("Exiting the code...")
            break
        case 1 :
            while True:
                try:
                    y = int(input("\nGive the Condition of the car Audi\n1.warmup\n2.run the car\n3.stop\n4.Take a difirent car\nYour choic: "))
                except ValueError:
                    print("ValueError: Please enter numbers only, no letters!")
                    continue
                match y:
                    case 1:
                        audi.warm()
                    case 2:
                        audi.run()
                    case 3:
                        audi.stop()
                    case 4:
                        audi.exet()
                        if audi.exitt == True:
                            exit
                        else:
                            continue

                    case _:
                        print("Pleas choic the nummbers betwin 1-4")
        case 2 :
            while True:
                try:
                    y = int(input("\nGive the Condition of the car Bmw\n1.warmup\n2.run the car\n3.stop\n4.Take a difirent car\nYour choic: "))
                except ValueError:
                    print("ValueError: Please enter numbers only, no letters!")
                    continue
                match y:
                    case 1:
                        bmw.warm()
                    case 2:
                        bmw.run()
                    case 3:
                        bmw.stop()
                    case 4:
                        bmw.exet()
                        if bmw.exitt == True:
                            exit
                        else:
                            continue
                    case _:
                        print("Pleas choic the nummbers betwin 1-4")
        case 3 :
            while True:
                try:
                    y = int(input("\nGive the Condition of the car Lamborghini\n1.warmup\n2.run the car\n3.stop\n4.Take a difirent car\nYour choic: "))
                except ValueError:
                    print("ValueError: Please enter numbers only, no letters!")
                    continue
                match y:
                    case 1:
                        lambo.warm()
                    case 2:
                        lambo.run()
                    case 3:
                        lambo.stop()
                    case 4:
                        lambo.exet()
                        if bmw.exitt == True:
                            exit
                        else:
                            continue
                    case _:
                        print("Pleas choic the nummbers betwin 1-4")
        case 4 :
            while True:
                try:
                    y = int(input("\nGive the Condition of the car Ferrari\n1.warmup\n2.run the car\n3.stop\n4.Take a difirent car\nYour choic: "))
                except ValueError:
                    print("ValueError: Please enter numbers only, no letters!")
                    continue
                match y:
                    case 1:
                        ferrari.warm()
                    case 2:
                        ferrari.run()
                    case 3:
                        ferrari.stop()
                    case 4:
                        ferrari.exet()
                        if ferrari.exitt == True:
                            exit
                        else:
                            continue
                    case _:
                        print("Pleas choic the nummbers betwin 1-4")