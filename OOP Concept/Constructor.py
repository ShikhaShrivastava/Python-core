class Cricketer:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def disp(self):
        print(f'{self.name}')
        print(f'{self.age}')


if __name__ == "__main__":
    r = Cricketer('Shikha', 24)
    r.disp()


