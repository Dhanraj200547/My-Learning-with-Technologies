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
def Sum(nums):
    pass
nums = [-1,0,1,2,-1,-4]
print(Sum(nums))