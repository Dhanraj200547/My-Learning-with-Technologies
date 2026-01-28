arr = [1,1,2,2,3,4,5,6,6,7,8]
d = {}

for i in arr:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1

print([i for i in d if d[i] > 1 ])