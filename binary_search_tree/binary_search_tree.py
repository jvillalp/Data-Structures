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
        #lowest number is always furthest to the left

        #base case?
        if none is None:
            return
        #what if the node we pass in is none?

        #recursive case
        self.in-in_order_print(self.left)

        #build up your call stack to see what happens


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        #use queue

        #while loop that checks size of queue
                #pointer variable that updates at the beginning of each loop



    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        #stack
        #start your stack with the root node

        #while loop that checks stack size
        #pointer

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
