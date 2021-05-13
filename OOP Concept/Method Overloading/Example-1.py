'''Method Overloading'''
class calculator:
    def add (self,a):
        return a+10

    def add(self,a,b):
        return a+b
    def add(self,a,b,c):
        return a+b+c

if __name__=='__main__':
    c=calculator()
    #print(c.add(10)) --->TypeError
    print(c.add(10,20,30))
