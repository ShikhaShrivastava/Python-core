'''class Employee:
    def __init__(self,name):
        self.name=name

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __init__(self,name,age,city):
        self.name=name
        self.age=age
        self.city=city

if __name__=='__main__':
    #e=Employee('sachin')--> TypeError: __init__() missing 2 required positional arguments: 'age' and 'city'

#Constructor overloading and method overloading is not possible in python
    e=Employee('shikha',45,'Banglore')
    print(e.name)
    print(e.age)
    print(e.city)'''

'''#**********Constructor Overloading using Default Argument***********
class Employee:
    def __init__(self,name=None,age=None,city=None):
        print('****Constructor Overloading using Default Argument****')
        self.name=name
        self.age=age
        self.city=city

if __name__=='__main__':
    e=Employee()
    e=Employee('shikha')
    e=Employee('shikha',45)
    e=Employee('shikha',45,'Banglore')
    print(e.name)
    print(e.age)
    print(e.city)'''


# *******Constructor Overloading using Variable Length Argument*****
class Employee:
    def __init__(self, *info):
        print('****Constructor Overloading using Variable Length Argument****')
        self.info = info


if __name__ == '__main__':
    e = Employee()
    e = Employee('shikha')
    e = Employee('shikha', 45)
    e = Employee('shikha', 45, 'Banglore')
    for emp_info in e.info:
        print(emp_info)

