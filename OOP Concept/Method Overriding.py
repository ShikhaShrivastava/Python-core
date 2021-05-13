# *****************Method Overriding****************************

# eg-1

class Parent:
    def property(self):
        print('Cash Land and car')

    def bike(self):
        print('Take Ktm 200')


class child(Parent):

    def bike(self):
        super().bike()
        print('No i will take royald enfield')


if __name__ == '__main__':
    c = child()
    c.property()
    c.bike()


# ******************************************************************************
class Parent:
    def __init__(self):
        print('Take splender bike')


class child(Parent):
    def __init__(self):
        # super().__init__() super method can be written anywhere
        print('No i will take royald enfield')
        super().__init__()


if __name__ == '__main__':
    c = child()
