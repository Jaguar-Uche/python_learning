# a function is a block of reusable code

def happy_birthday(name, age):
    print(f"Happy birthday to {name}")
    print(f"You are {age} years old!")
    print(f"Happy birthday to {name}")
    print()


happy_birthday("Alex", 20)
# happy_birthday("Steve",13)
# happy_birthday("Joe",15)

def display_invoice(username, amount, due_date):
    print(f"Hello, {username}!")
    print(f"Your bill of ${amount:.2f} is due on {due_date}.")

display_invoice("Nkechi", 20000, "01/01/2026")

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
print(add(1.3,2))
#  data type dont matter
print(sub(1,0.2))
print(mul(1,2))
print(div(1,2))

def create_name(first_name, last_name):
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()

    return first_name + " " + last_name

full_name = create_name("barlec", "uche")
print(f"{full_name}")