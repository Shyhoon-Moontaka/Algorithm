function heapify(array,n,i){
    let largest=i;
    let left=2*i+1;
    let right=2*i+2;
    
    if(left<n && array[left]>array[i]){
        largest=left;
    }
    if(right<n && array[right]>array[largest]){
        largest=right;
    }
    if(largest!==i){
        let temp=array[largest];
        array[largest]=array[i];
        array[i]=temp;
        heapify(array,n,largest);
    }
}
function heapSort(array){
    let n=array.length;
    for(let i=Math.round(n/2);i>=0;i--){
        heapify(array,n,i);
    }
    for(let j=n-1;j>0;j--){
        let temp=array[0];
        array[0]=array[j];
        array[j]=temp;
        heapify(array,j,0);
    }
}
let arr=[34,2,6,4,7,5];
let n=arr.length;
heapSort(arr);
console.log(arr)