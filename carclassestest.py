import json
from defcar import car

empty = car(brand= "nothing" ,color= "nothing" , maxspeed= "nothing")
audi = car(brand= "Audi" ,color= "Blue",maxspeed= 250)
bmw = car(brand= "Bmw", color= "Black" , maxspeed= 300)
lambo = car(brand= "Lamborghini" ,color="Green", maxspeed= 350)
ferrari = car(brand= "Ferrari",color= "Yellow", maxspeed= 400)
choice = empty
autos = [empty,audi.brand,bmw,lambo,ferrari]
print(autos)