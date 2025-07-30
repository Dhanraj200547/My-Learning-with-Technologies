def missingNumber(nums):
    sum = 0
    for i in nums:
        sum += i
    
    return (len(nums) * (len(nums) + 1)) / 2 - sum

nums = [9,6,4,2,3,5,7,0,1]
print(missingNumber(nums))