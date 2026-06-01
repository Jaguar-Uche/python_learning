
# keyword argument is an argument preceded by an identifier
# order of arguments does not matter

def hello(greeting, title, first_name, last_name):
    print(f"{greeting} {append_full_stop(title)}{first_name} {last_name}")

def append_full_stop(name):
    if name[len(name) -1] == '.':
        return name
    else:
       return name + '.'

hello("Hello", "Mr.", "Spongebob", "Squarepants")
# For this line here, position matters cause if you pass in hello as first name, it displays something else

hello(title="Mrs", greeting="Good Morning", last_name="Griffin", first_name="Lois")
hello("Hello", "Mrs",last_name="Griffin", first_name="Lois")
# positional arguments first before keyword arguments

for x in range(1,11):
    print(x, end=" ")
    # end is a keyword argument
    # print()
print()
print("1", "2", "3", "4", "5", sep="-")
# separate keyword to separate them with a dash

def get_phone(country_code, area_code, first_digits, last_digits):
    return f"{country_code}-{area_code}-{first_digits}-{last_digits}"

phone_num = get_phone(country_code=1, area_code=123, first_digits=456, last_digits=7890)
print(phone_num)