# def longestConsecutive(nums):
#     if not nums:
#         return 0
#     nums = list(set(nums))
#     nums.sort()
#     maxlength = 1
#     i = 0
#     j = 1
#     while(j < len(nums)):
#         if nums[j-1] == nums[j] - 1:              #Bruteforece approach
#             j += 1
#             maxlength = max(maxlength,j-i)
#         else:
#             i = j
#             j += 1
#     return maxlength
def longestConsecutive(nums):
    nums = set(nums)
    longest = 0
    for num in nums:
        if num -1 not in nums:
            current = num                           #although it has an inner loop why does it not considered as O(n^2)
            length = 1                              #
            while current + 1 in nums:
                current+=1
                length+=1
            longest = max(length,longest)
    
    return longest
    """
    Building the set: O(n)

Looping through set: O(n)

Inner while loop runs at most n times total across all elements
(Each number is part of only one sequence start)

Total Time: O(n)

"""
nums = [1,2,3,4,100,200]
print(longestConsecutive(nums))
