def findPeakElement(nums):
    s = 0
    e = len(nums) - 1
    while s + 1 < e:
        mid = (s+ e)//2
        if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
            return mid
        if nums[mid - 1] < nums[mid] < nums[mid + 1]:
            s = mid
        else:
            e = mid
    
    if nums[s] > nums[e]:
        return s
    else:
        return e
    
nums = [1,2,1,3,5,6,4]
print(nums[findPeakElement(nums)])