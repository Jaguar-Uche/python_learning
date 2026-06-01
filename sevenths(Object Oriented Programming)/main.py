
# In Python, an object is a bundle of related attributes(variables) and methods(functions)
# You need a class to create objects

# A class is the blueprint used to design the structure and layout of an object

from objects import Car
from objects import Student

car1 = Car("Mustang", 2024,"red",False)
# print(car1) This prints the memory address of the car
car2= Car("Corvette", 2025,"blue",True)
car3= Car("Charger", 2026,"yellow",True)

# . is attribute access operator

print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)

car1.drive()

print(car2.model)
print(car2.year)
print(car2.color)
car2.stop()

print(car3.model)
print(car3.year)

car1.describe()
car2.describe()
car3.describe()

# Class Variables are shared among all instances of a class
# They are defined outside the constructor so all instances of the class can use them

# instance variables, each object has its own

student1 = Student("Spongebob", 30)
student2 = Student("Patrick", 35)
student3 = Student("Squidward", 55)
student4 = Student("Sandy", 27)

print(student1.name)
print(student1.age)
# print(student1.class_year) It is good practice to access the class year by the class name instead of the object_name
print(Student.class_year)
print(student2.name)
print(student2.age)
print(student2.class_year)
print(Student.num_students)
print()
print(f"My graduating class of {Student.class_year} has {Student.num_students} students")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)