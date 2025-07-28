## Day 13: Generators & Iterators
#Small Coding Task
#Create a generator that yields all even numbers up to n

def evenNumbers(n):
    count = 0
    while count <= n:
        if count%2 == 0:
            yield count

        count+=1

#Build a generator that yields only vowels from a string.

def vowelsOnly(string):
    # List = list(string)
    vowels = "aeiouAEIOU"
    for char in string:
        if char  in vowels :
            yield char


#Create an iterator class that returns squares of numbers up to a limit.

class counter:
    def __init__(self, num, start):
        self.num = num
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.num:
            raise  StopIteration
        else:
            square = self.current**2
            self.current += 1
            return  square

#Write a generator to yield every 2nd character in a string.

def secondCharacter(string):
    for i in range(1, len(string),2):
        yield  string[i]





###LeetCode Question ###
# You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists.
# Implement an iterator to flatten it.
# NestedIterator(List<NestedInteger> nestedList) Initializes the iterator with the nested list nestedList.
# int next() Returns the next integer in the nested list.
# boolean hasNext() Returns true if there are still some integers in the nested list and false otherwise.

# Your code will be tested with the following pseudocode:

# initialize iterator with nestedList
# res = []
# while iterator.hasNext()
#     append iterator.next() to the end of res
# return res

# If res matches the expected flattened list, then your code will be judged as correct.




