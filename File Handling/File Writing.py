# if file not present it create by own

def file_writing():
    f = open("abc.txt", "w")  # opening
    f.write("Today is Saturday")
    f.close()
    f1 = open("abc.txt", "r")
    print(f1.read())


def main():
    file_writing()


if __name__ == "__main__":
    main()
