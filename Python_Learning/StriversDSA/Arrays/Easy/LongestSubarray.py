
# Bruteforce Approach: 

def longestSubarray(nums, k):
    maxlen = 0
    for i in range(len(nums)):
        sum = 0
        for j in range(i,len(nums)):
            sum += nums[j]
            if sum == k:
                maxlen = max(maxlen , j -i + 1)
    return maxlen
    
nums =  [10, 5, 2, 7, 1, 9]
k = 15
print(longestSubarray(nums,k))
