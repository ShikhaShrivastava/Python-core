print("MemberShip Operator")

lst = [12, 14, 5, 8, 23, 34, 56, 76, 89, 45]
print(lst)
for i in lst:
    if i == 34:
        print("Element Found")
        break
print(34 in lst)
print(44 in lst)
print(34 not in lst)

# Ex-2  using 'in' operator
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9]
for item in list1:
    if item in list2:
        print("overlapping")
else:
    print("not overlapping")

# not 'in' operator
x = 24
y = 20
list = [10, 20, 30, 40, 50];

if (x not in list):
    print("x is NOT present in given list")
else:
    print("x is present in given list")

if (y in list):
    print("y is present in given list")
else:
    print("y is NOT present in given list")
