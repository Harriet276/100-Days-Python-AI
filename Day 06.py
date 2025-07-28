# Day 06: Functions in Python (User-defined and Built-in)

#Small coding task
# Write a Python function number_summary() that:
# Takes a list of numbers as input.
# Returns a dictionary containing:
# count
# sum
# average
# min
# max


def number_summary(numList):
    sum = sum(numList)
    average = 0
    dictionary = {
    "average"  :  sum / len(numList),
    "sum " : sum,
    "count" : len(numList),
    "min" : min(numList),
    "max" : max(numList)
    }

    return  dictionary


#Practice Question #1
#Write a function that accepts a string and returns the number of vowels in it.

def stringParser(string):
    string1 = []
    count =0
    string1= list(string)
    vowels = "aeiouAEIOU"
    for char in string:
        if char in vowels:
            count += 1

    print(f"There are {count} vowels")


str= "abcdefaeiou"
stringParser(str)

string = "abcdefg"
stringParser(string)

#Practice Question #2
# Create a function that checks if a number is prime.
def isPrime(num):
    i = 2
    while i <= num-1:
        if num % i != 0 :
            i+= 1
        else:
            print("Not a prime number")

    print("It's a prime number")

isPrime(7)

##Practice Question #3
#Write a function that accepts two lists and returns a dictionary using one list as keys and the other as values.
def returnDictionary( list1, list2):
    if len(list1) != len(list2):
        print("Error lists are not the same size")

    else:
        dictionary = dict(zip(list1, list2))
        return  dictionary

