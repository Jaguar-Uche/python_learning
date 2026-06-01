#Tuples

# ordered and unchangeable(You cant even add or delete after declaring). It allows duplicates, and it is faster than list
# Use tuples over list

fruits = ("apple", "orange", "banana", "coconut", "coconut")

# print(dir(fruits)) for displaying the methods on a tuple
# print(help(fruits)) for explaining the methods on a tuple

print(len(fruits))
# This is for finding the length of a tuple

print("orange" in fruits)
# Checks for if an element is inside the tuple

print(fruits.index("orange"))
# This prints the index of an element in the tuple

print(fruits.count("coconut"))
# This prints the number of element(s) found inside the tuple

# It is iterable so u can iterate over it with a for loop

for fruit in fruits:
    print(fruit)
print(fruits)