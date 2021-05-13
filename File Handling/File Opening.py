# opening a file

def file_open():
    f = open("demo.txt", "r")  # opening
    print(f)
    print(f.read())  # reading

    f.close()  # close


def main():
    file_open()


if __name__ == "__main__":
    main()

'''with open("demo.txt","r") as f:
    print(f.read(6))'''

