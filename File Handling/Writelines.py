# writelines method:

def file_writing():
    f = open("demo.txt", "w")  # opening

    lst = ['shikha\n', 'raina\n', 'shubu\n', 'anup\n', 'durgesh\n', 'kinjol\n']
    f.writelines(lst)
    f.close()
    f1 = open("demo.txt", "r")
    print(f1.read())


def main():
    file_writing()


if __name__ == "__main__":
    main()
