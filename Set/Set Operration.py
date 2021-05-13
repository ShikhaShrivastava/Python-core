print("Set Operation:")
print(" ")
print("a) Union")
s1 = {1, 2, 3, 4, 5}
print(s1)
s2 = {4, 5, 6, 7}
print(s2)
print(s1.union(s2))
print(s2.union(s1))
print(s1 | s2)
print(s2 | s1)

print(" ")
print("b) Intersection")
s1 = {1, 2, 3, 4, 5}
print(s1)
s2 = {4, 5, 6, 7}
print(s2)
print(s1.intersection(s2))
print(s2.intersection(s1))
print(s1 & s2)
print(s2 & s1)

print(" ")
print("c) Difference")
s1 = {1, 2, 3, 4, 5}
print(s1)
s2 = {4, 5, 6, 7}
print(s2)
print(s1.difference(s2))
print(s2.difference(s1))
print(s1 - s2)
print(s2 - s1)

print(" ")
print("d) Symmetric Difference")
s1 = {1, 2, 3, 4, 5}
print(s1)
s2 = {4, 5, 6, 7}
print(s2)
print(s1.symmetric_difference(s2))
print(s2.symmetric_difference(s1))
print(s1 ^ s2)
print(s2 ^ s1)

print(" ")
print("e) Subset")
s1 = {1, 2, 3, 4, 5}
print(s1)
s2 = {4, 5, 6, 7}
print(s2)
print(s1.issubset(s2))
print(s2.issubset(s1))
print(s1 <= s2)
print(s2 <= s1)

print(" ")
print("f) Disjoint Set")
s1 = {1, 2, 3, 4, 5}
print(s1)
s2 = {4, 5, 6, 7}
print(s2)
print(s1.isdisjoint(s2))
print(s2.isdisjoint(s1))

print("")
print("Iteration on Set")
s = {1, 2, 3, 4, 5}
for i in s:
    s1.add(i ** 2)
print(s1)


