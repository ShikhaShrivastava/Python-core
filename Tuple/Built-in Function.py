"""Built in Functions"""
print(" ")
print("Built in Functions:")
print(" ")
tup1 = (2, 14, 5, 8, 23, 65, 40, 1000, 120000, 223334)
print(tup1)
print(" ")
print("Maximum Value:")
print(max(tup1))
print(" ")
print("Minimum Value")
print(min(tup1))
print(" ")
print("Length of tuple")
print(len(tup1))
print(" ")

print("1.Enumerate:")
tup1 = (2, 14, 5, 8, 23, 65, 40, 1000, 120000, 223334)
for i, j in enumerate(tup1):
    print("Index is:", i, "& Value is:", j)
print(" ")
print("2. Range Function():")
for i in range(len(tup1)):
    print("Index is:", i, "& Value is:", tup1[i])
