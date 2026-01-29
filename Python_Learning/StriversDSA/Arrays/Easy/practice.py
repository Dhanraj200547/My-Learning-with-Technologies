arr = [7,4,5,9,3,2,1]

max_sum = 0

for i in arr:
    sum = 0
    for j in arr:
        sum += j
    max_sum = max(max_sum,sum)

print(max_sum)