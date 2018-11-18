class Node(object):
    def __init__(self,data):
        self.data=data
        self.next_node = None

    def remove(self,data,previous_node):
        if self.data == data:
            previous_node.next_node = self.next_node
            del self.data
            del self.next_node
            return True
        else:
            if self.next_node is not None:
                return self.next_node.remove(data,self)

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.counter = 0

    def traverse_list(self):
        actual_node = self.head
        while actual_node is not None:
            print("%d" %actual_node.data,end=" ")
            actual_node=actual_node.next_node

    def insert_start(self,data):
        self.counter += 1
        new_node = Node(data)
        if not self.head:
            self.head=new_node
        else:
            new_node.next_node = self.head
            self.head=new_node

    def size(self):
        return self.counter

    def insert_end(self,data):
        if self.head is None:
            self.insert_start(data)
            return
        self.counter += 1
        new_node = Node(data)
        actual_node=self.head
        while actual_node.next_node is not None:
            actual_node=actual_node.next_node
        actual_node.next_node = new_node

    def remove(self,data):
        if self.head:
            if data==self.head.data:
                self.head=self.head.next_node
                self.counter -= 1
            else:
                if (self.head.remove(data,self.head)):
                    self.counter -= 1


    def reverse(self):
        actual_node = self.head
        prev_temp = None
        while actual_node is not None:
            next_temp = actual_node.next_node
            actual_node.next_node = prev_temp
            prev_temp =  actual_node
            actual_node = next_temp
        self.head=prev_temp

linked_list = LinkedList()

linked_list.insert_end(1)
linked_list.insert_end(2)
linked_list.insert_end(3)
linked_list.insert_end(4)
linked_list.insert_end(5)
print(linked_list.size())
linked_list.remove(3)
print(linked_list.size())


                    
        
