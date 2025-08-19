def searchMatrix(matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        ans = -1
        for i in range(len(matrix)):
            if matrix[i][0] <= target <= matrix[i][len(matrix[0])-1]:
                ans = i
                break
        if ans == -1:
            return False
        start = 0
        end = len(matrix[ans])
        while (start <= end):
            mid = (start + end)//2
            if matrix[ans][mid] == target:
                return True
            elif matrix[ans][mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return False
        
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
print(searchMatrix(matrix,3))