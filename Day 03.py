# Create a list of numbers. Ask the user for a number. Check:

# If it exists in the list.

# Its index if it does.

# Append it if it doesn’t exist.
from operator import index


def checknum(num, list):
    index = 0
    for i in range(len(list)):
       if  list[i] == num:
           index = i
           break

    if index != 0:
        print("Num is in the list at index " + str(index))
    else:
        print("Num is not there, appending it to the list")
        list.append(num)
        print(list)


list = [1,22,56,78,98,9,80,76,4,21,45,67,87,90,2,1]
num= int(input("Enter number: "))
checknum(num,list)

# Even & Odd Sorter
# Ask the user to enter 10 numbers. Store them in a list. Create two new lists: one with even numbers, one with odd.

def evenodd ():
    even = []
    odd = []
    for i in range(10):
        num = int(input("Enter a numer: "))
        if num%2 == 0:
            even.append(num)
        else:
            odd.append(num)
    # even.pop(0)
    # odd.pop(0)
    print( "Even list" + str(even))
    print("odd list" + str(odd))

evenodd()

# Min, Max, Sum, Average
# Write a function that receives a list of numbers and returns:
# Minimum
# Maximum
# Sum
# Average

def evaluationfunc(list):
    print("The sum of the list is: " + str(sum(list)))
    print("The average of the list: " + str((sum(list)/len(list))))
    list.sort()
    print("The maximum is: " + str(list[len(list)-1]))
    print("the minimum is: " + str(list[0]))

# list = [23,45,67,90,87,1,0,78,90,88]
# evaluationfunc(list)

# Tuple to List Conversion
# Given a tuple of student names, convert it to a list, add two new names, and convert it back to a tuple.

def tupleToListandBack(student_tuple):
    mylist = list(student_tuple)
    for i in range(2):
        name= input("Enter student name: ")
        mylist.append(name)

    student_tuple = tuple(mylist)
    print(student_tuple)



my_tuple = ('Harriet', 'Bob', 'Peter', 'Hellen', 'Hannah', 'Rose', 'Godfrey')
tupleToListandBack(my_tuple)

                                  ###LeetCode Question###

###MergeSortedArrays###

###Problem Description###

# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.


def MergeSortedArrays(nums1,nums2,m,n):
    for i in range(n):
        nums1[m + i] = nums2[i]


    nums1.sort()
    print(nums1)


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
MergeSortedArrays(nums1,nums2,m,n)


