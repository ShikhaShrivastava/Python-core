class Parent:
    a=10
    def __init__(self):
        self.b=10
class child(Parent):
    a=888
    def __init__(self):
        print(self.a)
        #print(self.b)
        self.b=100
        print(self.b)
        #print(Parent.a)
c=child()
