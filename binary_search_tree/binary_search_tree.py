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
# from collections import deque 
import sys
sys.path.append('../queue')
from queue_id import Queue

import sys
sys.path.append('../stack')
from stack_id import Stack

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is None: 
                self.left = BSTNode(value) #new_node = BTSNode(value)
            else:
                #if used 'return'still passed, but not necessary
                self.left.insert(value)
        elif value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value) 

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        #differece between if self.value == target:
        if target == self.value:
            return True
            #which direction: right (7 > 5)
            #based '=' just to keep with flow of insert
            #elif target >= self.value:
        elif target > self.value:
            #self.right  (5 = None?) Nope - based on test file
            if self.right is None:
                return False
            else:
            #why have to 'return' here and not on line 27?
            #in 'insert' it is doing an action and is not returning a value
            # in 'contains' we are asking for value to be returned (pass back value)
                return self.right.contains(target)
                #return True (same as line above)
        elif target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        #right most is where the max lies?
        if self.right is None:
            #return value at root, since right is where larger number would exist if in tree
            return self.value
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        #fn is a function that operates on the kind of data stored in the tree
        #value is not optional so this will work
        fn(self.value)
        if self.left is not None:
            self.left.for_each(fn)
        if self.right is not None:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node is not None:
            self.in_order_print(node.left)
            print(node.value)
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(node)
        while len(queue) > 0:
            popped = queue.dequeue()
            print(popped.value)
            if popped.left:
                queue.enqueue(popped.left)
            if popped.right:
                queue.enqueue(popped.right)


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(node)
        while len(stack) > 0:
            popped = stack.pop()
            print(popped.value)
            if popped.left:
                stack.push(popped.left)
            if popped.right:
                stack.push(popped.right)
        #stack
        #start your stack with the root node

        #while loop that checks stack size
            #pointer (each time you make a call you update pointer)



    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
         if node is not None:
            print(node.value)
            self.pre_order_dft(node.left)
            self.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node is not None:
            self.post_order_dft(node.left)
            self.post_order_dft(node.right)
            print(node.value)


 #lowest number is always furthest to the left
    #base case?
    #what if the node we pass in is none?
        # if node is None:
        #     return 
    #recursive case?
            # self.in_order_print(node.left)
            # print(node.value)
            # self.in_order_print(node.right)

             # if node:
        #     red = self.in_order_print(node.left)
        #     res.append(node.value)
        #     res = self.in_order_print(node.right)
        # return res

        # if self.left:
        #    return self.in_order_print(self.left)
        # else:
        #    return self.in_order_print(self.right)

        # if self.right:
        #    return self.in_order_print(self.right)
        # else:
        #    return self.in_order_print(self.left)
        # print(self.value)
        #build up your call stack to see what happens
