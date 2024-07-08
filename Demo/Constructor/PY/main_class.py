# A constructor is a special type of function that is used to create new objects.
# It's like a blueprint that defines the initial state of the object.
# self is a special parameter used within classes to refer to the current object instance.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Hello, my name is", self.name, "and I'm", self.age, "years old.")


person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

person1.display()
person2.display()
