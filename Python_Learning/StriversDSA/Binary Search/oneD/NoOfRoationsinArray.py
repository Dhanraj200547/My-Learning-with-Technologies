def findMin(nums):
        start = 0
        end = len(nums) - 1
        if nums[start] <= nums[end]:
            return nums[start]
        while(start <= end):
            mid = (start + end)//2
            if mid < len(nums)-1 and nums[mid] > nums[mid + 1]:                 #find pivot thats the no of rotations
                return mid + 1
            if mid > start and nums[mid] < nums[mid - 1]:
                return mid
            if nums[mid] >= nums[start]:
                start = mid + 1
            else:
                end = mid - 1
        return 0

nums =  [4,5,6,7,0,1,2,3]
print(findMin(nums))