def search(nums, target):
        start = 0
        end = len(nums)-1
        if len(nums) == 1 and nums[0] == target:
            return 0 
        if len(nums) <= 1:
            return -1
        while(start <= end):
            mid = (start + end)// 2
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                return mid
        return -1

nums = [2,5]
k = 5
print(search(nums,k))