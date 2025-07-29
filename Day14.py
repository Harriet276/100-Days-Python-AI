# Day 14: List and Dictionary Comprehensions in Python

##Practice Question #1
#Create a list of the squares of all even numbers between 1 and 20 using a one-liner.

even_squares= [x**2 for x in range(21) if x %2 ==0]
print(even_squares)

#List comprehension: Extract all vowels from a string.
input_string = "asrbdbfxjasuidu;ieoaeioaaaauaeioawq"
vowels = [char for char in input_string if char in "aeiouAEIOU"]
print(vowels)

#List comprehension: Given a list of numbers, return a list of "even" or "odd" labels.

num = [1,21,31,20,40]
even_odds = ["even" if x %2 == 0 else "odd" for x in num]

#Dictionary comprehension: Create a dictionary with numbers and their cubes from 1 to 10
cubes = {x:x**3 for x in range(1,11)}
