#input() returns the input data as string

name = input("What is your name? ")

age = input("How old are you? ")
#convert to your normal data type after accepting
age = int(age)
age +=1

gpa = float(input("What is your currrent gpa? "))
gpa +=1

print(f"Hello, {name}")
print("Happy Birthday!")
print(f"You are {age} years old.")
print(f"You have a gpa of {gpa}")

length = float(input("What is the length of the rectangle? "))
width = float(input("What is the width of the rectangle? "))

area = length * width
print(f"The area of the rectangle is {area} cm2")

item = input("What item are u trying to buy? ")
price = float(input(f"What is the price of each {item}? "))
quantity = int(input(f"How many {item}s are available? "))
total = price * quantity

print(f"There are {quantity} {item}s each at a price of ${price}. It would cost ${total} to get them all ")