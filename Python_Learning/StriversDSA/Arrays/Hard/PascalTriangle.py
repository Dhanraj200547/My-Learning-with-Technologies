def pascaltriangle(n):
    arr = []
    for i in range(n):
        row = [1] * (i+1)
        for j in range(1,i):
            row[j] = arr[i-1][j-1] + arr[i-1][j]
        arr.append(row)
    return arr

n = 5
print(pascaltriangle(n))
