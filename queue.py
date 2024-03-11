capacity=4
queue=[None]*capacity
front=0
rear= -1
totalItem=0
def enqueue(item):
    global capacity
    global front
    global rear
    global totalItem
    if totalItem==capacity:
        return -1
    else:
        rear=(rear+1)%capacity
        queue[rear]=item
        totalItem+=1

def dequeue(item):
    global capacity
    global front
    global rear
    global totalItem
    if totalItem==0:
        return -1
    else:
        frontItem=queue[front]
        queue[front]= -1
        front=(front+1)%capacity
        
        totalItem-=1
        return frontItem
enqueue(8)
enqueue(6)
enqueue(5)
print(queue)
dequeue(2)
enqueue(5)
dequeue(2)
print(queue)