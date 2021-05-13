def fibo(num):
    a, b = 0, 1
    while a < num:
        yield a
        a, b = b, a + b


for i in fibo(40):
    print(i)
