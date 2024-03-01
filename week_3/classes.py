# used to model a real world object
# real objects hane parameters(attributes), funtions(actions)

#cars.py :c used as an example
#thsi is a class thats describes cars

class car:
        def __init__(self,model,make,year_of_production,fuel_capacity,color,horse_power):
                self.model = model
                self.make = make
                self.make = make
                self.year_of_production = year_of_production
                self.fuel_capacity = fuel_capacity
                self.horse_power = horse_power
                self.color = color

        def print_make(self,make):
                       print("the car is of {0} make".format(self.make)) 


        def set_make(self,make): 
                self.make = make

        def get_make(self):
                return self.make

my_car = car("impalla","chrevolet","1969","2500cc","lilac","3900")

my_car.set_make("Toyota")

print(my_car.get_make())
          