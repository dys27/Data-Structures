from heapq import heappush,heappop
class Heap(object):
    def __init__(self):
        self.heap=[]
    def insert_key(self,i): #inserts a key to the heap
        heappush(self.heap,i)
    def parent(self,i):    #returns the parent of the heap
        return (i-1)/2
    def extract_min(self):
        return heappop(self.heap)
    def delete_key(self,i): #deletes a key from the heap
        self.decrease_key(i,float("-inf"))
        self.extract_min()
    def get_min(self):      #returns minimum element from the heap
        return self.heap[0]
    def print_heap(self):
        return self.heap
    def decrease_key(self,i,new_val):
        self.heap[i]=new_val
        if i!=0 and self.heap[i]<self.heap[self.parent(i)]:
            self.heap[i],self.heap[self.parent(i)]=self.heap[self.parent(i)],self.heap[i]
