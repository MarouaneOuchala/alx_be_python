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
        return math.pi * self.radius**2

# Testing Polymorphism
shapes = [
    Rectangle(10, 5),  # Rectangle with length=10, width=5
    Circle(7),         # Circle with radius=7
]

for shape in shapes:
    print(f"The area of the {shape.__class__.__name__} is: {shape.area():.2f}")
