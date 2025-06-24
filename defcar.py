import time
import random

class car:
    def __init__(self,brand,color,maxspeed):
        self.brand = brand
        self.color = color
        self.maxspeed = maxspeed
        self.warmup = False
        self.carrun = False
        self.carstop = False
        self.exitt = False
            
    def warm(self):
        if self.warmup == False and self.carrun == False:
            print(f"The car {self.brand} need to warmup it will take a while,")
            x = random.randint(5,10)
            time.sleep(x)
            self.warmup = True
            print(f"The car {self.brand} has warmed up")
            return self
        else:
            print(f"The car {self.brand} has already warmed up ")
            return self
    
    def run(self):
        if self.warmup == True and self.carrun == False:
            print(f"The car {self.brand} is started and it will take a while to go to maxspeed")
            x = random.randint(10,30)
            time.sleep(x)
            print(f"The car {self.brand} are on the max car speed of {self.maxspeed}")
            self.warmup = False
            self.carrun = True
            return self
        if self.carrun == True:
            print(F"The car {self.brand} ist alreade running")
            return self
        else:
            print(f"The car {self.brand} has to warm up please use warmup")
            return self
        
    def stop(self):
        if self.carrun == True:
            print(f"The car {self.brand} is now stopping and will take some time")
            x = random.randint(3,7)
            time.sleep(x)
            print(f"The car {self.brand} has stopped")
            self.carrun = False
            self.warmup = False
            self.carstop = True
            return self
        else:
            print(f"The car {self.brand} has to start")
            return self
    
    def exet(self):
        if self.carrun == False:
            self.exitt = True
            self.carrun = False
            self.warmup = False
            self.carstop = False
            print(f"You are exitting the Car {self.brand} ...")
            print("Going back to the main menu...")
            time.sleep(3)
            return self
        else:
            print(f"The car {self.brand} is running please use stop to stop the car")
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