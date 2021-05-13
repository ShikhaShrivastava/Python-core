def fun():
    num = 1
    yield num

    print(num)
    num = 2
    print(num)
    yield num
    num = 3
    print(num)
    yield num


f = fun()
print(f)
print(next(f))
#print(next(f))
#print(next(f))
