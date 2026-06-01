
# A module is a python file containing code you want to include in your program
# built in or you can create your own(import keyword)

# print(help("modules"))
# print()
# print(help("math"))

import math
# print(math.pi)

import math as m
# gives the import an alias so u can use the alias instead

from math import e
# for specific variable or function - it could lead to naming conflict

print(e)

# Now I have access to everything in the math module, ie the variables and functions

print(m.pi)

a,b,c,d,e = 1,2,3,4,5
# At this point, e which is exponential is reassigned 5
print(e ** a)
print(e ** b)
print(e ** c)
print(e ** d)

# USE MATH.PI INSTEAD

print(math.e ** a)
print(math.e ** b)
print(math.e ** c)
print(math.e ** d)