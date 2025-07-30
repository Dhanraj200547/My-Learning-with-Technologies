def longestSubarray(nums, k):
    maxLen = 0
    for i in range(len(nums)):
        sum = 0
        for j in range(i,len(nums)):
            sum += j
            