class Node(object):
    count=0
    def __init__(self,data):
        self.data=data
        self.left_child=None
        self.right_child=None
        
    def insert(self,data):
        if data < self.data:
            if not self.left_child:
                self.left_child = Node(data)
            else:
                self.left_child.insert(data)
        else:
            if not self.right_child:
                self.right_child=Node(data)
            else:
                self.right_child.insert(data)

    def remove(self,data,parent_node):
        if data<self.data:
            if self.left_child is not None:
                self.left_child.remove(data,self)
        elif data>self.data:
                if self.right_child is not None:
                    self.right_child.remove(data,self)
        else:
            if self.left_child is not None and self.right_child is not None:
                self.data = self.right_child.get_min()
                self.right_child.remove(self.data,self)
                
            elif parent_node.left_child == self:
                if self.left_child is not None:
                    temp_node = self.left_child
                else:
                    temp_node = self.right_child
                parent_node.left_child = temp_node
                    
            elif parent_node.right_child == self:
                if self.left_child is not None:
                    temp_node = self.left_child
                else:
                    temp_node = self.right_child
                parent_node.right_child = temp_node

    def get_min(self):
        if self.left_child is None:
            return self.data 
        else:
            return self.left_child.get_min()

    def get_max(self):
        if self.right_child is None:
            return self.data
        else:
            return self.right_child.get_max()

    def traverse_in_order(self):
        if self.left_child is not None:
            self.left_child.traverse_in_order()

        print self.data,

        if self.right_child is not None:
            self.right_child.traverse_in_order()

    def pre_order(self):
        print self.data,
        if self.left_child is not None:
            self.left_child.pre_order()
        if self.right_child is not None:
            self.right_child.pre_order()

    def post_order(self):
        if self.left_child is not None:
            self.left_child.post_order()
        if self.right_child is not None:
            self.right_child.post_order()
        print self.data,

    def level_order(self):
        queue=[self]
        while (len(queue)>0):
            print queue[0].data,
            n=queue.pop(0)
            if n.left_child is not None:
                queue.append(n.left_child)
            if n.right_child is not None:
                queue.append(n.right_child)
        
            
    def search(self,data):
        if self.data==data:
            #print self.data
            Node.count+=1
            if self.right_child is not None:
                self.right_child.search(data)
        elif data<self.data:
            if self.left_cild is not None:
                self.left_child.search(data)
    
        else:
            if self.right_child is not None:
                self.right_child.search(data)
        return Node.count

    def height(self):
        if self.left_child is not None and self.right_child is not None:
            return max(1+self.left_child.height(),1+self.right_child.height())
        elif self.left_child is not None:
            return 1+self.left_child.height()
        elif self.right_child is not None:
            return 1+self.right_child.height()
        else:
            return 0

class BST(object):

    def __init__(self):
        self.root_node = None

    def insert(self,data):
        if not self.root_node:
            self.root_node = Node(data)
        else:
            self.root_node.insert(data)

    def remove(self,data_to_remove):
        if self.root_node:
            if self.root_node == data_to_remove:
                temp_node = Node(None)
                temp_node.left_child = self.root_node
                self.root_node.remove(data_to_remove,temp_node)
            else:
                self.root_node.remove(data_to_remove, None)

    def get_max(self):
        if self.root_node:
            return self.root_node.get_max()

    def get_min(self):
        if self.root_node:
            return self.root_node.get_min()
        
    def traverse_in_order(self):
        if self.root_node:
            self.root_node.traverse_in_order()

    def pre_order(self):
        if self.root_node:
            self.root_node.pre_order()

    def post_order(self):
        if self.root_node:
            self.root_node.post_order()
            
    def level_order(self):
        if self.root_node:
            self.root_node.level_order()
            
    def search(self,data):
        if self.root_node:
            print self.root_node.search(data)
        else:
            print "not found"

    def height(self):
        if self.root_node:
            return self.root_node.height()

bst=BST()

bst.insert(1)
bst.insert(2)
bst.insert(3)
bst.insert(4)
#bst.insert(3)
#bst.insert(4)

#bst.search(-2)
#bst.traverse_in_order()
#print bst.get_max()
#print bst.get_min()
#bst.pre_order()
#bst.post_order()
#bst.traverse_in_order()
#bst.level_order()
print bst.height()


            
