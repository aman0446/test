from collections import defaultdict
from collections import Counter
import heapq


'''
Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to target.
Assume exactly one solution exists, and you may not use the same element twice.

nums = [2, 7, 11, 15]
target = 22


def two_sum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return(seen[diff], i)

        seen[num] = i

print(two_sum(nums, target))
'''

'''
Group Anagrams

Problem:
Given an array of strings strs, group the anagrams together. You can return the answer in any order

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

grouped_strs = defaultdict(list)
output = []

for word in strs:
    key = ''.join(sorted(word))
    grouped_strs[key].append(word)

for  value in grouped_strs.values():
    output.append(value)

print(output)

#improved implementation
grouped = defaultdict(list)

for word in strs:
    char_count = [0] * 26

    for c in word:
        char_count[ord(c) - ord('a')] += 1
    
    key = tuple(char_count)

    grouped[key].append(word)

print(list(grouped.values()))

'''

'''
Check if two strings are anagrams.


s = "anagram"
t = "nagaram"

def is_anagram(s, t):
    if len(s) != len(t):
        return False

    char_count = defaultdict(int)
    for c in s:
        char_count[c] += 1

    for c in t:
        if c in char_count:
            char_count[c] -= 1
        else:
            return False
    for v in char_count.values():
        if v != 0:
            return False
    return True


print(is_anagram(s,t)) 

'''

'''
Top K Frequent Elements

Problem:
Given an integer array nums and an integer k, return the k most frequent elements.



nums = [1, 1, 1, 2, 2, 3]
k = 2

freq_dict = defaultdict(int)

for num in nums:
    freq_dict[num] += 1

k_most_frequent = list(sorted(freq_dict.items(), key=lambda x:x[1], reverse= True))[:k]

print(k_most_frequent)
'''
'''
Longest Substring Without Repeating Characters

Problem:
Given a string s, find the length of the longest substring without repeating characters.

string = "arunk"

left =0 
right = 0
len_longest_substring = 0
seen = {}
for i,c in enumerate(string):
    if c in seen and i >= left: 
        left = seen[c] + 1    
    seen[c] = i
    len_longest_substring = max(len_longest_substring, i -left + 1)


print(len_longest_substring)

left = 0
seen = set()
longlen = 0 
for right in range(len(string)):
    
    while string[right] in seen:
        seen.remove(string[left])
        right +=1
    seen.add(string[right])

    longlen  = max(longlen, right -left +1)


print(longlen, seen)
'''
'''
maximum sum subarray 
'''
'''
nums = [2,1,5,1,3,9]
#prefix_sum = [2,3,8,9,12,14]
k = 3
maximum_sum = 0

prefix_sum = [0]
running_sum = 0
for num in nums:
    running_sum += num
    prefix_sum.append(running_sum) 

left =0 
right = k-1

while right < len(nums):
    current_sum = prefix_sum[right+1] - prefix_sum[left]
    maximum_sum = max(maximum_sum, current_sum)
    right+=1
    left+=1

print(maximum_sum)
'''
'''Minimum Size Subarray Sum

Problem:
Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0.
'''

'''
target = 7
nums = [2, 3, 1, 2, 4, 3]
left= 0
running_sum =0; 
window_length = float('inf') 
for right in range(len(nums)):
    running_sum += nums[right] 
    while running_sum >= target: 
        #print(running_sum)
        window_length = min(window_length, right - left +1 )
        #print("window_length : ", window_length)
        running_sum -= nums[left]
        left += 1

print(window_length)
'''

'''
Subarray Sum Equals K

Problem:
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals k.
'''
'''
#target = 7
#nums = [2, 3, 1, 2, 4, 3]
nums = [1, 1, 1]
target = 2
left = 0 
running_sum = 0
no_of_sa = 0
for right in range(len(nums)):
    running_sum += nums[right]
    while running_sum >= target:         
        if running_sum == target:
            no_of_sa +=1
        running_sum -= nums[left]
        left +=1    

print(no_of_sa)
'''

'''Kth Largest Element in an Array

Problem:
Given an integer array nums and an integer k, return the kth largest element in the array.
'''
'''
nums = [3, 2, 1, 5, 6, 4]
k = 2

import heapq 

heap = []

for num in nums:
    heapq.heappush(heap, num)
    if len(heap) > k:
        heapq.heappop(heap)

print(heap[0])
'''

'''
K Closest Points to Origin

Problem:
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).
'''
'''import heapq
points = [[1, 3], [-2, 2]]
k = 1
heap = []
for data in points:
    x,y= data[0], data[1]
    distance = (x*x) + (y*y)

    heapq.heappush(heap,(-distance,(x,y)))
    
    if len(heap) > k:
        heapq.heappop(heap)

print([data for _,d in heap])
'''
'''
Valid Parentheses

Problem:
Given a string s containing just the characters '(', ')', '{', '}', '[', and ']', determine if the input string is valid.

A string is valid if:
	•	Open brackets are closed by the same type of brackets.
	•	Open brackets are closed in the correct order.
	•	Every close bracket has a corresponding open bracket.
'''
'''
s = ")("
pairs = {'}' : '{' , ')' : '(' , ']' : '[' }

def is_valid(s):
    stack = []
    for c in s:
        if c in pairs:
            if stack and stack[len(stack) - 1] == pairs[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    if len(stack) == 0:
        return True
    else:
        return False

print(is_valid(s))
    
'''

#no of islands

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

rows = len(grid)
cols = len(grid[0])
no_of_islands = 0 

def dfs(r,c):
    if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0":
        return 
    #mark visited    
    grid[r][c] = "0" 

    dfs(r,c+1)
    dfs(r, c-1)
    dfs(r-1, c)
    dfs(r+1, c)

for i in range(rows):
    for j in range(cols):
        if grid[i][j] == "1":
            no_of_islands +=1
            dfs(i,j)

print(no_of_islands)




