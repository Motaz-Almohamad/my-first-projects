import time
from defcar import car
empty = car(brand= "nothing" ,color= "nothing" , maxspeed= "nothing" ,brokenchance= "nothing")
audi = car(brand= "Audi" ,color= "Blue",maxspeed= 250 ,brokenchance= 15)
bmw = car(brand= "Bmw", color= "Black" , maxspeed= 300, brokenchance= 20)
lambo = car(brand= "Lamborghini" ,color="Green", maxspeed= 350, brokenchance= 30)
ferrari = car(brand= "Ferrari",color= "Yellow", maxspeed= 400, brokenchance= 25)
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
                    y = int(input(f"\nGive the Condition of the car {choice.brand}\n1.garage\n2.repair\n3.fillup\n4.warmup\n5.run the car\n6.Join a race\n7.stop\n8.Take a difirent car\nYour choic: "))
                except ValueError:
                    print("ValueError: Please enter numbers only, no letters!")
                    continue
                match y:
                    case 1:
                        choice.garage()
                        time.sleep(3)
                    case 2:
                        choice.repair()
                        time.sleep(3)
                    case 3:
                        choice.fillup()
                        time.sleep(3)
                    case 4:
                        choice.warm()
                        time.sleep(3)
                    case 5:
                        choice.run()
                        time.sleep(3)
                    case 6:
                        choice.race()
                        time.sleep(3)
                    case 7:
                        choice.stop()
                        time.sleep(3)
                    case 8:
                        choice.exet()
                        if choice.exitt == True:
                            break
                        elif choice.exitt == False:
                            continue
    else:
        continue