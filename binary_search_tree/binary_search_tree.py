"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

from queue_copy import Queue

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value <  self.value:
            if self.left == None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else: 
            if self.right == None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if not self.value:
            return None
        else:
            if self.right is None:
                return self.value
            else: 
                return self.right.get_max()

    # Call the function `fn` on the value of each node
    
    ##callback function being used recursively?
    def for_each(self, fn):
        if not self.value:
            return 
        else:
            fn(self.value)
            if self.left:
                self.left.for_each(fn)
            if self.right:
                self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node:
            self.in_order_print(node.left)

            print(node.value)
            
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        q = Queue()
        
        q.enqueue(node)

        # print(node.value)
        # print(f"{q.storage.head}")
        # print(f"{q.storage.head.data.value}")
        # print(f"{q.size}")

        
        while q.size > 0:
            print(f"{q.storage.head.data.value}")
            tracking_node = q.dequeue()
            if tracking_node.right: 
                q.enqueue(tracking_node.right)
        
            if tracking_node.left:
                q.enqueue(tracking_node.left)
            
            
            
  
        

     

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        if node:
            print(node.value)
        self.dft_print(node.left)
        self.dft_print(node.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

t = BSTNode(1)
t.insert(8)
t.insert(5)
t.insert(7)
t.insert(6)
t.insert(3)
t.insert(4)
t.insert(2)

t.bft_print(t)
