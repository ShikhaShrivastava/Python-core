(" ")
print("Set Comprehensions:")
print(" ")
print("a) Using Loop-")
s1 = set()
s = {1, 2, 3, 4, 5}
for i in s:
    s1.add(i ** 2)
print(s1)

print(" ")
print("b) Using Comprehensions-")

s = {1, 2, 3, 4, 5}
s1 = {i ** 2 for i in s}
print(s1)

print(" ")
print("c1) Using if condition-")
s1 = set()
s = {1, 2, 3, 4, 5}
for i in s:
    if (i > 0):
        s1.add(True)
print(s1)
''' with comprehension'''
print("c2) Using if condition with comprehensions-")
s = {1, 2, 3, 4, 5}
s1 = {i > 0 for i in s}
print(s1)
