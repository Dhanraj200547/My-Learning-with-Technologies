def maxProfit(prices):
    i = prices[0]
    maxprofit = 0
    for j in prices:
        if j < i:
            i = j
        elif (j-i) > maxprofit:
            maxprofit = max((j-i),maxprofit)
    
    return maxprofit

nums = [7,1,5,3,6,4]
print(maxProfit(nums))
        