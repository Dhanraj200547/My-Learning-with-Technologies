'''
Bruteforce method
def majorityElement(nums):
        """
        :type nums: List[int]
        :rtype: int                         
        """
        my_dict = {}
        for i in nums:
            if i not in my_dict:
                my_dict[i] = 1              #O(n) ,O(n)
            else:
                my_dict[i] += 1
        
        return max(my_dict , key = my_dict.get)
    '''

def majorityElement(nums):              #Boyers moore majority voting algorithm O(n) , O(1)
    """
    :type nums: List[int]
    :rtype: int
    """
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        count += ( 1 if num == candidate else -1)
    
    return candidate
    
nums = [2,2,1,1,2,2]
print(majorityElement(nums))