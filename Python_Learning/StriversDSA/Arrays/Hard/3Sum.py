'''
#Brute Force Approach
def Sum(nums):
    ans = []
    n = len(nums)
    my_dict = {}
    for i in range(len(nums)):
        for j in range(i + 1,len(nums)):
            for k in range(j + 1,len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    key = tuple(sorted([nums[i],nums[j],nums[k]]))
                    if key not in my_dict:
                        my_dict[key] = True
                        ans.append([nums[i],nums[j],nums[k]])
                    
    return ans
'''
def threeSum(nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        ans = []
        nums.sort()
        for i in range(n):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = n -1
            while(j < k):
                sum = nums[i] + nums[j] + nums[k]
                if sum > 0:
                    k -= 1
                elif sum < 0:
                    j += 1
                else:
                    temp = [nums[i] , nums[j] ,nums[k]]
                    ans.append(temp)
                    j += 1
                    k -= 1
                    while (j < k) and nums[j] == nums[j -1]:
                        j += 1
                    while(j < k) and nums[k] == nums[k +1]:
                        k -= 1

        return ans
    
nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))