# O( m+n) approach
# def merge(nums1, m, nums2, n):
#         arr = []
#         i = 0
#         j = 0
#         while ( i < m and j < n):
#             if nums1[i] <= nums2[j]:
#                 arr.append(nums1[i])
#                 i += 1
#             else:
#                 arr.append(nums2[j])
#                 j += 1
#         while( i < m):
#             arr.append(nums1[i])
#             i += 1
#         while( j < n):
#             arr.append(nums2[j])
#             j += 1
#         for i in range(len(nums1)):
#             nums1[i] = arr[i]
            
# OPTIMAL APPROACH O(n)
def merge(nums1, m, nums2, n):
        i = m - 1
        j = n -1
        k = m + n - 1
        while ( j >= 0):
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        return nums1
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
print(merge(nums1,3,nums2,3))