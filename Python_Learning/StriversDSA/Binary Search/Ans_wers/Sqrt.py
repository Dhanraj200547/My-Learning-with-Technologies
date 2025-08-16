def sqrt(n):
    start = 0
    end = n - 1
    while(start < end):
        mid = (start + end)//2
        if (mid * mid) == n:
            return mid
        elif (mid * mid) > n:
            end = mid - 1
        else:
            start = mid + 1
    return start
    
n = 36
print(sqrt(n))