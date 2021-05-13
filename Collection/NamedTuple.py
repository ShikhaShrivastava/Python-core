'''____________________Namedtuple____________________'''
print("")
print("with normal tuple")
def employee_info():
    emp1=(101,"shikha","software developer","Wipro",24)
    emp2=(320,"shubham","business development associate","byjus",25)
    print(emp1)
    print(type(emp1))
    print(emp2)
    print(type(emp2))
    print(emp1[0])
    print(emp1[3])
    print(emp2[0])
    print(emp2[2])

if __name__=="__main__":
    employee_info()

print("")
print("with namedtuple")
from collections import namedtuple
'''def creating_namedtuple():
    Employee=namedtuple('Employee',['id','name','age','designation','salary'])
    e1=Employee(101,"shikha",24,"software developer",100000)
    e2=Employee(204,"riya",28,"sales executive",23000)

    print("--------different ways of excessing-----")
    print(e1)
    print(e1.id)
    print(e2.name)
    print(e1.salary)
    print(e1[0],e1[1],e1[2])
    print(e2[0],e2[1])
    print(getattr(e1,'designation'))

    print("-------checking for immutability of namedtuple---------")
    e1[1]="Shubham"
    e2.age=22
if __name__=="__main__":
    creating_namedtuple()'''

