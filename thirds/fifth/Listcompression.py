# a concise way to create lists
# [expression for value in iterable if condition]

doubles = []

for num in range(1, 11):
    doubles.append(num * 2)

print(doubles)

doubles_compressed =[x*2 for x in range(1,11)]
# a simpler way of creating this in the list

print(doubles_compressed)

triples =[num*3 for num in range(1,11)]
print(triples)

squares = [num**2 for num in range(1,11)]
print(squares)

fruits = ["apple", "orange", "banana", "coconut"]

fruits = [fruit.upper() for fruit in fruits]
# you can just do fruits = [fruit.upper() for fruit in ["apple", "orange", "banana", "coconut"]]

fruits_char = [fruit[0] for fruit in fruits]
print(fruits)
print(fruits_char)

numbers = [1,-2,3,-4,5,-6,8,-7]

positive_numbers = [number for number in numbers if number >=0]
negative_numbers = [number for number in numbers if number <0]
even_numbers =[number for number in numbers if number % 2 == 0]
odd_numbers =[number for number in numbers if number % 2 == 1]
print(positive_numbers)
print(negative_numbers)
print(even_numbers)
print(odd_numbers)

grades =[85,42,79,90,56,61,30]

passing_grades = [grade for grade in grades if grade >= 60]
passing_grades.sort()
# i cant method chain this to the list compression cause it modifies the original list
print(passing_grades)