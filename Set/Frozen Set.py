print("Frozen Set")  # ----->Immutable set
s = {1, 2, 3, 4, 5}
s1 = frozenset(s)
print(s1)
print(type(s1))

s.add(6)
print(s)
# s1.discard(5)
# print(s1)
# s1.remove(5)  //ATTRIBUTE ERROR
# print(s1)
# s1.add(55)
# print(s1)