# Polymorphism is a fancy term in programming that means "many forms."
# It allows you to treat objects of different classes in a similar way,
# even though they may have different underlying implementations.
# 1- Method Overriding
# There are a few reasons why Python doesn't support function overloading
# in the strict sense that languages like C++ do:
# Dynamic Typing: Python is a dynamically typed language.
# This means the data type of a variable is determined at runtime,
# not during compilation. This flexibility makes function overloading,
# which relies on static type checking, less straightforward in Python.


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Making animal sound...")


class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow!")


class Dog(Animal):
    def speak(self):
        print(f"{self.name} says Woof!")


d = Dog("Fido")

c = Cat("Whiskers")

d.speak()

c.speak()
