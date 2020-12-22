import math

print(math.cos(1))
math.log10(100)

import copy

a = [1,2,3]
b = a
c = a[:]
d = copy.copy(a)
a[0] = 4
print(a,b,c,d)
print(id(a),id(b),id(c), id(d))

import sys

print(sys.path)
