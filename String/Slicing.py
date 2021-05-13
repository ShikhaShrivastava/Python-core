def slicing():
    data = "Life is Incomplete"
    print(data[8:17])


if __name__ == "__main__":
    slicing()

print("example-2")


def concatinating():
    d1 = "java"
    d2 = "python"
    d3 = d1 + d2
    print(d3[4:10])
    print(d3[4:])
    print(d3[:10])
    print(d3[:])
    print(d3[::-1])
    print(d3[4::2])
    print(d3[-4::3])


if __name__ == "__main__":
    concatinating()
