def reading_data():
    f = open("D:\sample\myfile.txt", "r")
    # print(f.read())

    # print(f.read(5))

    # print(f.readline())

    lst = f.readlines()
    print(lst)

    for line in lst:
        print(line, end='')
    print("")
    f.close()

    if f.close() == True:
        print("file is closed")
    else:
        print("file is not closed")


def main():
    reading_data()


if __name__ == "__main__":
    main()


