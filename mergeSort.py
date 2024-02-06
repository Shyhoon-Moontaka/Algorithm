def mergeSort(array):   
    if len(array)<=1:
        return array
    else:
        mid=len(array)//2
        left=mergeSort(array[:mid])
        right=mergeSort(array[mid:])
    return merge(left,right)
def merge(left,right):
    result=[]
    i=0
    j=0
    while(i<len(left) and j<len(right)):
        if(left[i]<right[j]):
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result+=left[i:] 
    result+=right[j:]  
    return result
print(mergeSort([4,2,5,1,7,6,3]))