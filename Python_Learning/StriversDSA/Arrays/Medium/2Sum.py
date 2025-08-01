def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        my_dic = {}
        for i in range(len(nums)):
            remaining = target - nums[i]
            if remaining in my_dic :
                return [my_dic[remaining] , i]
            else:
                my_dic[nums[i]] = i
        return [0,0]
    
nums = [2,7,11,15]
target = 9
print(twoSum(nums,target))