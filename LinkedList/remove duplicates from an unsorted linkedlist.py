class node(object):
    def __init__(self,data):
        self.data=data
        self.nextNode=None
    def remove(self,data,previousNode):
        if self.data==data:
            previousNode.nextNode=self.nextNode
            del self.data
            del self.nextNode
        else:
            if self.nextNode is not None:
                self.nextNode.remove(data,self)
class linkedlist(object):
    def __init__(self):
        self.head=None
        self.counter=0
    def addFirst(self,data):
        self.counter+=1
        newNode=node(data)
        if self.head is None:
            self.head=newNode
        else:
            newNode.nextNode=self.head
            self.head=newNode

    def addLast(self,data):
        if self.head is None:
            self.addFirst(data)
            return
        self.counter+=1
        newNode=node(data)
        currentNode=self.head
        while currentNode.nextNode is not None:
            currentNode=currentNode.nextNode
        currentNode.nextNode=newNode

    def size(self):
        return self.counter

    def traverse(self):
        currentNode=self.head
        while currentNode is not None:
            print "%d"%currentNode.data,
            currentNode=currentNode.nextNode

    def remove(self,data):
        self.counter-=1
        if self.head:
            if self.head.data==data:
                self.head=self.head.nextNode
            else:
                self.head.remove(data,self.head)
    def reverse(self):
        currentNode=self.head
        tempPrev=None
        while currentNode is not None:
            tempNext=currentNode.nextNode
            currentNode.nextNode=tempPrev
            tempPrev=currentNode
            currentNode=tempNext
        self.head=currentNode

    def duplicate(self):
        dictionary={}
        currentNode=self.head
        prevNode=None
        while currentNode is not None:
            if currentNode.data not in dictionary:
                dictionary[currentNode.data]=1
                prevNode=currentNode
                currentNode=currentNode.nextNode        
            else:
                prevNode.nextNode=currentNode.nextNode
                del currentNode.data
                del currentNode.nextNode
                currentNode=prevNode.nextNode
