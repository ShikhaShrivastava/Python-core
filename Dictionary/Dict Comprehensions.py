# For loop
l1 = [1, 2, 3, 4, 5]
d = {}
for i in l1:
    d[i] = i ** 2
print(l1)
print(d)

# Comprehension
l1 = [1, 2, 3, 4, 5]
d = {i: i ** 2 for i in l1}
print(l1)
print(d)

# ************************************************************

# if-condition
l2 = [1, 2, 3, 4, 5]
d = {}
for i in l2:
    if i % 2 == 0:
        d[i] = i ** 2
print(l2)
print(d)

# Comprehension
l2 = [1, 2, 3, 4, 5]
d = {i: i ** 2 for i in l2 if i % 2 == 0}
print(l2)
print(d)

# **************************************************************

# if-else condition

l3 = [1, 2, 3, 4, 5]
d = {}
for i in l3:
    if i % 2 == 0:
        d[i] = i ** 2
    else:
        d[i] = i ** 3
print(l3)
print(d)

# Comprehension
l3 = [1, 2, 3, 4, 5]
d = {i: (i ** 2 if i % 2 == 0 else i ** 3) for i in l3}
print(l3)
print(d)

# *******************************************************************

# Changing key value pair
l4 = [1, 2, 3, 4, 5]
d = {}
for i in l4:
    if i % 2 == 0:
        d[i ** 2] = 'Square'
    else:
        d[i ** 3] = 'Cube'
print(l4)
print(d)

# comprehension
l4 = [1, 2, 3, 4, 5]
d = {(i ** 2 if i % 2 == 0 else i ** 3): ('Square' if i % 2 == 0 else 'Cube') for i in l4}
