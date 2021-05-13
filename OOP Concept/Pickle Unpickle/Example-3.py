#unpickling
import pickle, EmployeeInfo

f1=open('employee.txt','rb')
print('Unpickling started')
print('Employee Details are:')
while True:
    try:
        ref1=pickle.load(f1)
        ref1.display()

    except EOFError:
        print('Unpickling is completed')
        break
f1.close()
