def singleNumber(nums):
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        
        min_key = min(d, key=d.get)
        return min_key

nums = [4,1,2,1,2]
print(singleNumber(nums))