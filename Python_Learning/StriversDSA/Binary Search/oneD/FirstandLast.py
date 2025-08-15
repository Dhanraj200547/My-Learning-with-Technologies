def searchRange(nums, target):
        def findfirst(nums,target):
            start = 0
            end = len(nums) - 1
            while(start < end):
                mid = (start + end)//2
                if nums[mid] == target:
                    end = mid
                elif target > nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
            if start < len(nums) and nums[start] == target:
                return start
            return -1
        def findlast(nums,target):
            start = 0
            end = len(nums) -1 
            while(start < end):
                mid = ((start + end)//2) + 1
                if nums[mid] == target:
                    start = mid
                elif target > nums[mid]:
                    start = mid + 1
                else:
                    end = mid -1
            if start < len(nums) and nums[start]==target:
                return start
            return -1
        
        if len(nums) < 1:
            return -1,-1
        first = findfirst(nums,target)
        if first != -1:
            last = findlast(nums,target)
            return first,last
        return -1,-1
    
nums = [5,7,7,8,8,10]
print(searchRange(nums,8))