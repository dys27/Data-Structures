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
                
    def partition(self,part):
        l2=linkedlist()
        l3=linkedlist()
        l4=linkedlist()
        currentNode=self.head
        
        while currentNode is not None:
            if currentNode.data<part:
                l2.addFirst(currentNode.data)
                currentNode=currentNode.nextNode
            else:
                l3.addFirst(currentNode.data)
                currentNode=currentNode.nextNode
        l2.traverse()
        l3.traverse()
        
ll=linkedlist()
ll.addFirst(6)
ll.addFirst(5)
ll.addFirst(4)
ll.addFirst(3)
ll.addFirst(2)
ll.partition(4)
