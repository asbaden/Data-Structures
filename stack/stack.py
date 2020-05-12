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

class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next


class LinkedList:
    def __init__(self, node=None):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        new_node = Node(value)

        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:

            if self.head == self.tail:
                self.head.next = new_node
                self.tail = new_node
            else:
                self.tail.next = new_node
                self.tail = new_node

    def remove_from_tail(self):

        if not self.head and not self.tail:
            return

        if self.head.next == None:
            value = self.head.data
            self.head = None
            self.tail = None

            return value

        else:

            current = self.head
            prev_node = None

            while current.next is not None:
                prev_node = current
                current = current.next

            data = self.tail.data
            self.tail = prev_node
            self.tail.next = None

            return data


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.size += 1
        self.storage.add_to_tail(value)

    def pop(self):
        if self.size == 0:
            return
        else:
            self.size -= 1
            return self.storage.remove_from_tail()
            




# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return self.size

#     def push(self, value):
#         self.storage.append(value)
#         self.size += 1

#     def pop(self):
#         if self.size == 0:
#             return 
#         else:
#             value = self.storage.pop()
#             self.size -= 1 
#             return value

            
