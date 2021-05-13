from time import sleep


def countdown(num):
    print('Count down Starting.....')
    while num > 0:
        yield num
        num = num - 1


values = countdown(10)
for x in values:
    print(x)
    sleep(2)
