import pickle
class Student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks

    def display(self):
        print('Name:',self.name)
        print('Age:',self.age)
        print('Marks:',self.marks)

if __name__=='__main__':
    #s=Student('sushant',34,99)
    #s.display()
    f=open('shikhainfo.txt','wb')
    s=Student('shikha',23,99)
    s.display()
    pickle.dump(s,f)
    print('pickling is completed')
    f.close()
#*************unpickling************************
    f1=open('shikhainfo.txt','rb')
    ref=pickle.load(f1)
    print('Unpickling is completed')
    ref.display()
    f1.close()
