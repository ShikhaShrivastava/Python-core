class Parent:
    a=10
    def __init__(self):
        self.b=40
class child(Parent):
    a=888
    def __init__(self):
        super().__init__()
        print(super().a)  #10
        #print(super().b)----->Attribute Error
        print(self.a)   #888
        print(child.a)  #888
        print(Parent.a) #10
        print(self.b)   #40

c=child()
