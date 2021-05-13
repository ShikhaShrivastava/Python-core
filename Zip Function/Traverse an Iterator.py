# How to traverse an iterator
names = ['shikha', 'shubham', 'raina']
roll_no = [2, 1, 3]
marks = [98, 76, 57]

l = list(zip(names, roll_no, marks))
for tup in l:
    print(tup)

# case-2 (Using For loop)
names = ['shikha', 'shubham', 'raina']
roll_no = [2, 1, 3]
marks = [98, 76, 57]

for tup in zip(names, roll_no, marks):
    print(tup)

# case-3
names = ['shikha', 'shubham', 'raina']
roll_no = [2, 1, 3]
marks = [98, 76, 57]

for l1, l2, l3 in zip(names, roll_no, marks):
    print(l1, l2, l3)

# case-4 Using zip() on single list

marks = [98, 67, 89]
l = list(zip(marks))
print(l)

# case-5
k = ['a', 'b', 'c', 'd']
v = [1, 2, 3, 4]
d = {}

for key, val in zip(k, v):
    d[key] = val
print(d)
