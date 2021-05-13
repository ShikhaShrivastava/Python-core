'''Operator Overloading'''

#type-1
'''print(10+20+30) #addition
print('sh'+'ik'+'ha') #concatination'''

#**********MAGIC METHOD*******************


#type-2
'''class Book:
    def __init__(self,page):
        self.page=page

b1=Book(200)
b2=Book(400)
#print(b1+b2) --->TypeError :Unsupported operand type
print(b1.page+b2.page)'''

#***************************************************************
#type-3
class Book:
    def __init__(self,page):
        self.page=page

    def __add__(self,other):
        print(id(self))
        print(id(other))
        return self.page+other.page #b1.page+b2.page

b1=Book(200)
b2=Book(400)
print(id(b1))
print(id(b2))
print(b1+b2)

#**************************************************************
#type-4
'''class Book:
    def __init__(self,page):
        self.page=page

    def __add__(self,other,another):
        return self.page+other.page+another.page #b1.page+b2.page

b1=Book(200)
b2=Book(400)
b3=Book(100)
print(b1+b2+b3)''' #//Error
 #Note: Inside Magic Method we can not have more than 2 parameter

#******************************************************************
#type-5

'''class Book:
    def __init__(self,page):
        self.page=page
    def __add__(self,other):
        return (self.page+other.page)
    def __str__(self):
        #return "I will get called when print is encountered"
        return str(self.page)

b1=Book(200)
b2=Book(400)
print(b1)
print(b2)
print(b1+b2)'''
#********************************************************************
#type-6

'''class Book:
    def __init__(self,page):
        self.page=page
    def __add__(self,other):
        return Book(self.page+other.page)
    def __str__(self):
        return str(self.page)

b1=Book(200)
b2=Book(400)
b3=Book(120)
print(b1+b2+b3)'''
