# a collection is a single "variable" used to store multiple values

# List - [] ordered and changeable.

# Set - {} unordered and immutable(you cant change the value of an element inside once it is defined)
# but you can remove and pop add/remove ok, no duplicate values

# Tuples - () ordered and unchangeable. duplicates ok and faster

fruit_one = "citrus"
print(fruit_one)

fruits = ["apple", "orange", "banana", "coconut", "banana"]
#u access an element with fruits[index]
# for fruit in range(len(fruits)):
#     print(fruits[fruit])

# This is better than the line above
for fruit in fruits:
    print(fruit)

#Index operators
print(fruits[:3])
#The first 3(index 0-2) elements(remember the index is exclusive

print(fruits[::-1])
#prints fruits in a backward order

print(fruits[::2])
#begins at zero and prints the second fruit after

print(len(fruits))
#prints the number of elements inside a collection

print("apple" in fruits)
#checks if an element "apple" is in fruits(returns true or false)

fruits[0] = "pineapple"
print(fruits)
#You can reassign the values of List after creating it

#List methods

fruits.extend(["grape","lemon"])
# The .extend takes in an array and adds each element of the array(the .extend params) to the array it is called on

fruits.append("kiwi")
#adds an element to the end of the List
print(fruits)

fruits.remove("pineapple")
#removes an element named in the () from the list
print(fruits)

print(fruits.index("kiwi"))
#returns index of apple


fruits.insert(2, "mango")
#inserting into a particular index
print(fruits)
#It does not replace, it moves the other elements to the right

fruits.sort()
#sorts the List in alphabetical order
print(fruits)

fruits.reverse()
#doesn't reverse alphabetically by default, it reverses the order u placed them in
print(fruits)

print(fruits.count("banana"))
#returns the number of times the element is found in the list returns 0 if it is not found

fruits.clear()
#clears all the elements inside a list
print(fruits)

# print(fruits.index("apple"))
#This returns the index of an element(it says element is not on the list if the element is not found



#To list the methods available to a collection, u use print(dir(collection))

# print(dir(fruits)) -This lists the methods operable on a collection
# print(help(fruits)) - This explains the methods operable on the collection passed in
