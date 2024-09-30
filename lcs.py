def lcs(x,y):
    m=len(x)
    n=len(y)
    result=[[None for j in range(n+1)]for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                result[i][j]=0
            elif x[i-1]==y[j-1]:
                result[i][j]=result[i-1][j-1]+1
            else:
                result[i][j]=max(result[i-1][j],result[i][j-1])
    return result[m][n]
x="AGGTAB"
y="GXTXAYB"
print(lcs(x,y))
