from defcar import car

empty = car(brand= "nothing" ,color= "nothing" , maxspeed= "nothing" ,brokenchance= "nothing")
audi = car(brand= "Audi" ,color= "Blue",maxspeed= 250 ,brokenchance= 100)
bmw = car(brand= "Bmw", color= "Black" , maxspeed= 300, brokenchance= 50)
lambo = car(brand= "Lamborghini" ,color="Green", maxspeed= 350, brokenchance= 30)
ferrari = car(brand= "Ferrari",color= "Yellow", maxspeed= 400, brokenchance= 10)

audi.fillup().fillup().warm().run()
bmw.fillup().fillup().warm().run()
lambo.fillup().fillup().warm().run()
ferrari.fillup().fillup().warm().run()
