()

'''__________________________Ordered Dictionary_________________________'''
print("")
print("Ordered Dictionary:")
from collections import OrderedDict


def creating_ordered_dic():
    Student = OrderedDict([('usn', '123mnos'), ("name", "shikha"), ("cgpa", 7.98), ("sem", 4)])
    print(Student)
    print(type(Student))

    '''Alternate ways:---'''

    Employee = OrderedDict()
    Employee['id'] = 5267
    Employee['name'] = 'raina'
    Employee['salary'] = 10000
    Employee['designation'] = 'Associate Software Developer'
    Employee['location'] = 'Pune'

    print("")
    print("Accessing:")
    print(Student['usn'])
    print(Student['name'])
    print(Student['cgpa'])

    print("")
    print("move-to-end():")
    Student.move_to_end('cgpa', last=True)
    print(Student)
    Student.move_to_end('cgpa', last=False)
    print(Student)

    print("")
    print("pop items():")
    Employee.popitem(last=False)
    print(Employee)
    Employee.popitem()
    print(Employee)
    Employee.popitem(last=True)
    print(Employee)

    print("")
    print("pop():")
    Student.pop('usn')
    print(Student)

    return Student, Employee


def main():
    stud, emp = creating_ordered_dic()
    print(stud)
    print(type(stud))
    print()
    print(emp)
    print(type(emp))


if __name__ == "__main__":
    main()