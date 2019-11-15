import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList
class Queue:
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, item):
        self.storage.add_to_tail(item)
        self.size += 1

    def dequeue(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_from_head()

    def len(self):
        return self.size




class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
       next = self
       while(next):
         if value > next.value:
           if next.right is None:
             next.right = BinarySearchTree(value)
             next = None
           else:
             next = next.right
         elif value < next.value:
           if next.left is None:
             next.left = BinarySearchTree(value)
             next = None
           else:
             next = next.left
    




    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        next = self
        while(next):
          if target == next.value:
            return True
          elif target > next.value:
            if next.right is None:
              return False
            else:
              next = next.right
          else:
            if next.left is None:
              return False
            else:
              next = next.left

    # Return the maximum value found in the tree
    def get_max(self):
        max = 0
        next = self
        while(next):
          if next.value > max:
            max = next.value
          next = next.right
        return max

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        queue = Queue()
        if self.left is not None:
          queue.enqueue(self.left)
        if self.right is not None:
          queue.enqueue(self.right)
        while(queue.len() > 0):
          node_to_eval = queue.dequeue()
          cb(node_to_eval.value)
          if node_to_eval.left is not None:
            queue.enqueue(node_to_eval.left)
          if node_to_eval.right is not None:
            queue.enqueue(node_to_eval.right)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass