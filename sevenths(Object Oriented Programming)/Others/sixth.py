
# Decorator - A function that extends the behaviour of another function w/o modifying the base function
# You pass the base function as an argument to the decorator

def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("*You add sprinkles🎊*")
        func(*args, **kwargs)
    return wrapper

# Without the wrapper, you call the function as soon as the decorator is applied

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("You add fudge 🍫")
        func(*args, **kwargs)
    return wrapper

@add_sprinkles
@add_fudge
def get_ice_cream(flavour):
    print(f"Here is your {flavour} ice cream 🍧")

# When you want to accept parameters for these decorators, you pass it into the wrapper as *args, **kwargs and pass it down

get_ice_cream("vanilla")