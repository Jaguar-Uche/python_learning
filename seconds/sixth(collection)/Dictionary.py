# A dictionary is a collection of key : value pairs ordered and changeable and does not allow duplicates

capitals = {"USA": "washington Dc",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

# print(dir(capitals)) - to get the methods operable on a dictionary
# print(help(capitals)) - to get the full list of things you can do to a list

# To get a value from a dictionary
print(capitals.get("India"))
# the value associated with the key u passed into the get method

print(capitals.get("china"))
# returns none if it is not found and it is case-sensitive

if capitals.get("china"):
    print("That capital exists")
else:
    print("That capital doesn't exist")

# Updating a dictionary
capitals.update({"Germany":"Berlin"})
# adds this to the dictionary
capitals.update({"USA": "Detroit"})
# changes the existing capital of the USA
print(capitals)

# removing(pass in the key)
# capitals.pop("China")

# removing the latest item in the dictionary
# capitals.popitem()
# This removes the latest key - value pair

# capitals.clear()
#clearing the dictionary entirely

print(capitals)
# to get all the keys but not the values
keys = capitals.keys()
# this returns an object (the keys are an object)

# the elements inside capitals.keys are iterable
for key in capitals.keys():
    print(key)

print("---------")
values = capitals.values()
# This is for the values without the keys

# print(values) - this is an object and it is iterable

for value in capitals.values():
    print(value)

items = capitals.items()
# returns a 2d list of tuples ie the pairs are inside tuples while the entire thing is a list

for key, value in capitals.items():
    print(f"{key}: {value}")

print(items)
