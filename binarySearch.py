def quicksort(array):
    
    n=len(array)
    if n<=1:
        return array
    else:
        left=[]
        right=[]
        pivot=array.pop()
        for item in array:
            if item <pivot:
                left.append(item)
            else:
                right.append(item)
        result= quicksort(left)+[pivot]+quicksort(right)
        print(result)
        return result
        

def binarysearch(array,item):
    try:
        sortedArray=quicksort(array)
        print("sortedArray:",sortedArray)
        n=len(sortedArray)
        left=0
        right=n-1
        middle=(left+right)//2
    
        while left<=right:
        
            if sortedArray[middle]==item:
                print("Middle:",middle)
                return middle
            
            elif sortedArray[middle]<item:
                middle+=1
                print("Middle:",middle)
            else:
                middle-=1
                print("Middle:",middle)
    except:
        return -1
        
    
print(binarysearch(["b","d","a","s","h","g"],"g"))
