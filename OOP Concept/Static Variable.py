class Teacher:
    # Subject="python" #-----------(1)

    # modification
    mobile = "redmi" # -----------(2)
    print(mobile)
    print(id(mobile))

    mobile = "oppo"
    print(mobile)
    print(id(mobile))

    def __init__(self, mode, hour):
        Teacher.Subject = "python" #-----------------(3)
        Teacher.mobile = "samsung"
        self.mode = mode
        self.hour = hour

    def disp(self):
        Teacher.Subject = "python"  #------------------(4)
        Teacher.mobile = "iphone"

        self.name = "shikha"

    @classmethod
    def cmethod(cls):
        Teacher.institude = "Abc"  #---------------------(5)
        Teacher.mobile = "Micromax"

        cls.name = "Yuvraj"

    @staticmethod
    def smethod():
        Teacher.age = 36  # ------------------(6)
        Teacher.mobile = "vivo"


py1 = Teacher("online", 8)
print(py1.__dict__)
# accessing
print(Teacher.Subject)
print(self.Subject)

# print(py1.Subject)
# print(Teacher.Subject)

'''print()
py1.disp()
print(py1.__dict__)
#accessing
print(py1.Subject)
print(self.Subject)

print()
py1.cmethod()
Teacher.cmethod()
print(py1.__dict__)
print(Teacher.__dict__)
#accessing
print(py1.Subject)
print(self.Subject)


print()
py1.smethod()
print(py1.__dict__)
print(Teacher.__dict__)
#accessing
print(py1.Subject)
print(self.Subject)

print()
Teacher.batchname='UC3' #----------------------(6)
print(Teacher.__dict__)

py2=Teacher("offline",5)
print(py2.__dict__)
py2.disp()
#print(py2.Subject)


'''
