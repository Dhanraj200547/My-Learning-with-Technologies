def searchInsert(nums, target):
        start = 0
        end = len(nums)-1
        if len(nums) == 1 and nums[0] == target:
            return 0 
        while(start <= end):
            mid = (start + end)// 2
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                return mid
        return start

nums = [1,3,5,6]
k = 7
print(searchInsert(nums,k))