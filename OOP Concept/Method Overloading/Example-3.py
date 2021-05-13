# ex2
# Wap to handle overloaded method requirement

class calculator:
    def add(self, a=None, b=None, c=None):

        if a != None and b != None and c != None:
            return a + b + c

        elif a != None and b != None:
            return a + b

        elif a != None:
            return a + 10

        else:
            print('Zero Argument')


if __name__ == '__main__':
    c = calculator()
    print(c.add(10))
    print(c.add(10, 20))
    print(c.add(20, 30, 40))
    print(c.add())
