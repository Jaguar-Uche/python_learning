from objects import Shirts,Circle,Square,Triangle,Notebook,Textbook,AssignmentBook,Teachersbook

new_shirt = Shirts("Alex")
new_shirt.display()

circle = Circle("red", True,5)
print(f"A {circle.color} circle that has a radius of {circle.radius}cm is {circle.filled} filled")

square = Square("blue",False,10 )
print(f"A {square.color} square that has a width of {square.width}cm is {circle.filled} filled")

triangle = Triangle("Yellow",True,7,8)
print(f"A {triangle.color} triangle that has a height of {triangle.height}cm and width of {triangle.width}cm is {triangle.filled} filled")

circle.describe()

# Polymorphism by inheritance

book1 = Notebook(1)
# book1 is a Notebook and a book

books = [Notebook(4), Textbook(2), AssignmentBook(3), Teachersbook(6)]

for book in books:
    book.read_pages()
    print("This is the end")


# Polymorphism by duck typing

# Objects can be treated as if they are a different type as long as they meet the necessary attributes/method requirements

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("WOOF")

class Cat(Animal):
    def speak(self):
        print("MEOW")

class Car:
    alive = False
    def speak(self):
        print("HONK")

animals = [Dog(), Cat(), Car()]
for animal in animals:
    animal.speak()
    print(animal.alive)