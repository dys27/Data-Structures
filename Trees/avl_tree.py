#import random

class Node:
    def __init__(self,key):
        self.key=key
        self.right=None
        self.left=None
        self.height=1

def rotate_right(y):
    x=y.left
    T2=x.right
    x.right=y
    y.left=T2
    y.height=max(height(y.left),height(y.right))+1
    x.height=max(height(x.left),height(x.right))+1
    return x

def rotate_left(x):
    y=x.right
    T2=y.left
    y.left =x
    x.right = T2
    x.height = max(height(x.left),height(x.right))+1
    y.height = max(height(y.left),height(y.right))+1
    return y

def max(a,b):
    if a>b:
        return a
    else:
        return b

def Balance(current):
    if current== None:
        return 0
    return (height(current.left) - height(current.right))

def height(current):
    if current == None:
        return 0
    return current.height

def make_root(key):
    return Node(key)

#def newNode(key):

def insert(current,key):
    if current == None:
        return Node(key)
    
    if key<current.key:
        current.left=insert(current.left,key)
    else:
        current.right=insert(current.right,key)
    current.height=max(height(current.left),height(current.right))+1
    balance=Balance(current)

    #left left
    if balance > 1 and key < current.left.key:
        return rotate_right(current)

    #right right
    if balance < -1 and key > current.right.key:
        return rotate_left(current)

    #left right
    if balance > 1 and key > current.left.key:
        current.left=rotate_left(current.left)
        return rotate_right(current)

    #right left
    if balance < -1 and key < current.right.key:
        current.right=rotate_right(current.right)
        return rotate_left(current)

    return current

def pre_order(temp):
    if temp!=None:
        print temp.key," ",temp.height, " ",Balance(temp)
        pre_order(temp.left)
        pre_order(temp.right)

def main():
    import random
    root=make_root(10)
    #root=insert(root,20)
    #root=insert(root,30)
    #root=insert(root,40)
    for x in range(5):
        root=insert(root, random.randint(0,100))
    print root.key
    pre_order(root)

if __name__=="__main__":
    main()
