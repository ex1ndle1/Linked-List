class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_all_list(self):
        current : Node = self.head

        if not current:
            print('list is empty')
            return
        
        while current:
            print(current.data )
            current = current.next

        print('None')
my_list = LinkedList()
first = Node(10)
second  = Node(20)
third = Node(30)
my_list.head = first
first.next  = second
second.next = third




class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
      
        return len(self.items) == 0

    def enqueue(self, item):

        self.items.append(item)


    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def print_all(self):
        print( self.items)




class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self,new_item):
        self.stack.append(new_item)
    
    def pop(self):
        if not self.is_empty():
            self.stack.pop()
            return
        return -1
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
    def peek(self):
        return self.stack[-1]
    
    def rest(self):
        return  Stack