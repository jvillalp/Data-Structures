import sys
sys.path.append('../singly_linked_list')
from singly_linked_list import LinkedList

"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        #not sure why storage and not size?
        return len(self.storage)

    def push(self, value):
        return self.storage.append(value)

    def pop(self):
        #why do you need a conditional here??
        if len(self.storage) > 0:
            return self.storage.pop()


# #list
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = LinkedList()

#     def __len__(self):
#         return self.size

#     def push(self, value):
#         #add one from list when value added
#         self.size +=1
#         return self.storage.add_to_tail(value)

#     def pop(self):
#         #need to make sure to remove 1 from list everytime value added
#         if self.size == 0:
#             return None
#         self.size -=1
#         return self.storage.remove_tail()
       

