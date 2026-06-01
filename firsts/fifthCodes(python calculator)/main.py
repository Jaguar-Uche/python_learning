
operator = input("Enter your operator:(+ - * /) ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(round(num1 * num2, 2))
elif operator == "/":
    print(round(num1 / num2, 2))
else:
    print(f"{operator} is not a valid operation")

weight = float(input("Enter your weight: "))
unit = input("Kilograms or pounds? (K or L):")
validInput = True
if unit == "K":
    weight = weight * 2.205
    unit = "Lbs"
elif unit == "L":
    weight = weight /2.205
    unit = "Kg"
else:
    validInput = False
    print(f"{unit} was not valid")

if validInput:
    print(f"Your weight is: {round(weight, 1)} {unit}")

unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
temp = float(input(f"Enter the temperature in {unit}: "))
is_valid_temp = True
if unit == "C":
    temp = round((9 * temp)/5 + 32, 1)
    unit = "F"
elif unit == "F":
    temp = round((temp-32)* 5/9, 1)
    unit = "C"
else:
    print(f"{unit} is not among the options")
    is_valid_temp = False

if is_valid_temp:
    print(f"Your temperature in {unit} is {temp}degrees")