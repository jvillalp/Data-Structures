"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        #create a new node prev = none , next = none
        new_node = ListNode(value, None, None)
        # check if the DLL is empty:
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node 
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length +=1


    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        #want the value of the removed node returned
        #if DLL is empty
        if not self.head and not self.tail:
            return None
            #more than one item
        else:
            value = self.head.value
            self.length -= 1
            if self.tail == self.head:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
            return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        # empty
        # 1 or more
        new_node = ListNode(value, None, None)
        # check if the DLL is empty:
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node 
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length +=1

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        if not self.head and not self.tail:
            return None
            #more than one item
        else:
            value = self.tail.value
            self.length -= 1
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None
            return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        if not node:
            return
        if self.head == self.tail:
            return
        if node == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        node.next = self.head
        self.head = node
        node.prev = None

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        if not node:
            return
        if self.head == self.tail:
            return
        if node == self.head:
            self.head = self.head.next
            self.head.prev = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        node.prev = self.tail
        node.prev.next = node
        self.tail = node
        node.next = None

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        if not node:
            return None
        if node == self.head and node == self.tail:
            self.head = None
            self.tail = None
        else:
            if node.prev:
                node.prev.next = node.next
            if node.next:                
                node.next.prev = node.prev
            if node == self.head:
                self.head = node.next
            if node == self.tail:
                self.tail = node.prev
        self.length -= 1
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        head = self.head
        if not head:
            return 0
        maxval = head.value
        while head.next:
            if head.value > maxval:
                maxval = head.value
            head = head.next
        if head.value > maxval:
            maxval = head.value
        return maxval
