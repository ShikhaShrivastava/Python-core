'''___________________________Default Dictionary_______________________'''

print()
print("Regular Dictionary")
Student = {}
print(Student)

Student['usn'] = '1sd2e4lf'
Student['name'] = 'shikha'
Student['cgpa'] = 8.90
Student['subject'] = 'English'

print(Student['name'])
'''print(Student['sem'])'''

print()
print("using Default Dictionary")
from collections import defaultdict


def creating_default_dict():
    '''Student=defaultdict(func())
    Student=defaultdict(func)
    Student=defaultdict(lambda:8)
    Student=defaultdict(lambda:'key not found')
    Student=defaultdict(lambda:'invalid key')
    Student=defaultdict(int)'''
    Student = defaultdict(list)

    print(type(Student))
    '''lst=[('adhar number',1673256732),('address','Durg'),('phone_number',896326)]

 '''   '''Student['usn']='1sd2e4lf'
    Student['name']='shikha'
    Student['cgpa']=8.90
    Student['subject']='English'

    print(Student['name'])
    print(Student['sem'])

    for k,v in lst:
        Student[k].append[v]
    print(Student)'''


def func():
    '''return lambda:8
    return 8'''


def main():
    creating_default_dict()


if __name__ == "__main__":
    main()