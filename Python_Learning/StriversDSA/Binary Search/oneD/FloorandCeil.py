def floorandceil(nums,target):
    start = 0
    end = len(nums)-1
    floor_val = -1
    ceil_val = -1
    if len(nums) == 1 and nums[0] == target:
        return 0 
    while(start <= end):
        mid = (start + end)// 2
        if nums[mid] < target:
            floor_val = nums[mid]
            start = mid + 1
        elif nums[mid] > target:
            ceil_val = nums[mid]
            end = mid - 1
        else:
            return nums[mid]
    return floor_val,ceil_val

nums = [2, 4, 6, 8, 10, 12, 14]
x= 1
print(floorandceil(nums,x))