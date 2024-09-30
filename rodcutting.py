def rodcutting(prices):
    n=len(prices)
    result=[0 for i in range(n+1)]
    result[0]=0
    inf=-9999
    for i in range(1,n+1):
        maxValue=inf
        for j in range(i):
            maxValue=max(maxValue,prices[j]+result[i-j-1])
        result[i]=maxValue
    return result[n]
prices=[2, 4, 7, 9, 11, 16, 16, 21]
print(rodcutting(prices))

