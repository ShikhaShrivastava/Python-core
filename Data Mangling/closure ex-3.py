y = 10


def outer():
    z = 4

    def inner():
        x = 4
        print(x)

    inner()
    print(z)


outer()
print(y)
