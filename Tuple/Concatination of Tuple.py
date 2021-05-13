'''Concatination of Tuple'''
tup = (1, 2, 3, 4, 5)
print(tup)
print(type(tup))
print(id(tup))

tup1 = (6, 7, 8, 9)
print(tup1)
print(type(tup1))
print(id(tup1))
tup = tup + tup1
print(tup)
print(type(tup))
print(id(tup))
print(" ")

print("Unpacking")
tup2 = (2, 6, 7, 3, 5)
print(tup2)
a, b, c, d, e = tup2
print(a, b, c, d, e, sep='*')


