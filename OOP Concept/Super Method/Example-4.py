class Parent:
    def __init__(self):
        print('Parent class constructor')
    def imethod(self):
        print('Parent class Instance Method')
    @classmethod
    def cmethod(cls):
        print('Parent class Class Method')
    @staticmethod
    def smethod():
        print('Parent class Static Method')

class child(Parent):
    def __init__(self):
        super().__init__()
        super().imethod()
        super().cmethod()
        super().smethod()
c=child()


