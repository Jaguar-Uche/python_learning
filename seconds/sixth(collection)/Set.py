#Set

#works well with constants
fruits = {"apple", "orange", "banana", "coconut", "banana", "apple"}
#unordered and immutable. does not allow duplicates. you can add and remove but u cant change a value

print(fruits)
#This appears in a different order each time u run the code cuz a set is unordered

print(dir(fruits))
# print(help(fruits))

# print(len(fruits)) returns 4 cause it discards duplicate values

# print("apple" in fruits) checks if an element(apple) is found in fruits

# print(fruits[0]) This doesnt work cause order changes and then
# u cant change the value cause order changes too

#But you can add to a set
# fruits.add("pineapple")

# fruits.remove("apple")
#removes the element named there

# fruits.pop()
#This removes the first element, but it is in a random order since the order changes

# fruits.clear()
# removes all the elements inside the set


print(fruits)