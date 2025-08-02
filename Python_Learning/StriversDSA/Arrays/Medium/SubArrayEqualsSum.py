def subarraysum(nums,k):
    count = 0
    my_dict = {}
    my_dict[0] = 1
    sum = 0
    for i in range(len(nums)):
        sum += nums[i]
        if sum - k in my_dict:
            count += my_dict[sum - k]
        my_dict[sum] = my_dict.get(sum,0) + 1
    return count

nums = [1,1,1]
k = 2
print(subarraysum(nums,k))