def findpivot(nums):
        start = 0
        end = len(nums) - 1
        if nums[start] <= nums[end]:
            return 0
        while(start <= end):
            mid = (start + end)//2
            if mid < len(nums)-1 and nums[mid] > nums[mid + 1]:
                return mid + 1
            if mid > start and nums[mid] < nums[mid - 1]:
                return mid
            if nums[mid] >= nums[start]:
                start = mid + 1
            else:
                end = mid - 1
        return 0
def search(nums,start,end,target):
    while(start <= end):
        mid = (start + end)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1
nums = [7,8,0,1,2,3,4,5,6]
target = 8
start = 0
end = len(nums) - 1
print(findpivot(nums))
pivot = findpivot(nums)
ans = (search(nums,start,pivot-1,target))
if ans == -1:
    print(search(nums,pivot,end,target))
print(ans)