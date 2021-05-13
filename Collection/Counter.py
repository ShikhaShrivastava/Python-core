'''______________________________Counter_______________________________'''
print("")
print("Counter")


def namedtuple_methods():
    Employee1 = namedtuple('Employee1', ['id', 'name', 'age', 'designation', 'salary'])
    e1 = Employee1(101, "shikha", 24, "software developer", 100000)

    Person = namedtuple('Person', ["phonenumber", "address"])
    p1 = Person(701567283, "Raipur")

    print(e1)
    print(p1)
    print(e1._fields)

    Employee2 = namedtuple('Employee2', Employee1._fields + Person._fields)
    e2 = Employee2(120, "vishal", 23, "manager", 50000, 98338263, "durg")
    print(e2)

    print("")
    print("replacing namedtuple")
    new_namedtuple = e1._replace(name="riya")
    print(new_namedtuple)

    print("")
    print("make")
    Student = namedtuple('Student', ['rollnumber', 'subject', 'clas'])
    s1 = Student('12345', 'maths', '1')

    lst = ['10256', 'english', '2']
    print(Student._make(lst))

    print(s1._asdict())

    print(s1._field_defaults)


if __name__ == "__main__":
    namedtuple_methods()
