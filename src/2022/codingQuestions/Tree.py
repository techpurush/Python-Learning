c=0
from collections import deque
# print(dir(collections))

class  tree:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

    def insert(self,val):
        if self.val ==None:
            self.val=val
            return
        if val<self.val:
            if self.left:
                self.left.insert(val)
            else:
                self.left=tree(val)
        else:
            if self.right:
                self.right.insert(val)
            else:
                self.right=tree(val)

    def inorder(self):

        def inorder(node):

            if node is None:return

            inorder(node.left)
            print(node.val)
            inorder(node.right)
            return

        inorder(self)


    def getCount(self):

        def findcount(node):
            if node is None:
                return 0

            if node.left is None and node.right is None:
                # global c
                # c=c+1
                return 1

            leftc=findcount(node.left)
            rightc=findcount(node.right)
            # self.right.getCount()
            return leftc+rightc

            # print(c)
        return findcount(self)

    def getMaxWidth(self):

        x=deque()

        def findcount(node,k,d):
            if k==1:return d

            if node is None:
                return d

            if node.left is None and node.right is None:
                # global c
                # c=c+1
                return d

            if not d:
                d.append(node)
            else:
                while True:
                    n=d.popleft()
                    while n:
                        if n.left:
                            d.append(n.left)
                        elif n.right:
                            d.append(n.right)
                        else:break

            # d.append(node.right)

            findcount(node,k-1,d)
            # findcount(node.right,k-1,d)


            # print(c)
        return findcount(self,2,x)


t=tree(5)
t.insert(3)
t.insert(10)
t.insert(4)
t.insert(8)
t.insert(1)

print(t.getMaxWidth())
# t.inorder()






