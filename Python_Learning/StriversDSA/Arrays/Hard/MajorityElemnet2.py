def majorityElement(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        my_dict = {}
        for i in nums:
            if i not in my_dict:
                my_dict[i] = 1
            else:
                my_dict[i] += 1
        for i in my_dict:
            if my_dict[i] > (len(nums) // 3):
                ans.append(i)
        return ans
    
nums = [3,2,3]
print(majorityElement(nums))