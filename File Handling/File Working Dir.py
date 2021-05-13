import os


def working_dirs():
    cwd = os.getcwd()
    print("plz find ur current dir below:")
    print(cwd)
    os.mkdir("d1/d2/d3")
    os.removedirs("d1/d2/d3")
    os.mkdir("java")
    os.rename("java", "python")
    print(os.listdir())


def main():
    working_dirs()


if __name__ == "__main__":
    main()
