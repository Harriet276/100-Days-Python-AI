### Day 11 : Inheritance & Polymorphism in Python ###
import self


# Topics Covered:

# What is inheritance?
# The super() function
# Method overriding
# What is polymorphism?
# Abstract base classes (via abc)
# OOP Design: Animal Hierarchy

# Day 11 Practice Tasks: Small Coding Task

# Build a class Animal with a method speak()
# Subclass: Dog, Cat, Bird, each with custom speak() behavior
# Use a list of animals and loop through to call .speak() (polymorphism)
#

class Animal:
    def __init__(self, name):
        self.name = name
        def speak(self):
            return f"{name} speaks!"

class Dog(Animal):
    def speak(self):
        return f"{self.name} says woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says meow!"

class Bird(Animal):
    def __init__(self, name,canFly= True):
        super().__init__(name)
        self.canFly = canFly

    def speak(self):
        return f"{self.name} says cuckoo!"

animals = [Dog("Rex"), Cat("Misty"),Bird("cuckoo")]

for animal in animals:
    print(animal.speak())