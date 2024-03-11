class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class LinkedList:
    def __init__(self,value):
        newNode=Node(value)
        self.head=newNode
        self.tail=self.head
        self.length=1
    def push(self,value):
        newNode=Node(value)
        if not self.head:
            self.head=newNode
            self.tail=newNode
        else:
            self.tail.next=newNode
            self.tail=newNode
        self.length+=1
    def pop(self):
        if not self.head:
            return None
        else:
            current=myLinkedList.head
            i=1
            while i<myLinkedList.length:
                if current.value==5:
                    current.value=None
                current=current.next
                i+=1
            current.value=None
            self.length-=1
        return current.value
myLinkedList=LinkedList(4)
myLinkedList.push(5)
myLinkedList.push(6)
myLinkedList.push(7)
print("pop",myLinkedList.pop())
i=1
while i<=myLinkedList.length:
    print(myLinkedList.head.value)
    myLinkedList.head=myLinkedList.head.next
    i+=1
    
    