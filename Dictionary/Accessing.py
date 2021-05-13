# accessing
print(" ")
print("Accessing:")
d = {"brand": "ford", "model": "Mustang", "year": 1995}
print(d)
print(d["model"])
print(d.get("year"))
# print(d["cost"])
# print(d.get("cost"))

print("Different way to access dictionary:")
d = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
print(d.keys())
print(list(d.keys()))
print(d.values())
print(list(d.values()))
print(d.items())
print(list(d.items()))
