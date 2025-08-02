def setZeroes(matrix):
        row = len(matrix)
        col = len(matrix[0])

        zero_rows = set()
        zero_cols = set()
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)
        
        for i in zero_rows:
            for j in range(col):
                matrix[i][j] = 0
        for j in zero_cols:
            for i in range(row):
                matrix[i][j] = 0
        return matrix  
matrix = [[1,1,1],[1,0,1],[1,1,1]]
print(setZeroes(matrix))