#count frequen

arr = [1,1,2,2,3,3,4,4,4,4,5]
freq ={}
for _ in arr:
    freq[_] = freq.get(_ , 0) + 1
    
print(freq)
