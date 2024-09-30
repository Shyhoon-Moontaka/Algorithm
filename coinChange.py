def coinChange(deno,amount):
    i=len(deno)-1
    result=[]
    while i>=0:
        while deno[i]<=amount:
            amount-=deno[i]
            result.append(deno[i])
        i-=1
    return result
deno=[1, 2, 5, 10, 20, 50, 100, 500, 1000]
amount=93
print(coinChange(deno,amount))
