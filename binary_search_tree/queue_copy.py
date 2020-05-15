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

    def add_to_head(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def add_to_tail(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            if self.head == self.tail:
                self.head.next = new_node
                self.tail = new_node
            else:
                self.tail.next = new_node
                self.tail = new_node

    def remove_from_head(self):

        if not self.head and not self.tail:
            return
        else:
            data = self.head.data

            if self.head == self.tail:
                self.head = None
                self.tail = None
                return data
            else:
                data = self.head.data
                self.head = self.head.next
                return data

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
        self.head = None
        self.tail = None
  
    
    def __len__(self):
        return self.size
    

    def enqueue(self, value):
        self.size += 1
        self.storage.add_to_tail(value)
        
    def dequeue(self):
        if self.size == 0:
            return
        else:
            self.size -= 1
            return self.storage.remove_from_head()
       