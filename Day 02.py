import re
from traceback import print_tb

##Coding task##

# Write a Python program that takes your full name as input and returns:
# Your initials in uppercase
# Your name in title case
# The total number of characters excluding spaces


def namefunc(name):
    print(f"Title Case "+name.title())
    value= name.find(" ")
    if value == -1:
        initials = name[0].upper() + "."
        print(f"Initials"+ initials)
    else:
        print(f"Initials "+name[0].upper() + "."+ name[value+1].upper())

    total_characters = len(name.replace(" ", ""))
    print(f"The total number of characters are:" + str(total_characters))


name= input("Enter your full name: ")
namefunc(name)

##Coding task 2##
# Palindrome Checker
# Write a program to check if a given string is a palindrome (reads the same forward and backward).

def palindromeCheck(string,array):
    for i in range(len(string)):
        array[i] = string[len(string) - 1-i]

    if ''.join(array) == string:
        print("It is a valid palindrome")
    else:
        print("Not a palindrome")

string = input("Enter palindrome: ")
array=[None]*len(string)
palindromeCheck(string,array)


# ##Coding task 4##
# Word Reverser
# Take a sentence input from the user and print each word reversed but keep their order.
# Example: "Python is fun" - "nohtyP si nuf"

def wordreverser(string):
    array = [None]*len(string)
    for i in range(len(string)):
        array[i] = string[len(string) - 1-i]
    print(''.join(array))
string = input("Enter string: ")
wordreverser(string)


##Coding task 3##
# Vowel Counter
# Create a function that counts the number of vowels (a, e, i, o, u) in a given sentence.

def vowelCounter(string):
    count = 0
    for i in range(len(string)):
        if string[i].lower() in 'aeiou':
            count = count + 1

    print(f"The total number of vowel are: {count} " )
string = input("Enter a sentence: ")
vowelCounter(string)


###LeetCode Questions####
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters,
# it reads the same forward and backward. Alphanumeric characters include letters and numbers.


def isPalindrome( s):
    cleaned_text = re.sub(r'[^A-Za-z0-9]', '', s.lower())
    self = [None] * len(cleaned_text)
    for i in range(len(cleaned_text)):
        self[i] = cleaned_text[len(cleaned_text) -1 -i]

    if cleaned_text == "".join(self):
        return True
    else:
        return False


string = input("Enter a sentence: ")
self = [None]* len(string)
result = isPalindrome(string)
print(result)

