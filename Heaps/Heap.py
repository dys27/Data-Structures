from heapq import heappush,heappop
class heap(object):
    def __init__(self):
        self.heap=[]
    def insertKey(self,i): #inserts a key to the heap
        heappush(self.heap,i)
    def parent(self,i):    #returns the parent of the heap
        return (i-1)/2
    def extractMin(self):
        return heappop(self.heap)
    def deleteKey(self,i): #deletes a key from the heap
        self.decreaseKey(i,float("-inf"))
        self.extractMin()
    def getMin(self):      #returns minimum element from the heap
        return self.heap[0]
    def printHeap(self):
        return self.heap
    def decreaseKey(self,i,new_val):
        self.heap[i]=new_val
        if i!=0 and self.heap[i]<self.heap[self.parent(i)]:
            self.heap[i],self.heap[self.parent(i)]=self.heap[self.parent(i)],self.heap[i]
