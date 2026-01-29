# nums = [1,1,1,2,2,3]
# k = int(input())
# d = {}
# for i in nums:
#     if i not in d:
#         d[i] = 1
#     else:
#         d[i] += 1

# def top_k(k,d):
#     l = []
#     while k > 0:
#         a = max(d,key=d.get)
#         del d[max(d,key= d.get)]
#         k -= 1
#         l.append(a)
#     return l

# print(top_k(k,d))

from collections import Counter
nums = [1,1,1,2,2,3,3,3,3,4,5,5,5,5,5,6,6,6,7,7,7,7,7,7,7,7,7,8,8,8,8,8,8,8]

freq = Counter(nums)
k = int(input())
print([num for num,count in freq.most_common(k)])