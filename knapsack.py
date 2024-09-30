def knapsack(weight,profit,w,n):
    result=[[0 for i in range(w+1)] for j in range(n+1)]
    for i in range(n+1):
        for j in range(w+1):
            if i==0 or j==0:
                result[i][j]=0
            elif weight[i-1]<=j:
                result[i][j]=max(profit[i-1]+result[i-1][j-weight[i-1]],result[i-1][j])
            else:
                result[i][j]=result[i-1][j]
    return result[n][w]
weight=[10,20,30]
profit=[60,100,120]
w=50
n=len(profit)
print(knapsack(weight,profit,w,n))
