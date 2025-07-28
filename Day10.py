#### Day 10:  Object-Oriented Programming (OOP) Basics & Class Design

 # Topics Covered:

# What is Object-Oriented Programming?
# Creating Classes & Objects
# __init__() constructor
# Instance variables vs. class variables
# Adding methods to a class
# __str__() method for clean printing
# Small project: Student class with behavior

# Small Coding Task
# Create a Student class with:
# __init__() method
# A calculate_average() method (takes a list of marks)
# A method to check if the student is on the Dean's List (average >= 85)

class Student:
    def __init__(self, name, age,grade):
        self.name = name
        self.age = age
        self.grade = grade

    def calculate_Average(self):
        return sum(self.grade)/len(self.grade)



    def Dean_List(self):
        return self.calculate_Average() >= 85

