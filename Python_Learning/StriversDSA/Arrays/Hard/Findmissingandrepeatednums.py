def findmissingandrepeated(nums):
    arr = []
    n = len(nums)
    dic = {}
    for i in nums:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    for i in dic:
        if dic[i] == 2:
            arr.append(i)
            arr.append(i)
    seen = set(nums)
    number = ((n * (n+1)) // 2 )- sum(seen)
    arr.append(number)
    arr.sort()
    return arr
    
nums = [3,1,2,5,3]
print(findmissingandrepeated(nums))