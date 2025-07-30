def findMaxConsecutiveOnes(nums):
    maxCount = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            count = 0
            for j in range(i,len(nums)):
                if nums[j] == 1:
                    count += 1
                else:
                    break
            if count > maxCount:
                maxCount = count
    return maxCount

#Optimized Approach
"""
maxcount = 0
        count = 0
        for i in nums:
            if i == 1:
                count += 1
                maxcount = max(count,maxcount)
            else:
                count = 0
        
        return maxcount
"""
nums = [1,0,1,1,0,1]
print(findMaxConsecutiveOnes(nums))