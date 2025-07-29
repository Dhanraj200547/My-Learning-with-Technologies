def CheckSorted(nums):
    count = 0
    for i in range(len(nums)):
        if nums[i] > nums[(i+1) % len(nums)]:
            count += 1
    
    return count <= 1

nums = [2,1,3,4]
print(CheckSorted(nums))