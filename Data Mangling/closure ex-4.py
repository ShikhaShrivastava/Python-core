def outerfun():
    x = 99

    def innerfun():
        print(x)

    return innerfun


if __name__ == '__main__':
    ref = outerfun()
    ref()
    # del outerfun()
    # ref()
