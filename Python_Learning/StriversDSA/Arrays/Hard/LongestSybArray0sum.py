# Bruteforce approach
# def longestsubarray(nums):
#     maxlen = 0
#     for i in range(len(nums)):
#         length = 0
#         s = 0
#         for j in range(i,len(nums)):
#             s += nums[j]
#             if s == 0:
#                 maxlen = max(maxlen,(j - i) + 1)
#     return maxlen
def longestsubarray(nums):
    maxlen = 0
    dic = {}
    s = 0
    for i in range(len(nums)):
        s += nums[i]
        if s == 0:
            maxlen = i + 1
        if s in dic:
            maxlen = max(maxlen,i - dic[s])
        else:
            dic[s] = i
    return maxlen


nums = [9, -3, 3, -1, 6, -5]
print(longestsubarray(nums))

