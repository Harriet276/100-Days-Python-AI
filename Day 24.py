##Day 24 – NumPy Statistics, Random, and Aggregations
import numpy as np
from numpy import random



# Q1: Weather Stats

# Create an array representing daily temperatures (°C) over a week:
# temps = np.array([28, 30, 29, 31, 27, 26, 32])
# Tasks:
# Calculate the mean, median, and standard deviation.
# What is the max temperature and which day did it occur?

def tempCalculations(arr):
    print(f"The mean temperature is " + str(np.mean(arr)))
    print(f"The median temperature is " + str(np.median(arr)))
    print(f"The standard deviation temperature is " + str(np.std(arr)))
    if np.argmax(arr) == 0:
        print("The max temperature is on Monday")
    elif np.argmax(arr) == 1:
        print("The max temperature is on Tuesday")
    elif np.argmax(arr) == 2:
        print("The max temperature is on Wednesday")
    elif np.argmax(arr) == 3:
        print("The max temperature is on Thursday")
    elif np.argmax(arr) == 4:
        print("The max temperature is on Friday")
    elif np.argmax(arr) == 5:
        print("The max temperature is on Saturday")
    elif np.argmax(arr) == 6:
        print("The max temperature is on Sunday")
        print("          ")


temps = np.array([28, 30, 29, 31, 27, 26, 32])
tempCalculations(temps)


# Q2: Cumulative Sales

# Create a NumPy array for sales: [120, 80, 90, 150, 200]
# Tasks:
# Calculate the cumulative sales (np.cumsum)
# Calculate total revenue
# What’s the average sale?

def cumulativeSales(arr):
    print(f"The cumulative sales are {np.cumsum(arr)}")
    print(f"The total revenue is {np.sum(arr)}")
    print(f"The average sale is {np.average(arr)}")
    print("        ")



sales = np.array([120, 80, 90, 150, 200])
cumulativeSales(sales)


# Q3: Simulate Student Marks

# Generate 100 students’ scores between 0 and 100 (integers):
# What is the highest score?
# What percentile is 90?
# How many students scored above the mean?

student_scores= np.array([random.randint(1,100)])
print(f"The highest score is {np.max(student_scores)}")
print(f"The 90th percentile  is {np.percentile(90, student_scores)}")

