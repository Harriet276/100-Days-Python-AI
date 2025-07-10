              ### Day 4: Dictionaries and Sets in Python ###

# Character Frequency Counter
# Input a string, count how many times each character appears using a dictionary.


def dictionary(input_string):
    char = {}
    for i in range(len(input_string)):
        current_char = input_string[i]
        if current_char in char:
            char[current_char] =+ 1
        else:
            char[current_char] = 1

    print(char)


dictionary("hello")

# Common Items in Two Lists
# Write a function to find and return the common elements using sets.

def commonItem(a, b):
    return list(set(a) & set(b))

a = [1,2,3,4,5,6]
b = [4,5,6,7,8,9,1]
c = []
c = commonItem(a,b)
print(c)

# Dictionary Sorter
# Given a dictionary of items and prices, return a list of items sorted by price.
def dictionarySorter(dictionary):
    sorted_prices = sorted(dictionary.items(),key= lambda x: x[1])
    print(sorted_prices)



items_prices = {
    "Milk": 4.50,
    "Bread": 2.00,
    "Eggs": 3.20,
    "Butter": 5.00,
    "Cheese": 6.80,
    "Apples": 2.50,
    "Chicken": 9.75,
    "Rice": 3.00,
    "Yogurt": 1.25,
    "Oranges": 3.00
}
dictionarySorter(items_prices)

###HackerRank Question###

# You are given  words. Some words may repeat. For each word, output its number of occurrences.
# The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification.

#Sample Input
# 4
# bcdef
# abcdefg
# bcde
# bcdef

# Sample Output
# 3
# 2 1 1

# Explanation
# There are  distinct words. Here, "bcdef" appears twice in the input at the first and last positions.
# The other words appear once each. The order of the first appearances are "bcdef", "abcdefg" and "bcde" which corresponds to the output.
# Note: Each input line ends with a "\n" character.

def wordSearch():
     n = int(input())
     word_count = {}
     for i in range (n):
         word= input().strip()
         if word in word_count:
             word_count[word] += 1
         else:
             word_count[word] = 1


     print(len(word_count))
     print(''.join(str(count) for count in word_count.values()))

wordSearch()
