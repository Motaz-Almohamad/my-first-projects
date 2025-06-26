from defcar import car
empty = car(brand= "nothing" ,color= "nothing" , maxspeed= "nothing")
audi = car(brand= "Audi" ,color= "Blue",maxspeed= 250)
bmw = car(brand= "Bmw", color= "Black" , maxspeed= 300)
lambo = car(brand= "Lamborghini" ,color="Green", maxspeed= 350)
ferrari = car(brand= "Ferrari",color= "Yellow", maxspeed= 400)
choice = empty

#if choice == empty:
#    choice = audi
#    print(choice.brand)
#    choice = empty
#    print(choice.brand)
while True:
    try:
        x = int(input("\nWhich car do you want\n0.Exiting the code\n1.Audi\n2.Bmw\n3.Lambo\n4.Ferrari\nYour choic: "))
    except ValueError:
        print("ValueError: Please enter numbers only, no letters!")
        continue
    match x:
        case 0:
            print("Exiting the code...")
            exit()
        case 1:
            choice = audi
        case 2:
            choice = bmw
        case 3: 
            choice = lambo
        case 4:
            choice = ferrari
        case _:
            print("Pleas choic the nummbers betwin 1-4")
    if 1 <= x <= 4:
        while True:
                try:
                    y = int(input(f"\nGive the Condition of the car {choice.brand}\n1.fillup\n2.warmup\n3.run the car\n4.stop\n5.Take a difirent car\nYour choic: "))
                except ValueError:
                    print("ValueError: Please enter numbers only, no letters!")
                    continue
                match y:
                    case 1:
                        choice.fillup()
                    case 2:
                        choice.warm()
                    case 3:
                        choice.run()
                    case 4:
                        choice.stop()
                    case 5:
                        choice.exet()
                        if choice.exitt == True:
                            break
                        elif choice.exitt == False:
                            continue
    else:
        continue