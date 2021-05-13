# Using Variable length  Argument:

class Test:
    def sum(self, *a):
        total = 0
        for i in a:
            total = total + i
        print('The sum is:', total)


if __name__ == '__main__':
    t = Test()
    t.sum()
    t.sum(10)
    t.sum(10, 20)
    t.sum(30, 40, 50)
