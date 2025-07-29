def rotate(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        def reverseArray(nums , start ,end):
            while(start < end):
                temp = nums[end - 1]
                nums[end -1] = nums[start]
                nums[start] = temp
                start += 1
                end -= 1
        if len(nums) < 1:
            return
        k = k % len(nums)
        reverseArray(nums, 0 , len(nums))
        reverseArray(nums,0,k)
        reverseArray(nums,k,len(nums))
nums = [1,2,3,4,5,6,7]
k = 3
rotate(nums,k)
print(nums)