# Day 15: Lambda Functions & Functional Tools (map, filter, reduce)
from functools import reduce

## Practice Questions #1 ##

#Create a list of squared even numbers from 1 to 20 using filter and map
nums = range(1,21)
list_Map = list(map(lambda x: x**2 ,filter(lambda x:x%2 == 0, nums)))

#Practice Question #2 ##
#Lambda + map: Given a list of prices, increase each by 10%
prices = range(1,31)
increase_price = list(map(lambda x: x +(x*10/100), nums))
print(increase_price)


#Practice Question #3 ##
#Lambda + filter: From a list of words, keep only those longer than 4 characters
words = ["aasa", "asa", "asas", "ab", "awawdxs", "aawawaa", "aawaap", "aaaawa", "aawapapa"]
wordsPrice = list(filter(lambda x: len(x) >= 4, words))
print(wordsPrice)


#Practice Question #4 ##
#Lambda + reduce: From a list of integers, find the sum of only the even ones
nums = [1,2,3,4,5,6,7,8,11,12,13,14,15]
integer_filter = reduce(lambda acc, x: acc + x, filter(lambda x: x %2 == 0, nums))


