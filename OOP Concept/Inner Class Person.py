#write a program to create a person and his DOB using the inner class
class Person:
    def __init__(self,name):
        self.name=name
        self.d=self.Dob(20,'sept',1996)


    def display_name_dob(self):
        print('My Name is:',self.name)
        self.d.display_dob()

    class Dob:
        def __init__(self,date,month,year):
            self.date=date
            self.month=month
            self.year=year

        def display_dob(self):
            print('My DOB is:',self.date,'-',self.month,'-',self.year)

p= Person('Shubham')
p.display_name_dob()
