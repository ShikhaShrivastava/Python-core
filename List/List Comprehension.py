'''List Comprehension'''
# using loop
print("using loop")
lst1 = []
lst = [1, 2, 3, 4, 5]
for i in lst:
    lst1.append(i ** 2)
    print(lst1)

# using Comprehensions:
print("using Comprehensions")
lst = [1, 2, 3, 4, 5]
lst1 = [i ** 2 for i in lst]
print(lst1)

# *************************************************************************************************
# using if condition:
print(" ")
print("Using if condition")
lst1 = []
lst = [1, 2, 3, 4, 5]
for i in lst:
    if i % 2 == 0:
        lst1.append(i ** 2)
print(lst1)

print("using Comprehensions-: I")
lst = list(range(1, 21))
lst1 = [i ** 2 for i in lst if i % 2 == 0]
print(lst1)

print("using Comprehensions-: II")
lst = [20, 23.4, True, "Corona", 34 + 5j, 56, [1, 2, 3], 66, (4, 5), 5]
lst1 = [i ** 2 for i in lst if type(i) == int]
print(lst1)

# ************************************************************************************************

'''using Multiple if Condition'''
print(" ")
print("using Multiple if Condition")
lst1 = []
lst = list(range(1, 21))
for i in lst:
    if i > 8:
        if i < 17:
            lst1.append(i ** 2)
print(lst1)

print("using Comprehensions")
lst = list(range(1, 21))
lst1 = [i ** 2 for i in lst if i > 8 if i < 17]
print(lst1)

# ************************************************************************************************
'''Using if-else condition'''
print(" ")
print("Using if-else condition")
lst1 = []
lst = list(range(1, 11))
for i in lst:
    if i % 2 == 0:
        lst1.append(i ** 2)
    else:
        lst1.append(i ** 3)
print(lst1)
print("using Comprehensions")
lst = list(range(1, 21))
lst1 = [i ** 2 if i % 2 == 0 else i ** 3 for i in lst]
print(lst1)
