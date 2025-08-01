# def rearrangeArray(nums):
#     pos = []
#     neg = []
#     for i in nums:
#         if i > 0:
#             pos.append(i)
#         else:
#             neg.append(i)
    
#     for i in range(len(pos)):
#         nums[2*i] = pos[i]                #Bruteforce approach
#     for i in range(len(neg)):
#         nums[2*i+1] = neg[i]
    
#     return nums

def rearrangeArray(nums):
        ans = [0]*len(nums)
        i = 0
        j = 1
        for k in range(len(nums)):
            if nums[k] > 0:
                ans[i] = nums[k]
                i += 2
            else:
                ans[j] = nums[k]
                j += 2
        return ans
nums = [3,1,-2,-5,2,-4]
print(rearrangeArray(nums))