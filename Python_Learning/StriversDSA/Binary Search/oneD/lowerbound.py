def lowerbound(nums,k):
    start = 0
    end = len(nums) - 1
    ans = 0
    while(start<=end):
        mid = (start + end)//2
        if nums[mid] >= k:
            ans = mid
            end = mid - 1
        elif nums[mid] < k:
            start = mid + 1
    return ans

nums =  [3, 5, 8, 15, 19]
k = 9
print(lowerbound(nums,k))