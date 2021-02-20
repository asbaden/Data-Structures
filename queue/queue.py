"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""

# class Node:
#     def __init__(self, data, next_node=None):
#         self.data = data
#         self.next = next_node

#     def get_data(self):
#         return self.data

#     def get_next(self):
#         return self.next

#     def set_next(self, new_next):
#         self.next = new_next


# class LinkedList:
#     def __init__(self, node=None):
#         self.head = None
#         self.tail = None

#     def add_to_head(self, data):
#         new_node = Node(data)

#         if not self.head:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             new_node.next = self.head
#             self.head = new_node

#     def add_to_tail(self, data):
#         new_node = Node(data)

#         if not self.head:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             if self.head == self.tail:
#                 self.head.next = new_node
#                 self.tail = new_node
#             else:
#                 self.tail.next = new_node
#                 self.tail = new_node

#     def remove_from_head(self):

#         if not self.head and not self.tail:
#             return
#         else:
#             data = self.head.data

#             if self.head == self.tail:
#                 self.head = None
#                 self.tail = None
#                 return data
#             else:
#                 data = self.head.data
#                 self.head = self.head.next
#                 return data

# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = LinkedList()
  
    
#     def __len__(self):
#         return self.size
    

#     def enqueue(self, value):
#         self.size += 1
#         self.storage.add_to_tail(value)
        
#     def dequeue(self):
#         if self.size == 0:
#             return
#         else:
#             self.size -= 1
#             return self.storage.remove_from_head()
       


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []
  
    
    def __len__(self):
        return self.size
    def is_empty(self):
        return self.size == 0

    def enqueue(self, value):
        self.storage.append(value)
        self.size += 1
    
    def dequeue(self):
       if self.size == 0:
            return
       else:
           self.size -= 1
           data = self.storage[0]
           self.storage.pop(0)
           return data
