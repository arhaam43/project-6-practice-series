# 3. Public Variables and Methods
# Assignment:
# Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.

class Car:
    #public variable
    brand = "Mercedes"
    def start(self):
        print(f"{self.brand} has been begining...")

#object of car
my_car = Car()

""" To Call the start method
my_car.start() """

#accessing public variable
print(my_car.brand)         #output: Mercedes