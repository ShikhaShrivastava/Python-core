# Program to count the no. of reference pointing to same object

import sys


class Animal:
    pass


ref1 = Animal()
ref2 = ref1
print("Reference count is", sys.getrefcount(ref1))
ref3 = ref2
ref4 = ref3
print("Reference count is", sys.getrefcount(ref1))
