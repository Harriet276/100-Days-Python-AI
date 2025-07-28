# Day 05: Loops and Conditional Statements in Python

# Small Coding Task
# Write a Python program that:
# Asks the user to enter a number between 1–20.
# If it’s even, print all even numbers from 0 up to that number using a for loop.
# If it’s odd, print all odd numbers up to that number using a while loop.
# If number is not in range, print "Out of range".


def EvenOrOdd():
    num = int(input("Enter a number between 1 -20: "))
    if num >= 0 and num <= 20:

        if num % 2 == 0:
            for i in range(num):
                if i % 2 == 0:
                    print(i)

        elif num % 2 != 0:
            count = 0
            while count <= num:
                if count % 2 != 0:
                    print(count)
                count += 1

    else:
        print("Number is out of range!")



#EvenOrOdd()

#Practice Question #1
# Write a program to print all numbers from 1 to 100 that are divisible by 3 or 5 (not both).
def function():
    count = 0
    while count <= 100:
        if (count % 3 == 0 and count % 5 != 0) or  (count % 3 != 0 and count % 5 == 0) :
            print(count)
        count += 1
#function()

#Practice Question #2
#Build a multiplication table (1 to 10) using nested for loops.
def fuction01():
    for i in range(11):
        for j in range(13):
            print(f"{i} * {j} = {i*j}")
#fuction01()


#Question #3
#Ask the user to input 5 numbers. Count how many were positive, negative, and zero.

def  function3():
    postive  =0
    negative = 0
    zero = 0
    for i in range(0,5):
        n = int(input("Please enter a number: "))
        if n > 0:
            postive+= 1
        elif  n < 0 :
            negative += 1

        else:
            zero += 1
    print(f"Positive: {postive} , negative {negative}, zero {zero}")

function3()