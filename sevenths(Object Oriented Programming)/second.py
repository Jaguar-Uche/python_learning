from objects import Dog
from objects import Cat
from objects import Mouse
from objects import Animal
# Inheritance - inheriting the attributs and methods from another class

dog1 = Dog("Scooby")
cat1 = Cat("Garfield")
mouse1 = Mouse("Mickey")

print(dog1.name)
print(dog1.is_alive)
print(cat1.name)
print(cat1.is_alive)
print(mouse1.name)
print(mouse1.is_alive)

dog1.eat()
cat1.sleep()
mouse1.eat()

dog1.speak()
cat1.speak()
mouse1.speak()

# Multiple and Multi-Level Inheritance

# Multiple Inheritance - When a child class inherits from more than one parent class
# Multi-Level Inheritance - Inheriting from a parent which inherits from another parent

from objects import Rabbit,Hawk,Fish

rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("NEMO")

rabbit.flee()
hawk.hunt()
fish.flee()
# Fish is both a prey and predator,multiple inheritance
fish.hunt()

# All animals can eat, sleep - Multi-Level Inheritance

rabbit.eat()
hawk.sleep()

