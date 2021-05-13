# Constructor overriding:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Employee(Person):
    def __init__(self, name, age, profession):
        super().__init__(name, age)
        self.profession = profession


e = Employee('shikha', 45, 'Banglore')
print(e.name)
print(e.age)
print(e.profession)


