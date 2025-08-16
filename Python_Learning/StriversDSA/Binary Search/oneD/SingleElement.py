def singleNonDuplicate(nums):
        start = 0
        end = len(nums) -1
        while(start < end):
            mid = 2 * ((start + end) // 4)
            if nums[mid] == nums[mid+1]:
                start = mid + 2
            else:
                end = mid
        return nums[start]
    
nums = [1,1,2,3,3,4,4,8,8]
print(singleNonDuplicate(nums))