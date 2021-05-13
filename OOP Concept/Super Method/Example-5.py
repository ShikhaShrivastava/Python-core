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
    '''print('Instance Method')
    def child_imethod(self):
        super().__init__()
        super().imethod()
        super().cmethod()
        super().smethod()
    print('Static Method')
    def child_smethod():
        super().__init__()
        super().imethod()
        super().cmethod()
        super().smethod()

    print()'''
    print('class Method')

    def child_cmethod(cls):
        super().__init__()
        super().imethod()
        super().cmethod()
        super().smethod()


c = child()
# c.child_imethod()
# c.child_smethod()
c.child_cmethod()

