def working_binary():
    with open(r"D:\shikha\pune\bua.jpg", "rb")as f1:
        with open("chikoo.jpg", "wb")as f2:
            binary_data = f1.read()
            f2.write(binary_data)
            print("chikoo image copied")


def main():
    working_binary()


if __name__ == "__main__":
    main()

