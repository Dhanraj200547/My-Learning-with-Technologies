
def fourSum(nums, target):
    nums.sort()
    ans = []
    n = len(nums)

    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # Skip duplicate i
        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue  # Skip duplicate j
            left, right = j + 1, n - 1
            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]
                if total == target:
                    ans.append([nums[i], nums[j], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # Skip duplicates for left
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # Skip duplicates for right
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1
    return ans

nums = [1,0,-1,0,-2,2]
print(fourSum(nums,0))