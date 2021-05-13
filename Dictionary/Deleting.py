# Deletion:
d = {"brand": "ford", "model": "Mustang", "year": 1995}
print(d)
print("Deletion:")
print(d.popitem())
print(d)

print(d.pop("year"))
print(d)

del d["brand"]
print(d)

d.clear()
print(d)

d1 = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e"}
# del d1
# print(d1)
