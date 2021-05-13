class Bike:
    def __init__(self, name, model, colour, price):
        self.name = name
        self.model = model
        self.colour = colour
        self.price = price

    def get_bike_detail(self):
        print(self.name, '-', self.model, '-', self.colour, '-', self.price)


class Employee:
    def __init__(self, ename, esalary, bike):
        self.ename = ename
        self.esalary = esalary
        self.bike = bike

    def display_emp_info(self):
        print('Information of Employee:')
        print('Name of Employee:', self.ename)
        print('Salary of employee:', self.esalary)
        self.bike.get_bike_detail()

        print('*************************************')


bike = Bike('Royal Enfield', 'classic 350', 'black', 2000000)
e = Employee('Shubham', 100000, bike)
e.display_emp_info()

print()
