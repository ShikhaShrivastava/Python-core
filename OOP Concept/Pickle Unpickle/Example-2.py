#Pickling
import pickle, EmployeeInfo

f = open('employee.txt', 'wb')
n = int(input('Enter the number of object\n'))
for i in range(n):
    name = input('Enter the name\n')
    addr = input('Enter the address\n')
    sal = int(input('Enter the salary\n'))
    ref = pickling2.Employee(name, addr, sal)
    pickle.dump(ref, f)
print('pickling is completed')
f.close()

