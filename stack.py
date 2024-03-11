capacity=4
stack=[None]*capacity

top= -1
def pop():
    global top
    if top>=0:
        item=stack[top]
        stack[top]=None
        top=top-1
        return item
    return -1
def push(value):
    global top
    if top<capacity-1:
        top=top+1
        stack[top]=value
    else:
        return -1


push(8)
push(5)
push(7)
push(9)
pop()
pop()
print(stack)