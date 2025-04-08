"""
Classes allow you to create user-defined data structures.
Classes define functions called methods, which identify the behaviors and actions that
an object created from the class can perform with its data.

While the class is the blueprint, an instance is an object
that’s built from a class and contains real data
"""

class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

"""
You define the properties that all Dog objects must have in a method called .__init__()
"""