# ***********************Abstract Method********************************
# Demo-1
'''from abc import *
class Demo:
    @abstractmethod
    def m1(self):
        pass'''

# Demo-2
'''from abc import *
class Fruit:
    @abstractmethod
    def taste(self):
        pass

    def healthy(self):
        print('Every Fruit is good for health')

if __name__=='__main__':
    f=Fruit()
    f.healthy()
    f.taste() #abstract method'''

# ***********************Abstract Class*******************************

# ex-1

'''from abc import *
class Demo:
    pass

if __name__=='__main__':
    Demo()'''

# ex-2
'''from abc import *
class Demo(ABC):
    pass

if __name__=='__main__':
    Demo()'''

# ex-3
'''from abc import *
#class Demo(ABC):
class Demo():

    @abstractmethod
    def m1(self):
        pass

if __name__=='__main__':
    d=Demo()
    d.m1()'''

# ex-5
'''from abc import *
#class Demo(ABC):
class Demo():

    @abstractmethod
    def m1(self):
        print('Hey i am abstract method') #implementation in abstract is allowed

if __name__=='__main__':
    d=Demo()
    d.m1()'''

# ex-6
'''from abc import *
class Fruit(ABC):

    @abstractmethod
    def taste(self):
        pass

class Mango(Fruit):
    pass'''

# ex-7
'''
from abc import *
class Fruit(ABC):

    @abstractmethod
    def taste(self):
        pass

class Mango(Fruit):
    pass
if __name__=='__main__':
    Mango()
'''
# ex-8
from abc import *


class Vehicle(ABC):

    @abstractmethod
    def no_of_wheels(self):
        pass

    def d1(self):
        print('To drive a vehicle d1 is require')  # converting Am to Im


class Bike(Vehicle):
    def no_of_wheels(self):
        return 'The no. of wheels is :2'


class Car(Vehicle):
    def no_of_wheels(self):
        return 'The no. of wheels is :4'


if __name__ == '__main__':
    b = Bike()
    print(b.no_of_wheels())
    b.d1()

    c = Car()
    print(c.no_of_wheels())
    c.d1()

# ex-10
'''from abc import *
class Animal(ABC):

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def sleep(self):
        pass

    def breathe(self):
        print('In order to survive all animal brethe in air')

class Lion(Animal):
    def eat(self):
        print('Lion eat flesh of other animal')

    def sleep(self):
        print('sleep everytime')

if __name__=='__main__':
    simba=Lion()
    simba.eat()
    #simba.sleep()
    simba.breathe()'''

# **************************(Build in Function)**************************
'''class parent:
    def m1(self):
        pass
class child(parent):
    def m1(self):
        print('child class method')

if __name__=='__main__':
    c=child()
    print(issubclass(child,parent))
    print(isinstance(child,parent))
    print(isinstance(c,child))'''

# ************************Concrete Class****************************
'''from abc import ABC,abstractmethod

class Polygon(ABC):
    def no_of_sides(self):
        pass
class Triangle(Polygon):
    def no_of_sides(self):
        print('Three sided Figure')

class Hexagon(Polygon):
    def no_of_sides(self):
        print('Six sided Figure')

if __name__=='__main__':
    Polygon()
    t=Triangle()
    t.no_of_sides()
    h=Hexagon()
    h.no_of_sides()'''


