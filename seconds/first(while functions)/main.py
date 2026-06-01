#while loop(execute code until a condition is not true)
#remember u need to give the user a way to break the loop
name = input("What is your name? ")
if name == "":
    print("You didn't enter your name.")
else:
    print("Hello, " + name)

while name == "":
    name = input("What is your name? ")
print("Hello, " + name)

age = int(input("What is your age? "))
while age<0:
    print("Age cannot be negative.")
    age = int(input("What is your age? "))
print(f"You are {age} years old.")

food = input("Enter a food you like (q to quit): ")

while food != "q":
    print("That's nice")
    food = input("Enter a food you like (q to quit): ")
#not is a logical negation operator while != is a comparison operator

num = int(input("Enter a number between 1 and 10: "))

while num<1 or num>10:
    num = int(input("Enter a number between 1 and 10: "))
print(f"Your number is {num}")
