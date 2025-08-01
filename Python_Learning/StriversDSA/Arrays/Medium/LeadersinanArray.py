# def leadersinarray(nums):
#     ans = []
#     for i in range(len(nums)):
#         Leader = True
#         for j in range(i + 1,len(nums)):
#             if nums[j] > nums[i]:             #Bruteforce approach 
#                 Leader = False
#                 break
#         if Leader:
#             ans.append(nums[i])
    
#     return ans
def leadersinarray(nums):
    n = len(nums)
    ans = []
    max = nums[n-1]
    ans.append(nums[n-1])
    for i in range(n-2,-1,-1):              #optimal but in reverse, can be adjusted
        if nums[i] > max:
            ans.append(nums[i])
            max = nums[i]
    return ans

nums = [10, 22, 12, 3, 0, 6]
print(leadersinarray(nums))