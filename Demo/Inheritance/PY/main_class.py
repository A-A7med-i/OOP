# Inheritance is a fundamental concept in object-oriented programming (OOP)
# that lets you create new classes based on existing ones.
# The derived class "is-a" kind of the base class.

from Example1.high_student import HighStudent
from Example1.student import Student
from Example2.type import TypeOne


if __name__ == "__main__":

    s1 = Student("Ahmed", 20, 3.5, "Computer Science")
    s1.display()  # Output:
    # From Person
    # From Student
    # Hello, my name is Ahmed and I'm 20 years old.
    # Your GPA is: 3.5 and Your department is: Computer Science

    s2 = HighStudent("Alice", 18, 4.0, "Mathematics", "Number Theory")
    s2.display()  # Output:
    # From Person
    # From Student
    # Hello, my name is Alice and I'm 18 years old.
    # Your GPA is: 4.0 and Your department is: Mathematics
    # Research is: Number Theory

    # Example2
    d1 = TypeOne("Dog", 2, "bones", 5.00, "Babse")
    d1.display()  # Output:
    # Type is: Dog and age: 2
    # Type of eat is: bones and price is: 5.0
    # The name is: Babse
