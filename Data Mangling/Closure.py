def outerfun():
    x = 99

    def innerfun():
        print(x)

    innerfun()


if __name__ == '__main__':
    outerfun()
