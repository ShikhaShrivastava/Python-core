class Dog:
    def sound(self):
        print('Bow Bow')


class Cat:
    def sound(self):
        print('Meau Meau')


class Duck:
    def sound(self):
        print('Quack Quack')


def call_Instance_method(objref):
    objref.sound()


animal = [Dog(), Cat(), Duck()]
for objref in animal:
    call_Instance_method(objref)

# Note: If we use different method name it will show Attribute Error--->
# To overcome-->use hasattr()

print()


class Dog:
    def barks(self):
        print('Bow Bow')


class Cat:
    def talk(self):
        print('Meau Meau')


class Duck:
    def sound(self):
        print('Quack Quack')


def call_Instance_method(objref):
    if hasattr(objref, 'barks'):
        objref.barks()
    elif hasattr(objref, 'talk'):
        objref.talk()
    else:
        objref.sound()


animal = [Dog(), Cat(), Duck()]
for objref in animal:
    call_Instance_method(objref)



