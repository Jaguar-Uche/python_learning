#This is my first python program

print("I like Wrestling")
print("It's really good!")

#variable is a container for a value(a variable behaves as the value it contains)

first_name = "Alex"
food = "Rice"
email = "alex222@gmai.com"


print(f"Hello {first_name}")
#f - string puts string together with variable. u put the variable in braces
print(f"You like {food}")
print(f"Your email is {email}")
#These are all strings

#integers

age = 22
quantity = 3
num_of_students = 30

print(f"You are {age} years old")
print(f"You have selected {quantity} items")
print(f"Your class has {num_of_students} students")


#float
price = 10.99
gpa = 3.2
distance = 5.5
print(f"The price is ${price}")
print(f"My gpa is {gpa}")
print(f"You ran {distance} kilometers")

#boolean
is_student = False
is_graduated = True

print(f"Are you a student? {is_student}")
if is_student:
    print(f"You are a student")
else:
    print("You are not a student")

for_sale = True
if for_sale:
    print("That item is for sale")
else:
    print("That item is not available")

is_online = True

if is_online:
    print("You are online")
else:
    print("You are not online")

#TypeCasting is the process of converting a variable from one data type to another

name = " "
years_old = 25
grade = 3.6
is_enrolled = True

print(type(is_enrolled))
#for printing the type of variable

gpa = int(gpa)
#converts to integer(it doesn't approximate, it just throws the decimal part away)
print(gpa)

years_old = float(years_old)
print(years_old)

age = str(age)
age += "1"
#This is for string concatenation
print(age)

name = bool(name)
#If u typeCast a string of text to a boolean even if there is like only one space or something, it gives true but if the string is empty, it returns false
#For checking if input was actually entered or not
print(name)