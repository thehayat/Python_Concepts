"""
Classes are the simple recipes that are used to create two
main things.

1. Provide a data Container
    i. Variables
    ii. Constants

2. Provide operations on the data
    i. Functions
    ii. Methods
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello, my name is {self.name}")


"""
Encapsulation

It refers to the bundling of data (attributes) and methods (functions) that operate on the data into a single unit or 
class, and restricting direct access to some of the object's components, which can prevent the accidental modification
of data.

Below are concepts of how encapsulation constitutes and works.
1.Class Definitions: 
A class is defined with attributes and methods. Attributes represent the state of an object, 
while methods represent the behavior.
"""

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self._speed = 0  # _speed is a protected attribute

    def accelerate(self):
        self._speed += 5

    def brake(self):
        self._speed -= 5

    def get_speed(self):
        return self._speed
