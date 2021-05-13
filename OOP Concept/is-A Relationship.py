class Parent:
    def __init__(self):
        print('Inside Parent class')

class Child(Parent):
    '''def __init__(self):
        super().__init__()  //super Method call'''
    pass

c=Child()
