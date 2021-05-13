# Write a program to demonstrate Is-a Realtionship & Has-a Relationship between the classes
from Showroom import Bike


class Parent:
    name = 'Alok'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print('Pure Vegitarian, Having Rice-Sambhar')


class child(Parent):
    def __init__(self, name, age, bike):
        super().__init__(name, age)  # is-a-relationship---->constructor
        self.bike = bike

    def job(self):  # specialized-method
        print('Developer')
        self.bike.get_bike_info()

    def eat(self):  # overriden method
        print('Pure Non-Veg ,Having Chicken Tandoori')


b = Bike('Yamaha', '400cc', 'Black', 200000)
c = child('shikha', 23, b)
print('Name of the Father is:', Parent.name)
print('Name of the child is:', c.name)
c.job()
c.eat()
