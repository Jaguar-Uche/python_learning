# 2d Lists
# A grid or matrix of data

fruits =     ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats =      ["chicken", "fish", "turkey"]

fruits_two = {"apple", "orange", "banana", "coconut"}
vegetables_two = {"celery", "carrots", "potatoes"}
meats_two = {"chicken", "fish", "turkey"}

fruits_three = ("apple", "orange", "banana", "coconut")
vegetables_three = ("celery", "carrots", "potatoes")
meats_three = ("chicken", "fish", "turkey")

groceries = [fruits, vegetables, meats]
# a list of lists

groceries_two = [fruits_two, vegetables_two, meats_two]
# A list of sets

groceries_three = [fruits_three, vegetables_three, meats_three]
# A list of tuples

groceries_four = (fruits_three, vegetables_three, meats_three)
# A tuple of tuples

groceries_five = (fruits_two, vegetables_two, meats_two)
# A tuple of sets

# groceries = [
#              ["apple", "orange", "banana", "coconut"],
#              ["celery", "carrots", "potatoes"],
#              ["chicken", "fish", "turkey"]
#             ]  You can list everything out explicitly

# print(groceries[0]) -prints the first element(the first list)
# print(groceries[1][1]) - accessing an element in the list u need to access the first list
# and then the coordinates inside the list
for collection in groceries:
    for element in collection:
        print(element, end=" ")
    print()
# This prints the elements inside each collection(nested loop)
print(groceries)

#Num Pad
first_Row = (1, 2, 3)
second_Row = (4, 5, 6)
third_Row = (7, 8, 9)
fourth_Row = ("*", 0, "#")
calculator_layout = (first_Row, second_Row, third_Row, fourth_Row)

for collection in calculator_layout:
    for number in collection:
        print(number, end=" ")
    print()