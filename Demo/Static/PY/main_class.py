# 1. Static Data (Class Variables):
# Static data, also known as class variables, are variables defined at the class level.
# They are shared by all instances (objects) of the class.

# 2. Static Methods:
# They are typically used for utility functions that are related to the class
# but don't necessarily need to modify object state.


from Example1.count import Count
from Example2.math_helper import MathHelper
from Example3.my_class import MyClass


c1 = Count()
c2 = Count()
c3 = Count()

print(c3.get_count())


result = MathHelper.add(5, 3)
print(result)

result = MathHelper.multiply(5, 3)
print(result)


MyClass.static_method()


m1 = MyClass()
print(MyClass.count)


m2 = MyClass()
print(MyClass.get_count())
