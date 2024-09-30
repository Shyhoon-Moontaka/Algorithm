def bubblesort(lis):
    for i in range(len(lis)-1,0,-1):
        for j in range(i):
            if lis[j]>lis[j+1]:
                lis[j],lis[j+1]=lis[j+1],lis[j]
    return lis
lis=[5,2,8,4,1]
print(bubblesort(lis))
