from __future__ import print_function
class Node(object):
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

class linkedList(object):
    def __init__(self):
        self.head=None
        self.counter=0
    #o(n)
    def traverseList(self):
        actualNode = self.head

        while actualNode is not None:
            print ("%d" %actualNode.data,end=" ")
            actualNode=actualNode.nextNode

    def insertStart(self,data):
        
        self.counter +=1
        newNode=node(data)

        if not self.head:
            self.head=newNode
        else:
            newNode.nextNode=self.head
            self.head=newNode
    #O(1)
    def size(self):
        return self.counter

    def insertEnd(self,data):

        if self.head is None:
            self.insertStart(data)
            return

        self.counter+=1
            
        newNode = node(data)
        actualNode=self.head

        while actualNode.nextNode is not None:
            actualNode=actualNode.nextNode

        actualNode.nextNode=newNode
    #O(n)
    def remove(self,data):

        self.counter-=1
        if self.head:
            if data==self.head.data:
                self.head = self.head.nextNode
            else:
                self.head.remove(data,self.head)

    def reverse(self):
            actualNode=self.head
            prevTemp=None
            while actualNode is not None:
                nextTemp=actualNode.nextNode
                actualNode.nextNode=prevTemp
                prevTemp=actualNode
                actualNode=nextTemp
            self.head=prevTemp

linkedlist = linkedList()
linkedlist.insertStart(12)
linkedlist.insertStart(13)
linkedlist.insertStart(14)
linkedlist.insertStart(15)

linkedlist.traverseList()
print (linkedlist.size())
linkedlist.remove(12)
linkedlist.traverseList()
print (linkedlist.size())

                    
        
