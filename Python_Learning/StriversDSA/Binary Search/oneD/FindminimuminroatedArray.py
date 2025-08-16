def findMin(nums):
        start = 0
        end = len(nums) - 1
        if nums[start] <= nums[end]:
            return nums[start]
        while(start <= end):
            mid = (start + end)//2
            if mid < len(nums)-1 and nums[mid] > nums[mid + 1]:                 #find pivot thats the minimum
                return nums[mid + 1]
            if mid > start and nums[mid] < nums[mid - 1]:
                return nums[mid]
            if nums[mid] >= nums[start]:
                start = mid + 1
            else:
                end = mid - 1
        return 0

nums = [11,13,15,17]
print(findMin(nums))