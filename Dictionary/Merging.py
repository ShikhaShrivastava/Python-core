# 'Merging of Dictionary:

print('2 Dictionary have no duplicate:-')
d1 = {1: 'a', 2: 'b', 3: 'c'}
d2 = {4: 'd', 5: 'e'}
d1.update(d2)
print(d1)
# d3={**d1,**d2}
# print(d3)
print()
print('2 Dictionary have duplicate:-')
d1 = {1: 'a', 2: 'b', 3: 'c'}
d2 = {4: 'd', 2: 'b'}
# d1.update(d2)
d3 = {**d1, **d2}
print(d3)
# print(d1)
