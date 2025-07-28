##Day 07: Modules & Imports in Python (math, random)##
import math
from random import random


# Small Coding Task
# Create a simple quiz generator:
# Use random.choice() to select 2 random numbers between 1 and 10.
# Ask the user to calculate their sum.
# Use math.isclose() to check if the user’s answer is approximately correct (optional).
# Repeat this 5 times and give a final score.

def QuizGenerator():
    count = 0
    for i in range(5):
      num1 = random.randint(1,10)
      num2 = random.randint(1,10)
      num3 = float(input(f"Add these two numbers and give the result {num1} , {num2}: "))
      num3O = num1 + num2
      if math.isclose(num3,num3O) == True:
          print("correct\n")
          count+= 1

      else:
          print(f"false the correct answer is: {num3O}")
    print(f"The total score is: {count}/5")


##Practice Question #1
#Generate a list of 10 random integers between 50 and 100.

def generateList():
    list = []
    for i in range(10):
        list.append(random.randint(50,100))
    print( list)

##Practice Question #2
#Write a function to compute the area of a circle given radius using math.pi

def area(radius):
     pi = math.pi
     area = pi * radius
     print(f"The area of the circle is: {area}")

##Practice Question #3
#Simulate a dice roll using random.randint() (values from 1 to 6).

def dice_roll():
    while 1==1:
        input("Welcome to dice roll, press Enter to roll a dice: ")
        result = random.randint(0,6)
        print(f"Your result is: {result}")
        again= input("To continue playing enter 'y' else press any digit")
        if again != 'y':
            print("Thanks for playing")
            break

