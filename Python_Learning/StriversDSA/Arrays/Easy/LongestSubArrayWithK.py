'''
BruteForce Approach 
def longestSubarray(nums, k):
    arr = []
    n = len(nums)
    i = 0
    j = 0
    while(i < n):
        sum = 0
        while (sum <= k and j < n):
            sum += nums[j]
            if sum == k:
                arr.append(j-i+1)
            j += 1
        i += 1
        j = i
    
    return max(arr) if arr else 0
'''
def longestSubarray(nums,k):                #Optimized approach 
    prefix_sum = 0
    max_len = 0
    prefix_map = {}

    for i in range(len(nums)):
        prefix_sum += nums[i]

        if prefix_sum == k:
            max_len = i + 1

        if (prefix_sum - k) in prefix_map:
            max_len = max(max_len, i - prefix_map[prefix_sum - k])

        if prefix_sum not in prefix_map:
            prefix_map[prefix_sum] = i

    return max_len

nums = [2,3,5,1,9]
k = 10
print(longestSubarray(nums,k))