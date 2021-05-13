class Parent:
    a=10
    def __init__(self):
        self.b=10
class child(Parent):
    a=888
    def __init__(self):
        super().__init__() #to access IV of parent class
        print(self.a) #888
        print(self.b)   #10
        self.b=100
        print(self.b)   #100
        self.a=990
        print(self.a)   #990
        print(child.a)  #888
        print(Parent.a) #10
c=child()



