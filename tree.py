class BST:
    def __init__(self,value):
        self.root=value
        self.left=None
        self.right=None
    def push(self,node,value):
        if not node.root:
            node.root=value
        else:
            if value<node.root:
                self.left=push(self,node.left,value)
            else:
                self.right=push(self,node.right,value)
            return node
while self.left is not None and self.right is not None:
    print(self.left)
    print(self.right)
mybst=BST()
root=None
mybst.push(root,4)
            

