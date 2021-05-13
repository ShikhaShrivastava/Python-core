'''creating copy of Nested list'''
# shallow copy
print(" ")
print("Creating Copy Of Nested List")
print(" ")
print("1. Shallow Copy")
print(" ")
lst1 = [[1, 2], [3, 4]]
print(lst1)
print(id(lst1))
print(id(lst1[0]))

print("copied list=")
lst2 = lst1[:]
print(lst2)
print(id(lst2))
print(id(lst2[0]))

print("Appending=")
lst1.append([5, 6])
print(lst1)
print(lst2)

print("adding 33=")
lst1[1][0] = 33
print(lst1)
print(lst2)

# Deep Copy
import copy

print(" ")
print("2.Deep Copy")
print(" ")
lst11 = [[1, 2], [3, 4]]
print(lst11)
print(id(lst11))
print(id(lst11[0][1]))

print("copied list=")
lst22 = copy.deepcopy(lst11)
print(lst22)
print(id(lst22))
print(id(lst22[0][1]))

print("Appending=")

lst11.append([5, 6])
print(lst11)
print(lst22)

print("adding 33=")

lst11[1][0] = 33
print(lst11)
print(lst22)
