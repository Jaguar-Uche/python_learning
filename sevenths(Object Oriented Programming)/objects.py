class Car :
    def __init__(self, model, year, color, for_sale=False):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You drive the {self.color} {self.model}")

    def stop(self):
        print(f"You stop the {self.color} {self.model}")

    def describe(self):
        print(f"{self.year} {self.color} {self.model}")

class Student:

    class_year = 2027
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

# Animal is a superclass
class Animal:
    def __init__(self,name):
        self.name = name
        self.is_alive = True
    def eat(self):
        print(f"{self.name} is eating.")
    def sleep(self):
        print(f"{self.name} is sleeping.")

# This is a subclass
class Dog(Animal):
    def speak(self):
        print("WOOF")

# This is a subclass
class Cat(Animal):
    def speak(self):
        print("MEOW")

# This is a subclass
class Mouse(Animal):
    def speak(self):
        print("SQUEAK")


class WildAnimals:
    def __init__(self,name):
        self.name = name
    def eat(self):
        print(f"{self.name.capitalize()} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Prey(WildAnimals):
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(WildAnimals):
    def hunt(self):
        print(f"{self.name} is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey,Predator):
    pass

class Properties:
    def __init__(self,owner):
        self.owner = owner

class MyProperties(Properties):
    # This cant have a constructor of its own
    pass

class Clothes:
    color = "red"

class Trouser:
    pass

class Shirts(Properties, Clothes):
    def display(self):
        print(f"{self.owner} owns a {self.color} Shirt")


# super is used in a child class to call methods from a parent class
# super() allows you to extend the functionality of the inherited methods

class Shape:
    def __init__(self,color,filled):
        self.color = color
        self.filled = filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.filled else 'not filled'}")

class Circle(Shape):
    def __init__(self,color,filled,radius):
        super().__init__(color, filled)
        self.radius = radius

    def describe(self):
        print(f"It is circle of area {3.14 * self.radius * self.radius}cm2")
#         If a child has same name with that of the parent, you would override the parent and use the child's own
        super().describe()

class Square(Shape):
    def __init__(self, color, filled, width):
        super().__init__(color, filled)
        self.width = width
    def describe(self):
        print(f"It is a square of area {self.width * self.width}cm2")
        super().describe()


class Triangle(Shape):
    def __init__(self, color, is_filled, width,height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    # When you want the filled property of a triangle, it is filled, not is_filled because it is named filled in the superclass
    def describe(self):
        print(f"It is a square of area {self.width * self.width}cm")
        super().describe()

# Polymorphism

from abc import ABC, abstractmethod
import time
class Book:
    @abstractmethod
    def read_pages(self):
        pass
#     I think abstractmethod means all the children must have it or stn

class Notebook(Book):
    def __init__(self,pages):
        self.pages = pages

    def read_pages(self):
        for x in range(1,self.pages+1):
            print(x)
            time.sleep(1)
class Textbook(Book):
    def __init__(self, pages):
        self.pages = pages
    def read_pages(self):
        for x in range(1,self.pages+1):
            print(x)
            time.sleep(2)

class AssignmentBook(Book):
    def __init__(self, pages):
        self.pages = pages
    def read_pages(self):
        for x in range(1,self.pages+1):
            print(x)
            time.sleep(0.5)

class Teachersbook(Textbook):
    def __init__(self,pages):
        super().__init__(pages)

