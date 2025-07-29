def seclarge(nums):
    nums = list(set(nums))
    if len(nums) < 2:
        return -1
    first = nums[0]
    sec = nums[1]
    if first == sec:
        first = nums[1]
        sec = nums[2]
    if sec > first:
        first , sec = sec , first
    for i in range(2,len(nums)):
        if nums[i] > first and nums[i] > sec:
            temp = first
            first = nums[i]
            sec = temp
        elif nums[i] > sec and nums[i] < first:
            sec = nums[i]
    return sec

nums =  [10, 10, 10, 10, 10]
print(seclarge(nums))