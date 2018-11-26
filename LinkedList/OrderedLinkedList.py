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

class Linkedlist(object):
    def __init__(self):
        self.head = None
        self.counter = 0

    def traverse_list(self):
        actual_node = self.head
        while actual_node is not None:
            print("%d" %actual_node.data,end=" ")
            actual_node=actual_node.next_node

    def insert(self,data):
        self.counter += 1
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            previous_node = None
            stop = False
            while current_node is not None and not stop:
                if current_node.data > data:
                    stop = True
                else:
                    previous_node = current_node
                    current_node= current_node.next_node
            if previous_node is None:
                new_node.next_node = self.head
                self.head = new_node
            else:
                new_node.next_node = current_node
                previous_node.next_node = new_node
                    

    def size(self):
        return self.counter

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

linked_list = Linkedlist()

linked_list.insert(5)
linked_list.insert(6)
linked_list.insert(2)
linked_list.insert(9)
linked_list.insert(1)
linked_list.traverse_list()

