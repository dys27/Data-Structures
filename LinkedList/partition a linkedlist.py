class Node(object):
    def __init__(self,data):
        self.data=data
        self.next_node=None
    def remove(self,data,previous_node):
        if self.data==data:
            previous_node.next_node=self.next_node
            del self.data
            del self.next_node
        else:
            if self.next_node is not None:
                self.next_node.remove(data,self)
class LinkedList(object):
    def __init__(self):
        self.head=None
        self.counter=0
    def add_first(self,data):
        self.counter+=1
        new_node=node(data)
        if self.head is None:
            self.head=new_node
        else:
            new_node.next_node=self.head
            self.head=new_node

    def add_last(self,data):
        if self.head is None:
            self.add_first(data)
            return
        self.counter+=1
        new_node=node(data)
        current_node=self.head
        while current_node.next_node is not None:
            current_node=current_node.next_node
        current_node.next_node=new_node

    def size(self):
        return self.counter

    def traverse(self):
        current_node=self.head
        while current_node is not None:
            print "%d"%current_node.data,
            current_node=current_node.next_node

    def remove(self,data):
        self.counter-=1
        if self.head:
            if self.head.data==data:
                self.head=self.head.next_node
            else:
                self.head.remove(data,self.head)
                
    def partition(self,part):
        l2=LinkedList()
        l3=LinkedList()
        l4=LinkedList()
        current_node=self.head
        
        while current_node is not None:
            if current_node.data<part:
                l2.add_first(current_node.data)
                current_node=current_node.next_node
            else:
                l3.add_first(current_node.data)
                current_node=current_node.next_node
        l2.traverse()
        l3.traverse()
        
ll=LinkedList()
ll.add_first(6)
ll.add_first(5)
ll.add_first(4)
ll.add_first(3)
ll.add_first(2)
ll.partition(4)
