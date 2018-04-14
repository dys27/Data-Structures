class node(object):
    count=0
    def __init__(self,data):
        self.data=data
        self.leftChild=None
        self.rightChild=None
        
    def insert(self,data):
        if data < self.data:
            if not self.leftChild:
                self.leftChild = node(data)
            else:
                self.leftChild.insert(data)
        else:
            if not self.rightChild:
                self.rightChild=node(data)
            else:
                self.rightChild.insert(data)

    def remove(self,data,parentNode):
        if data<self.data:
            if self.leftChild is not None:
                self.leftChild.remove(data,self)
        elif data>self.data:
                if self.rightChild is not None:
                    self.rightChild.remove(data,self)
        else:
            if self.leftChild is not None and self.rightChild is not None:
                self.data = self.rightChild.getMin()
                self.rightChild.remove(self.data,self)
                
            elif parentNode.leftChild == self:
                if self.leftChild is not None:
                    tempNode = self.leftChild
                else:
                    tempNode = self.rightChild
                parentNode.leftChild = tempNode
                    
            elif parentNode.rightChild == self:
                if self.leftChild is not None:
                    tempNode = self.leftChild
                else:
                    tempNode = self.rightChild
                parentNode.rightChild = tempNode

    def getMin(self):
        if self.leftChild is None:
            return self.data 
        else:
            return self.leftChild.getMin()

    def getMax(self):
        if self.rightChild is None:
            return self.data
        else:
            return self.rightChild.getMax()

    def traverseInOrder(self):
        if self.leftChild is not None:
            self.leftChild.traverseInOrder()

        print self.data,

        if self.rightChild is not None:
            self.rightChild.traverseInOrder()

    def preOrder(self):
        print self.data,
        if self.leftChild is not None:
            self.leftChild.preOrder()
        if self.rightChild is not None:
            self.rightChild.preOrder()

    def postOrder(self):
        if self.leftChild is not None:
            self.leftChild.postOrder()
        if self.rightChild is not None:
            self.rightChild.postOrder()
        print self.data,

    def levelOrder(self):
        queue=[self]
        while (len(queue)>0):
            print queue[0].data,
            n=queue.pop(0)
            if n.leftChild is not None:
                queue.append(n.leftChild)
            if n.rightChild is not None:
                queue.append(n.rightChild)
        
            
    def search(self,data):
        if self.data==data:
            #print self.data
            node.count+=1
            if self.rightChild is not None:
                self.rightChild.search(data)
        elif data<self.data:
            if self.leftChild is not None:
                self.leftChild.search(data)
    
        else:
            if self.rightChild is not None:
                self.rightChild.search(data)
        return node.count

    def height(self):
        if self.leftChild is not None and self.rightChild is not None:
            return max(1+self.leftChild.height(),1+self.rightChild.height())
        elif self.leftChild is not None:
            return 1+self.leftChild.height()
        elif self.rightChild is not None:
            return 1+self.rightChild.height()
        else:
            return 0

class BST(object):

    def __init__(self):
        self.rootNode = None

    def insert(self,data):
        if not self.rootNode:
            self.rootNode = node(data)
        else:
            self.rootNode.insert(data)

    def remove(self,dataToRemove):
        if self.rootNode:
            if self.rootNode == dataToRemove:
                tempNode = node(None)
                tempNode.leftChild = self.rootNode
                self.rootNode.remove(dataToRemove,tempNode)
            else:
                self.rootNode.remove(dataToRemove, None)

    def getMax(self):
        if self.rootNode:
            return self.rootNode.getMax()

    def getMin(self):
        if self.rootNode:
            return self.rootNode.getMin()
        
    def traverseInOrder(self):
        if self.rootNode:
            self.rootNode.traverseInOrder()

    def preOrder(self):
        if self.rootNode:
            self.rootNode.preOrder()

    def postOrder(self):
        if self.rootNode:
            self.rootNode.postOrder()
            
    def levelOrder(self):
        if self.rootNode:
            self.rootNode.levelOrder()
            
    def search(self,data):
        if self.rootNode:
            print self.rootNode.search(data)
        else:
            print "not found"

    def height(self):
        if self.rootNode:
            return self.rootNode.height()

bst=BST()

bst.insert(1)
bst.insert(2)
bst.insert(3)
bst.insert(4)
#bst.insert(3)
#bst.insert(4)

#bst.search(-2)
#bst.traverseInOrder()
#print bst.getMax()
#print bst.getMin()
#bst.preOrder()
#bst.postOrder()
#bst.traverseInOrder()
#bst.levelOrder()
print bst.height()


            
