def merge(intervals):
    intervals.sort()
    ans = []
    for interval in intervals:
        if not ans or ans[-1][1] < interval[0]:
            ans.append(interval)
        else:
            ans[-1][1] = max(ans[-1][1], interval[1])
    return ans
arr =  [[1,3],[2,6],[8,10],[15,18]]
print(merge(arr))