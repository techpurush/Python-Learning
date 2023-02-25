class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data

    def insert(self,item):
        if self:
            if item<self.data:
                if not self.left:
                    self.left=Node(item)
                else:
                    self.left.insert(item)
            else:
                if not self.right:
                    self.right=Node(item)
                else:
                    self.right.insert(item)

    def printTree(self):
        if self.left:
            self.left.printTree()

        if self.right:
            self.right.printTree()

        print(self.data)

    def height(self,root):
        if root is None:
            return -1
        left_h=self.height(root.left)
        right_h=self.height(root.right)

        return 1+max(left_h,right_h)

n=Node(6)
n.insert(10)
n.insert(8)
n.insert(3)
n.insert(5)
n.insert(2)
n.insert(11)

n.printTree()

print("--"*15)

print("Height: ",n.height(n))