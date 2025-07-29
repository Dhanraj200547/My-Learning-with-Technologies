#Remove duplicates from a sorted array
def removeDuplicates(nums):
    i = 0
    for j in range(1,len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
    return i + 1

nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums))
print(nums)