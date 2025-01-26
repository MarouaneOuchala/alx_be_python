import math

# Base Class
class Shape:
    def area(self):
        raise NotImplementedError("Derived classes must implement the area method")

# Derived Class - Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Derived Class - Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)
# Correct output
for shape in shapes:
    if isinstance(shape, Rectangle):
        print(f"The area of the Rectangle is: {int(shape.area())}")
    elif isinstance(shape, Circle):
        print(f"The area of the Circle is: {shape.area()}")
