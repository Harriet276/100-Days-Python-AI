## Day 17: Queues & Heaps ##
import heapq
from collections import deque, Counter


#  Practice Questions: Queue Practice.
# Build a queue that simulates customers in line at a bank. Enqueue 5 names, dequeue 2, then print the queue.

def QueueBank():
    bankLine = deque()
    bankLine.append("Harold")
    bankLine.append("Elizabeth")
    bankLine.append("Meera")
    bankLine.append("Reddington")
    bankLine.append("Kingmaker")

    bankLine.popleft()
    bankLine.popleft()
    print(bankLine)




QueueBank()



#Practice Question #2: Heap Practice.
# Use a heap to keep track of the smallest 3 numbers from a list of 10 random numbers.

def HeapImplementation( list):
    heapq.heapify(list)
    sorted_list = []
    count =0
    while count <= 2:
        sorted_list.append(heapq.heappop(list))
        count += 1
    print(sorted_list)
    print(list)

nums = [10,2,9,8,7,56,1,21,34,0]
HeapImplementation(nums)

#Top K Frequent Elements (Advanced):
# Given an array of integers, return the k most frequent elements using heapq
def topFrequentNums(nums, k):
    count = Counter(nums) # returns {nums:Frequency}
    return heapq.nlargest(k,count.keys(),  key=count.get)

nums = [1,1,1,2,2,3]
listy = []
listy =topFrequentNums(nums, 2)
print(listy)




