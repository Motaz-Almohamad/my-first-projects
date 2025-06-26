import time
import random

class car:
    def __init__(self,brand,color,maxspeed):
        self.brand = brand
        self.color = color
        self.maxspeed = maxspeed
        self.filup = 0
        self.warmup = False
        self.carrun = False
        self.carstop = False
        self.exitt = False
    
    def fillup(self):
        if self.filup <= 400:
            print(f"The car {self.brand} is filling up. Please wait a moment.")
            time.sleep(5)
            self.filup += 200
            print(f"The car {self.brand} is filled to {self.filup}. The limit is 400.")
            return self
        elif self.filup >= 350:
           print(f"The car {self.brand} is already filled to {self.filup}. The maximum amount is 400. You can warm up the car.")

    def warm(self):
        if self.warmup == False and self.carrun == False and self.filup >= 200:
            print(f"The car {self.brand} needs to warm up. This will take a while.")
            x = random.randint(5, 10)
            time.sleep(x)
            self.warmup = True
            self.filup -= 200
            print(f"The car {self.brand} has warmed up.")
            return self
        elif self.warmup == True:
            print(f"The car {self.brand} has already warmed up.")
            return self
        elif self.filup <= 200:
            print(f"The car {self.brand} is filled to only {self.filup}. It needs to be at least 200.")
    
    def run(self):
        if self.warmup == True and self.carrun == False and self.filup >= 200:
            print(f"The car {self.brand} has started and it will take a while to reach maximum speed.")
            x = random.randint(10, 30)
            time.sleep(x)
            print(f"The car {self.brand} is now at its maximum speed of {self.maxspeed}.")
            self.warmup = False            
            self.carrun = True
            self.filup -= 200
            return self
        elif self.filup == 0:
            print(f"You need to fill the car {self.brand} to 200. It is currently at {self.filup}.")
            return self
        elif self.carrun == True:
            print(f"The car {self.brand} is already running.")
            return self
        else:
            print(f"The car {self.brand} needs to warm up first. Please use the warmup function.")
            return self
        
    def stop(self):
        if self.carrun == True:
            print(f"The car {self.brand} is now stopping. This will take some time.")
            x = random.randint(3, 7)
            time.sleep(x)
            print(f"The car {self.brand} has stopped.")
            self.carrun = False
            self.warmup = False
            self.carstop = True
            return self
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