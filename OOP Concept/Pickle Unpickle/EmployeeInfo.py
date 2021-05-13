import pickle
class Employee:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

    def display(self):
        print('Name:',self.name)
        print('Age:',self.age)
        print('Marks:',self.salary)
