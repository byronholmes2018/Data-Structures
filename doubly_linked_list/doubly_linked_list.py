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

    def add_to_head(self, value):
        if(self.head == None):
            self.head = ListNode(value, prev=None, next=None)
            self.tail = self.head
        else:
            old_head = self.head
            old_head.prev = ListNode(value, prev=None, next=old_head)
            self.head = old_head.prev

    def remove_from_head(self):
        if(self.head.next):
            old_head = self.head
            self.head = old_head.next
            self.head.prev = None
        else:
            old_head = self.head
            self.head = None
            self.tail = None
        return old_head.value

    def add_to_tail(self, value):
        if(self.tail):
            new_node = ListNode(value, prev=self.tail, next=None)
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = ListNode(value, prev=None, next=None)
            self.tail = self.head

    def remove_from_tail(self):
        if(self.tail.prev):
            old_tail = self.tail
            new_tail = old_tail.prev
            new_tail.next = None
            self.tail = new_tail
        else:
            old_tail = self.tail
            self.head = None
            self.tail = None
        return old_tail.value

    def move_to_front(self, node):
        if node.next:
            node.prev.next = node.next
            node.next.prev = node.prev

        old_head = self.head
        old_head.prev = node
        node.next = old_head
        node.prev = None
        self.head = node

    def move_to_end(self, node):
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        old_tail = self.tail
        old_tail.next = node
        node.next = None
        node.prev = old_tail
        self.tail = node

    def delete(self, node):
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if node == self.head:
            self.head = node.next
        if node == self.tail:
            self.tail = node.prev

    def get_max(self):
        max_value = self.head.value
        current_node = self.head
        while(current_node.next):
            current_node = current_node.next
            if current_node.value > max_value:
                max_value = current_node.value
        return max_value
