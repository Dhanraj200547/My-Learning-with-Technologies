from collections import defaultdict
def countsubarrays(nums,k):
    xr = 0
    dic = defaultdict(int)
    dic[xr] = 1
    count = 0
    for i in range(len(nums)):
        xr ^= nums[i]
        x = xr ^ k
        count += dic[x]
        dic[xr] += 1
    return count

nums = [4, 2, 2, 6, 4]
k = 6
print(countsubarrays(nums,k))