friends =5
# friends +=1
#augumented arithmetic operator
# friends -=2
# friends *= 3
# friends /=2
# friends **=2

remainder = friends % 3
#remember if a number is divided by 2 without a remainder(0), then it is even, else it is odd

x = 3.54
y=-4
z = 5

result = round(x)
res = abs(y)
power = pow(y, 2)
print (max(x,y,z))
print (min(x,y,z))
print(result)
print(res)
print(power)
print(remainder)

import math

print(math.pi)
print(math.e)
res = math.sqrt(x)
print(res)
res = math.ceil(x)
#always rounds a floating point up
print(res)

res = math.floor(x)
#always round a floating point down
print(res)

radius = float(input("Enter the radius(cm): "))
circumference =2* math.pi * radius
area = math.pi * pow(radius, 2)
print(f"The circumference of the circle is {round(circumference, 2)}cm")
print(f"The area of the circle is {round(area, 2)}cm^2")

adj = float(input("Enter the adjacent side(cm): "))
opp = float(input("Enter the opposite side(cm): "))

hyp = math.sqrt(pow(adj,2) + pow(opp,2))

print(f"The hypotenuse of the triangle is {hyp}cm")

age = int(input("Enter your age: "))
if age >= 18:
    print("You are now signed up")
elif age<0:
    print("You havent been born yet")
elif age>=100:
    print("You are too old to sign up")
else:
    print("You must be 18+ to access this website")

response = input("Would you like some food (Y/N): ")
if response == "Y":
    print("Have some food")
else:
    print("No food for u")

name = input("Enter your name: ")
if name == "":
    print("You didn't type in your name!")
else:
    print(f"Hello, {name}")

for_sale = True
if for_sale:
    print(f"This item is for sale")
else:
    print("This item is not for sale")

is_online = False
if is_online:
    print("The user is online")
else:
    print("The user is offline")