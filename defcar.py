import time
import random
Botcars = ["bmw","audi","Lamborghini","Ferrari"]
garageplace = 2
class car:
    def __init__(self,brand,color,maxspeed,brokenchance):
        self.brand = brand
        self.color = color
        self.maxspeed = maxspeed
        self.brokenchance = brokenchance
        self.filup = 0
        self.warmup = False
        self.carrun = False
        self.carstop = False
        self.exitt = False
        self.broken = False
        self.garagee = False 
    def garage(self):    
        if garageplace >= 1 and self.garagee == False:
            print(f"Your car {self.brand} is going in the Garage...")
            self.carrun = False
            self.warmup = False
            self.carstop = True
            timee = random.randint(3,6)
            time.sleep(timee)
            garageplace -= 1
            print(f"The car {self.brand} is in the garage the are {garageplace} left ")
            time.sleep(3)
            print(f"The car {self.brand} is now stopped")
        elif garageplace < 1 and self.garagee == False:
            print("The garage are full")
        elif self.garagee == True:
            x = input("do you want do exet the garage? y for yes or n for no: ")
            if x == "y":
                print(f"Your car {self.brand} is exitting the garage...")
                timee = random.randint(3,6)
                time.sleep(timee)
                print(f"Yoir car{self.brand} is now out")
            elif x == "x":
                print(f"You are going back to the car {self.brand} menu")
        return self
                
    def repair(self):
        if self.broken == True:
            print(f"The car {self.brand} is repair and will take a while...")
            time.sleep(5)
            print(f"THe car {self.brand} is repair you need to warmup the car again")
            self.broken = False
            return self
        if self.broken == False:
            print(f"The car {self.brand} is not broken")
            return self
    
    def fillup(self):
        if self.filup <= 400 and self.broken == False and self.garagee == False:
            print(f"The car {self.brand} is filling up. Please wait a moment.")
            time.sleep(5)
            self.filup += 400
            print(f"The car {self.brand} is filled to {self.filup}. The limit is 400.")
        elif self.filup >= 350 and self.garagee == False:
           print(f"The car {self.brand} is already filled to {self.filup}. The maximum amount is 400. You can warm up the car.")
        elif self.broken == True:
            print(f"The car {self.brand} is broken you need to repair")
        elif self.garagee == True:
            print(f"Your car {self.brand} id in the garage. use garage to go out")
        return self
    
    def warm(self):
        if self.warmup == False and self.carrun == False and self.filup >= 200 and self.broken == False and self.garagee == False:
            print(f"The car {self.brand} needs to warm up. This will take a while.")
            x = random.randint(5, 10)
            time.sleep(x)
            self.warmup = True
            self.carstop = False
            self.filup -= 200
            print(f"The car {self.brand} has warmed up.")
        elif self.warmup == True:
            print(f"The car {self.brand} has already warmed up.")
        elif self.broken == True:
            print(f"The car {self.brand} is broken Pleas repair")
        elif self.filup <= 200 and self.garagee == False:
            print(f"The car {self.brand} is filled to only {self.filup}. It needs to be at least 200.")
        elif self.garagee == True:
            print(f"The car {self.brand} is in the garage. use garage to go out")
        return self
    
    def run(self):
        if self.garagee == True:
            print(f"Your car {self.brand} is in the garage. use garage to go out")
        elif self.warmup == True and self.carrun == False and self.filup >= 200 and self.broken == False:
            print(f"The car {self.brand} has started and it will take a while to reach maximum speed.")
            x = random.randint(10, 30)
            time.sleep(x)
            print(f"The car {self.brand} is now at its maximum speed of {self.maxspeed}.")
            self.warmup = False            
            self.carrun = True
            self.filup -= 200
            if random.randint(1,100) <= self.brokenchance:
                print(f"The car {self.brand} is broken. use repair to repair the car")
                print(f"The car is stopping...")
                time.sleep(3)
                self.carrun = False
                self.warmup = False
                self.broken = True
        elif self.broken == True :
            print(f"The car {self.brand} is broke. use repair")
        elif self.filup == 0 :
            print(f"You need to fill the car {self.brand} to 200. It is currently at {self.filup}.")
        elif self.carrun == True:
            print(f"The car {self.brand} is already running.")
        else:
            print(f"The car {self.brand} needs to warm up first. Please use the warmup function.")
        return self
    
    def race(self):
        if self.carrun == False and self.filup >= 400:
            print(f"Your car {self.brand} is now warmup for the race...")
            time.sleep(3)
            self.warmup = True
            if self.warmup == True and self.carrun ==  False:
                bot = random.randint(-30,30)
                player = random.randint(-30,30)
                bot = self.maxspeed + bot
                player = self.maxspeed + player
                racecar = random.choice(Botcars)
                print(f"The race has startet Your car is {self.brand} agains your opponent car is {racecar}")
                print(f"The cars are now speding up...")
                time.sleep(5)
                print(f"Your {self.brand} is at {player}Km/h and The opponent {racecar} is at {bot}Km/h")
                print("The game has endet")
                if player > bot:
                    print(f"Your {self.brand} has won again the opponent {racecar}")
                elif player < bot:
                    print(f"Your opponent {racecar} has won again your {self.brand} more luck next time")
                elif player == bot:
                    print("It was a draw The cars were at the same time in the end")
        elif self.carrun == True:
            print(f"Your {self.brand} is running pleas stop the car to begann a race")
        elif self.filup < 200 :
            print(f"Your {self.brand} has {self.filup} filed up but it need 200 to start The race")
            
        
        
    def stop(self):
        if self.carrun == True:
            print(f"The car {self.brand} is now stopping. This will take some time.")
            x = random.randint(3, 7)
            time.sleep(x)
            print(f"The car {self.brand} has stopped.")
            self.carrun = False
            self.warmup = False
            self.carstop = True
        elif self.carstop == True:
            print(f"The car {self.brand} has already stopped.")
        else:
            print(f"The car {self.brand} needs to be started first.")
        return self
        
    def exet(self):
        if self.carrun == False:
            self.exitt = True
            self.carrun = False
            self.warmup = False
            self.carstop = False
            print(f"You are exiting the car {self.brand}...")
            print("Returning to the main menu...")
            time.sleep(3)
            return self
        else:
            print(f"The car {self.brand} is still running. Please stop the car first.")
            self.exitt = False
            return self
    """        
    def first(x):
    while True:
        try:
            x = int(input("\nWhich car do you want\n1.Audi\n2.Bmw\n3.Lambo\n4.Ferrari: "))
        except ValueError:
                print("ValueError: Please enter numbers only, no letters!")
                    
    def second(y):
    while True:
        try:
            y = int(input("\nGive the Condition of the car Audi\n1.warmup\n2.run the car\n3.stop\n4.Take a difirent car"))
        except ValueError:
            print("ValueError: Please enter numbers only, no letters!")
    """
