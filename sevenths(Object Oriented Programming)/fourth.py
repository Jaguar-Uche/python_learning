# Static Methods in python

# static methods - A method that belongs to a class rather than any object from the class
# instance methods - Used for operations on instances of the class
# Static methods - Used on utility functions that don't need access to class data

class Employee:
    def __init__(self,name,position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier","Cook" ,"Janitor"]
        return position in valid_positions
            # Static Methods don't have self as the first parameter because they don't belong to a particular object



employee1 = Employee("Eugene","Manager")
employee2 = Employee("Squidward","Cashier")
employee3 = Employee("Spongebob", "Cook")

print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())

# Class Method

class Student:
    count = 0
    total_gpa = 0.0
    def __init__(self,name,gpa):
        self.name = name
        self.gpa = gpa
        Student.count +=1
        Student.total_gpa += gpa

    # This is an instance method
    def get_info(self):
        return f"{self.name} : {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"Total number of students : {cls.count}"

    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"The Average GPA is {cls.total_gpa/cls.count:.2f}"

print(Student.get_count())

student1 = Student("Spongebob", 3.2)
stdent2 = Student("Patrick", 2.0)
student3 = Student("Sandy", 4.0)

print(Student.get_count())
print(Student.get_average_gpa())

# Magic Methods - Dunder Methods
# They are automatically called by python's built-in operations

class Book:

    @classmethod
    def current_book(cls,title):
        cls.title = title

    def __init__(self,title, author,num_pages):
        Book.current_book(title)
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __eq__(self,other):
        return self.title == other.title and self.author == other.author

    def __lt__(self,other):
        return self.num_pages < other.num_pages

    def __gt__(self,other):
        return self.num_pages > other.num_pages

    def __add__(self,other):
        return f"{self.num_pages + other.num_pages} pages"

    def __contains__(self,keyword):
        return keyword in self.title or keyword in self.author

    def __getitem__(self,keyword):
        if keyword == "title":
            return self.title
        elif keyword == "author":
            return self.author
        elif keyword == "num_pages":
            return self.num_pages
        else:
            return f"'{keyword}' not found"


book1 = Book("The Hobbit",'J.R.R. Tolken',310)
book2 = Book("Harry Potter and the philosopher's Stone", "J.K. Rowling", 223)
book3 = Book("The Lion, The Witch and The Wardrobe", "C.S. Lewis", 172)
book4 = Book("Harry Potter and the philosopher's Stone", "J.K. Rowling", 200)


# print(book1) This prints a memory address
# customize this behaviour using the __str__ method and make it return something else

print(book1)
# print(book1 == book4)
# Maybe cause of the memory address, so you customize it using __eq__
print(book2 == book4)
print(book3 == book4)
# print(book2 > book4)
# Normally you can't do logical operations on class instances
# print(book3<book4)
# But you customize for less than with lt and greater than with gt

print(book2 > book4)

print(book3<book4)

print(book3 + book4)

# print("Lewis" in book3) shows error that it is not iterable
# Membership operators use __contains__

print("Lewis" in book3)


# print(book1["title"]) shows error that it is not subscriptable
print(book1["author"])
print(book2["title"])
print(book3["num_pages"])
print(book4["name"])