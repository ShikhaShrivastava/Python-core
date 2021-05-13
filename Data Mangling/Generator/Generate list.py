def firstn(num):
    n=0
    while n<num:
        yield n
        n=n+1
for i in firstn(10):
    print(i)