from Example1.circle import Circle
from Example1.square import Square


# In object-oriented programming (OOP), an abstract class is a special kind of class
# that serves as a blueprint for derived classes but cannot be directly
# instantiated (used to create objects) itself.
# Abstract Methods: Abstract classes contain one or more methods declared without a definition (implementation).
# These methods are called abstract methods or pure virtual functions (in C++).
# Inheritance: Derived classes inherit from an abstract class to gain access to its non-abstract methods and attributes.

if __name__ == "__main__":
    # Create a Circle object
    circle1 = Circle(5.0)

    # Create a Square object
    square1 = Square(3.0)

    square1.display()

    print(circle1.get_area())
    print(square1.get_area())
