#Day 23 – NumPy Matrix Operations & Broadcasting
import numpy as np

# Q1: Dot Product Check
# Create two matrices A (2x3) and B (3x2). Compute:
# A dot B
# B dot A
# Verify the resulting shapes.
# Which one is valid? Why?

arr= np.array([[2,4,5],
              [6,7,8]])

arr2= np.arange(1,7).reshape(3,2)
arr3 = []
print(np.dot(arr,arr2))
print("      ")
print(np.dot(arr2,arr))
print("      ")

# Q2: Broadcasting with Scalars
# Given a 3x3 matrix:
#
# M = np.array([[1,2,3],
#               [4,5,6],
#               [7,8,9]])
#
# Add 10 to every element using broadcasting.
# Multiply each row by [1,2,3] using broadcasting.

M = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
M_plus_10 = M +10
print(M_plus_10)
row_multiplier = np.array([1,2,3])
scaled = M * row_multiplier
print("      ")
print(scaled)
print("    ")

# Q3: Row Normalization
# For a 2D NumPy array, normalize each row so its sum equals 1 (hint: divide each row by row.sum(axis=1, keepdims=True)).

arr= np.array([[2,4,5],
              [6,7,8]])
sumArr = arr.sum(axis=1,keepdims=True)
normalized = arr/sumArr
print(normalized)
