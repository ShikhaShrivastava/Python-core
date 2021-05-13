class Student:
    def __init__(self, name, marks, subject):
        self.name = name
        self.marks = marks
        self.subject = subject

    def disp(self):
        self.city = "Mumbai"

        # accessing

    def disp2(self):
        print(self.name)
        print(self.marks)
        print(self.gender)
        print(s1.name)
        print(s1.marks)
        print(s1.gender)

        # modifying

    def disp3(self, subject):
        self.subject = subject

    def disp4(self):
        self.subject = "python"

        # deleting

    def disp5(self):
        del self.subject
        del self.name


if __name__ == "__main__":
    s1 = Student(name="shikha", marks=56, subject="maths")
    print(s1.__dict__)

    s1.disp()
    print(s1.__dict__)

    s1.gender = "female"
    print(s1.__dict__)

    s1.disp2()
    print(s1.__dict__)

    s1.disp3(subject="java")
    print(s1.__dict__)

    s1.disp4()
    print(s1.__dict__)

    # modify
    s1.name = "shubh"
    print(s1.__dict__)

    # remove
    del s1.marks
    print(s1.__dict__)

    s1.disp5()
    print(s1.__dict__)

    del s1.__dict__
    print(s1.__dict__)

    # accessing
    print(self.name)  # //error
    print(self.marks)  # //error
    print(self.gender)  # //error
    print(s1.name)
    print(s1.marks)
    print(s1.gender)


