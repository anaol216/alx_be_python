# polymorphism_demo.py

import math

class Shape:
    """
    Base class for all geometric shapes.
    Defines the area() interface that all derived classes must implement.
    """
    def area(self):
        """
        Raises an error to enforce method overriding in subclasses.
        """
        raise NotImplementedError("Subclasses must implement the 'area()' method.")

class Rectangle(Shape):
    """
    Derived class for a rectangle, inheriting from Shape.
    """
    def __init__(self, length, width):
        """Initializes the rectangle's dimensions."""
        self.length = length
        self.width = width

    def area(self):
        """
        Overrides the area() method to calculate the rectangle's area.
        Formula: length * width
        """
        return self.length * self.width

class Circle(Shape):
    """
    Derived class for a circle, inheriting from Shape.
    """
    def __init__(self, radius):
        """Initializes the circle's radius."""
        self.radius = radius

    def area(self):
        """
        Overrides the area() method to calculate the circle's area.
        Formula: pi * radius^2
        """
        return math.pi * (self.radius ** 2)

# End of polymorphism_demo.py