def unionArray(nums1, nums2):
    arr = []
    i = 0
    j = 0
    while i != len(nums1) and j != len(nums2):
        if nums1[i] == nums2[j]:
            if not arr or arr[-1] != nums1[i]:
                arr.append(nums1[i])
                i += 1
                j += 1
        elif nums1[i] < nums2[j]:
            if not arr or arr[-1] != nums1[i]:
                arr.append(nums1[i])
                i += 1
        else:
            if not arr or arr[-1] != nums2[j]:
                arr.append(nums2[j])
                j += 1
            
    while i != len(nums1):
        if not arr or arr[-1] != nums1[i]:
            arr.append(nums1[i])
            i += 1
        
    while j != len(nums2):
        if not arr or arr[-1] != nums2[j]:
            arr.append(nums2[j])
            j += 1
        
    return arr
nums1 = [1,2,3,4,5]
nums2 = [1,2,7]
print(unionArray(nums1,nums2))