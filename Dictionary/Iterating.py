# Different ways of iterating over Dictionary
print("Different ways of iterating over Dictionary:")
print("1st way")
d = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
for i in d:
    print(i)
print()
print("2nd way")
d = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
for i in d.keys():
    print(i)

print()
print("3rd way")
d = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
for i in d.values():
    print(i)

print()
print("4th way")
d = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
for i in d.items():
    print(i)

print()
print("5th way")
d = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
for i, j in d.items():
    print(i, j)
