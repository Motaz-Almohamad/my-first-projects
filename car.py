import time
import random

class auto:
    def __init__(self,brand,color,maxspeed):
        self.brand = brand
        self.color = color
        self.maxspeed = maxspeed
        self.warmup = False
        self.carrun = False
        self.carstop = False
            
    def warm(self):
        if self.warmup == True:
            print(f"The car {self.brand} has already warmed up ")
            return self
        else:
            print(f"The car {self.brand} need to warmup it will take a while,")
            x = random.randint(5,10)
            time.sleep(x)
            self.warmup = True
            print(f"The car {self.brand} has warmed up")
            return self
    
    def run(self):
        if self.warmup == True:
            print(f"The car {self.brand} is started and it will take a while to go to maxspeed")
            x = random.randint(10,30)
            time.sleep(x)
            print(f"The car {self.brand} are on the max car speed of {self.maxspeed}")
            self.carrun = True
            return self
        else:
            print(f"The car {self.brand} has to warm up please use warm")
            return self
        
    def stop(self):
        if self.carrun == True:
            print(f"The car {self.brand} is now stopping and will take some time")
            x = random.randint(3,7)
            time.sleep(x)
            print(f"The car {self.brand} has stopped")
            self.carstop = True
            return self
        else:
            print(f"The car {self.brand} has to start")
            return self


audi = auto(brand= "Audi" ,color= "Blue",maxspeed= 150)
print(audi.brand,audi.color,audi.maxspeed) 
audi.warm().run().stop()

