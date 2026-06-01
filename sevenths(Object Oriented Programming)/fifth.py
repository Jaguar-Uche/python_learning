
# Property - decorator - allows us to define a method as a property. It can be accessed like an attribute
# When reading, writing or deleting attributes, you can add additional logic. It gives getter, setter and deleter method

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width:.1f}cm"

    @property
    def height(self):
        return f"{self._height:.1f}cm"

    @width.setter
    def width(self,new_width):
        if new_width > 0 :
            self._width = new_width
        else:
            print("Width must be greater than 0")

    @height.setter
    def height(self,new_height):
        if new_height > 0 :
            self._height = new_height
        else:
            print("Height must be greater than 0")


    @width.deleter
    def width(self):
        del self._width
        print("Width deleted")

    @height.deleter
    def height(self):
        del self._height
        print("Height deleted")

rectangle = Rectangle(380, 400)
rectangle.width = 6
rectangle.height = 7

print(rectangle.width)
print(rectangle.height)

del rectangle.width
del rectangle.height