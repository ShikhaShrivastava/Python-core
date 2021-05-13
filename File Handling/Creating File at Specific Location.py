# creating a file at specific path

import os


def creating_file_specificpath():
    # creating a root path

    # syntax=join(path,filename)
    filepath = os.path.join("D:\python", "StudentInfo.txt")

    f = open(filepath, 'w')
    abc_stud_info = ['shikha\t', 'ABCJAN20UPA2BTM002\t', 'UC3']
    f.writelines(abc_stud_info)
    print("student info written successfully")
    print('Is file closed or not:', f.closed)
    f.close()

    print('Is file closed or not:', f.closed)


def main():
    creating_file_specificpath()


if __name__ == "__main__":
    main()
