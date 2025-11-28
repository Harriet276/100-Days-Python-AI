#Day 22 – NumPy Slicing, Indexing & Image Manipulation
import numpy as np
import matplotlib.pyplot as plt
from numpy.matrixlib.defmatrix import matrix

#Practice Question #1

#Load an image, convert it to grayscale, crop the center 100×100 region, and save it.

# Q1: Submatrix Extraction
# Given a 6x6 NumPy array filled with values from 1 to 36, extract a submatrix containing:
# Rows: 2nd to 4th (inclusive)
# Columns: 3rd to 5th (inclusive)

arr = np.arange(1,37).reshape(6,6)
print(arr)
subarr= arr[1:4, 2:5]
print(subarr)


# Q2: Grayscale Conversion
# Given a color image loaded using matplotlib.pyplot.imread('image.jpg') (shape: (H, W, 3)),
# convert it to grayscale by averaging the RGB channels.
# Input: img as a NumPy array of shape (H, W, 3)
# Output: A new array of shape (H, W) with dtype uint8
# Your Task:
# Average the 3rd axis (RGB channels)
# Convert result to np.uint8
# Bonus: Plot the grayscale image using matplotlib.pyplot.imshow(gray, cmap='gray')
img = plt.imread('image.jpg')
cropped = img[100:300, 150:350]





## Question 3
# Write a function that:
# Accepts a 2D NumPy array (arr)
# Flips it horizontally (axis=1)
# Compares the original and flipped versions to find how many values remain unchanged (i.e., symmetric columns)

def count_symmetric_rows(arr):
    copy_arr = arr
    flip_h = np.flip(arr, axis=1)
    count = 0
    mask = (arr == flip_h)
    return np.sum(np.all(mask,axis=1))



arr = np.array([
    [1, 2, 1],
    [3, 3, 3],
    [4, 5, 6],
    [7, 8, 7]
])
result = count_symmetric_rows(arr)
print(result)