def maxEle(nums):
    max = 0
    for i in nums:
        if i > max:
            max = i
    return max

nums = [3, 3, 6, 1]
print(maxEle(nums))