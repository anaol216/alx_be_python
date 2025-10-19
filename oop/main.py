# main.py (Provided for Testing)

from polymorphism_demo import Shape, Rectangle, Circle
import math

def main():
    # Create a list containing different shape objects
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    # Iterate through the list and call area() on each object
    for shape in shapes:
        # The same method call (shape.area()) produces different results
        # based on the object's class (Polymorphism)
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

if __name__ == "__main__":
    main()