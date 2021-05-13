'''Accessing Index and Value of element from list'''

print("I-Accessing Index & Value of element from list")
print(" ")
print("1.Enumerate")
lst = [1, 2, 3, 4, 5, 6, 7]
print(lst)
for i, j in enumerate(lst):
    print("Index is:", i, "& Value is:", j)

print(" ")
print("2.Range Function")
lst = [1, 2, 3, 4, 5, 6, 7]
print(lst)
for i in range(len(lst)):
    print("Index is:", i, "& Value is:", lst[i])
