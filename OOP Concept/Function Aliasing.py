'''Funtion Aliasing'''


def calculator():
    print('Calculator function is called')

    def add():
        print('Add function is called')

    a = add
    a()


print(calculator)
print(id(calculator))
print(type(calculator))
c = calculator
print(id(c))
c()
