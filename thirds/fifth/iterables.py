# an iterable is an object/collection that can return its elements one at a time
# allowing it to be iterated over in a loop

Numbers = [1,2,3,4,5]
# List
for number in Numbers:
    print(number, end=" ")
print()
for number in reversed(Numbers):
    print(number, end="-")

tuple_Number = (1,2,3,4,5)
# Tuple
print()
for number in tuple_Number:
    print(number, end="=")

print()
fruits = {"apple", "orange", "banana","coconut"}
# A set (sets are not reversible
for fruit in fruits:
    print(fruit)
print()

name = "Alex Uche"
for character in name:
    print(character, end=" ")

print()
my_dictionary = {"A":1, "B":2, "C":3}

for item in my_dictionary:
    print(item)
# Iterating over a dictionary returns a key and not the values

print()

# my_dictionary.value returns the value of your dictionary as iterables
for value in my_dictionary.values():
    print(value)
print()

# my_dictionary.items returns the key value pairs in the dictionary as iterables

for key,value in my_dictionary.items():
    print(f"{key} = {value}")
    print(key,value)
    print()