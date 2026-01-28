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
            print(current.data)
            current = current.next

        print('None')
my_list = LinkedList()
x = Node(10)
my_list.head = x
print(my_list.print_all_list())