def transpose(matrix):
    for i in range(len(matrix)):
        for j in range(i+1,len(matrix)):
            matrix[i][j],matrix[j][i] = matrix[j][i], matrix[i][j]

def reverse(matrix):
    for row in matrix:
        row.reverse()
def rotate(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    transpose(matrix)
    reverse(matrix)
    return matrix
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate(matrix))