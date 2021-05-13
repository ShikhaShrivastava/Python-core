'''Creating copy of List'''
# using Slicing Techniques-cloning process

print("Creating copy of list using Slicing Techniques")
lst = [1, 2, 3, 4, 5]
print(lst)
print(id(lst))

lst1 = lst[:]
print(lst1)
print(id(lst1))

lst1.append(6)
print(lst)
print(lst1)

lst1.remove(3)
print(lst)
print(lst1)

# using Build in Function-list()
print(" ")
print("Creating copy of list using built in function list()")
print(" ")
lst = [1, 2, 3, 4, 5]
print(lst)
print(id(lst))

lst1 = list(lst)
print(lst1)
print(id(lst1))

lst1.append(6)
print(lst)
print(lst1)

lst1.remove(3)
print(lst)
print(lst1)
