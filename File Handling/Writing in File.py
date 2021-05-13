# opening a file

def file_open():
    f = open("demo.txt", "w")  # opening

    f.write("abc\n")  # writing
    f.write("tech\n")  # writing
    f.write("python")  # writing

    f.close()  # close
    f2 = open("demo.txt", "w")  # opening
    f2.write("java\n")  # overridden
    f2.write("laravel is as php frame work\n")  # overridden

    f2.close()

    f1 = open("demo.txt", "r")  # opening
    print(f1.read())
    print(f1.tell())
    print(f1.seek(0))
    f1.close()

    with open("demo.txt", "w")as f3:
        lst = ['shikha\n', 'raina\n', 'disha\n', 'riya\n']
        f3.writelines(lst)
        f3.close()


def main():
    file_open()


if __name__ == "__main__":
    main()
