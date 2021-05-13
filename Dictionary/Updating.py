# updating 1 item:
d = {"brand": "ford", "model": "Mustang", "year": 1995}
print(d)
print("updating:")
d["year"] = 2020
print(d)

# updating more Number of items
print(" ")
print("updating more Number of items:")
d.update({"Mileage": 35, "type": "petrol"})
print(d)

# updating using list of tuple method
print(" ")
print("updating using list of tuple method")
d.update([(1, "a"), (2, "b")])
print(d)
