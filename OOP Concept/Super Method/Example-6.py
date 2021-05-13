class A:
    def m1(self):
        print('A class method')
class B(A):
    def m1(self):
        print('B class method')
class C(B):
    def m1(self):
        print('C class method')
class D(C):
    def m1(self):
        print('D class method')
class E(D):
    def m1(self):
        super().m1() #D class method
        super(D,self).m1() #C class method
        super(B,self).m1()  #A class method
        B.m1(self) #B class method
        D.m1(self)  #D class method

e=E()
e.m1()

