# *args - allows you to pass multiple non-key arguments(args) - packs arguments into a tuple
# **kwargs - allows you to pass multiple keyword arguments(keyword arguments kwargs) - packs arguments into a dictionary
#             * unpacking operator
# arbitrary - varying amount of arguments


def add_function(*args):
    # print(type(args))
    total =0
    for arg in args:
        total+=arg
    return total
print(add_function(1,2, 3, 4,6,7))

def display_name(*names):
    for name in names:
        print(name, end=" ")

display_name("Dr.", "Spongebob","Harold" ,"Squarepants","III")
print()
def print_address(**kwargs):
    # print(type(kwargs))
    for value in kwargs.values():
        print(value)
    for key in kwargs.keys():
        print(key)
    for key,value in kwargs.items():
        print(f"{key}:{value}")
print_address(street="123 Fake St.",apartment="100" ,city="Detroit", state="MI", zip="54321")

def shipping_label(*args, **kwargs):
    # args before keywords
    for arg in args:
        print(arg, end=" ")
    print()
    if 'apartment' in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apartment')}")

    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')} {kwargs.get('state')}, {kwargs.get('zip')}")


shipping_label("Dr", "Spongebob","Squarepants", "III", street ="123 Fake St.", apartment="100", city="Detroit", state="MI", zip="54321", pobox="PO box #1001")