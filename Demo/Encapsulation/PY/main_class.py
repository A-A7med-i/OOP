# Encapsulation is a fundamental principle in object-oriented programming (OOP)
# that focuses on bundling data (attributes) and
# the methods that operate on that data within a single unit called a class.
# Data Protection

from calculator import Calculator


calculator = Calculator(5, 2)


result = calculator.add()
print(f"Addition: {result}")

result = calculator.division()
print(f"Division: {result}")

calculator = Calculator(10, 0)
result = calculator.division()
print(result)
