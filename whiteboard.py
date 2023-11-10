# Given an array of integers, find the one that appears an odd number of times.

# There will always be only one integer that appears an odd number of times.

# Examples
# [7] should return 7, because it occurs 1 time (which is odd).
# [0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
# [1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).
# constraints: 
# cannot use .count()

# count = 0
# for loop to pick only odd occurencies and add to count
# return the element


def solution(nums):
    count = {}
    for n in nums:
        if n not in count:
            count[n] = 1
        else:
            count[n] += 1
    for k,v in count.items():
        if v %2 != 0:
            return v
            
def solution(arr):
    odd_count = 0
    num_count = {}
    for num in arr:
        if num not in num_count:
            num_count[num] = 1
        else:
            num_count[num] += 1
    for key, value in num_count.items():
        if value % 2 !=0:
            return key
        
def solution(nums):
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
    for num, val in count.items():
        if val % 2:
            return num
            
