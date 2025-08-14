#Day 21 — NumPy Basics & Array Operations

#  Small Coding Task
# Create two NumPy arrays and:
# Add, subtract, multiply, and divide them.
# Calculate the mean and standard deviation.
# Reshape them into a 2x3 matrix.

import numpy as np
import random as randint

Array1 = np.array([2,3,4,5])
Array2 = np.array([6,7,8,9])
print(Array1 + Array2)
print(Array2 - Array1)
print(Array1 - Array2)
print(Array1 * Array2)
print(Array1 / Array2)
print(f"Array 1 mean{Array1.mean()}")
print(f"Array 2 mean{Array2.mean()}")
print(f"Array 2 standard deviation {Array2.std()}")
print(f"Array 1 standard deviation{Array1.std()}")
ReshapeArray1 = Array1.reshape(2,2)
print(ReshapeArray1)
ReshapeArray2 = Array2.reshape(2,2)
print(ReshapeArray2)

# Practice  Question #1
# Create a 5x5 matrix with random integers between 1 and 50 and find:
# Maximum value
# Minimum value
# Mean

array = np.random.randint(1,51, size = (5,5))
print(array)
max = array.max()
min = array.min()
mean = array.mean()
print( max, min, mean)

#Practice Question #2
# Given:
# arr = np.array([[1, 2, 3], [4, 5, 6]])
# Print the second column.
# Replace all values greater than 3 with 0.
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr[:,1])
arr[arr > 3] = 0

#Practice 3
#Generate an array of 10 evenly spaced numbers from 0 to 5, square them, and print the result.

array4 = np.linspace(0,5, 10)
for i in range(len(array4)):
    array4[i] = array4[i] * array4[i]

print(array4)



