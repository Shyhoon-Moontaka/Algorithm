def maxSubArray(array):
    currentSum=maxSum=array[0]
    for num in array[1:]:
        currentSum=max(num,num+currentSum)
        maxSum=max(currentSum,maxSum)
    return maxSum
array=[5,4,-1,7,8]
print(maxSubArray(array))
