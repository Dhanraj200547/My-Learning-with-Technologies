# def maxSubArray(nums):
#     maxsum = float('-inf')
#     for i in range(len(nums)):
#         sum = 0
#         for j in range(i,len(nums)):
#             sum += nums[j]
#             maxsum = max(maxsum,sum)
    
#     return maxsum             #Bruteforce methid

def maxSubArray(nums):
    maxsum = float('-inf')
    sum = 0
    for i in nums:
        sum += i

        if sum > maxsum:
            maxsum = sum
        
        if sum < 0:
            sum = 0
    return maxsum
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))

def maxSubArrayprint(nums):
    maxsum = float('-inf')
    start , end = 0,0
    for i in range(len(nums)):
        sum = 0
        for j in range(i,len(nums)):
            sum += nums[j]
            if sum > maxsum:
                maxsum = max(maxsum,sum)
                start ,end = i ,j 
    return [start,end]

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArrayprint(nums))
    