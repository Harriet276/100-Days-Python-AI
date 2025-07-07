from datetime import datetime
# Write a Python program that asks the user for their name, age, and if they are a student, and then prints a short bio.
name = input("Enter your name: ")
age = int(input("Enter your age:"))
is_student = input("Are you a student ? (Yes/No) :")
print("Hi my name is " + name+ " i am " +str(age)  + " years old. \n Student status:" + is_student)

#Practice Question###

# Create a program that:
# Stores your birth year and current year in variables
# Calculates and prints your age
# Displays whether you are older than 18
# Bonus: Use an f-string for clean output.

birth_year= int(input("What is you birth year: "))
current_year =  int(datetime.now().year)
current_age = int(current_year - birth_year)
if current_age > 18 : print(current_age)
else:print(f"you are younger than 18!" + current_age)






###TwoSums LeetCode###

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.
# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
#


def twoSums(self, nums,target):
    for i in range(len(nums)):
            x = target - nums[i]
            for j in range(i+1, len(nums)):
                if x == nums[j]:
                    self[0]= i
                    self[1] = j
                    return self

    return [] #when no pair is found

nums1= [20,31,2,33,7,10,13]
target1 = 15
self1 = []
self1= twoSums(self1,nums1,target1)
print(self1)