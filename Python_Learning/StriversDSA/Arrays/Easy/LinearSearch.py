def linearSearch(nums, target):
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1
    
nums =  [2, 3, 4, 5, 3]
target = 5
print(linearSearch(nums,target))