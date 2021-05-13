# with statement

def using_with():
    with open(r'D:\python\StudentInfo.txt', "r+")as f:
        print(f.read(65))

    if f.closed == True:
        print("file is closed")
    else:
        print("file is not closed")


def main():
    using_with()


if __name__ == "__main__":
    main()
