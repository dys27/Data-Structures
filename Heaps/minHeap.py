class Heap:
    def __init__(self):
        self.capacity = 10
        self.size = 0
        self.elements = [None]*self.capacity
 
    def getLeftChildIndex(self,parentIndex):
        return parentIndex*2+1

    def getRightChildIndex(self,parentIndex):
        return parentIndex*2+2

    def getParent(self,childIndex):
        return (childIndex-1)//2

    def hasLeftChild(self,parentIndex):
        return self.getLeftChildIndex(parentIndex) < self.size

    def hasRightChild(self,parentIndex):
        return self.getRightChildIndex(parentIndex) < self.size

    def hasParent(self,childIndex):
        return self.getParent(childIndex) >= 0

    def leftChild(self,parent):
        return self.elements[self.getLeftChildIndex(parent)]

    def rightChild(self,parent):
        return self.elements[self.getRightChildIndex(parent)]

    def parent(self,child):
        return self.elements[self.getParent(child)]

    def swap(self,index1,index2):
        self.elements[index1],self.elements[index2] = self.elements[index2],self.elements[index1]

    def ensureExtraCapacity(self):
        if self.capacity == self.size:
            self.elements += ([None]*self.capacity)
            self.capacity*=2
 
    def peek(self):
        if self.size > 0:
            return self.elements[0]

    def poll(self):
        if self.size > 0:
            element = self.elements[0]
            self.swap(0,self.size-1)
            self.size -= 1
            self.heapifyDown()
            return element

    def add(self,val):
        self.ensureExtraCapacity()
        self.elements[self.size] = val
        self.size += 1
        self.heapifyUp()

    def heapifyUp(self):
        index = self.size-1
        while self.hasParent(index) and self.parent(index) > self.elements[index]:
            self.swap(self.getParent(index),index)
            index = self.getParent(index)

    def heapifyDown(self):
        index = 0
        while self.hasLeftChild(index):
            smallerChildIndex = self.getLeftChildIndex(index)
            if self.hasRightChild(index) and self.rightChild(index) < self.leftChild(index):
                smallerChildIndex = self.getRightChildIndex(index)
            if self.elements[index] < self.elements[smallerChildIndex]:
                break
            else:
                self.swap(index,smallerChildIndex)
            index = smallerChildIndex
