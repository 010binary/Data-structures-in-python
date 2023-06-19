class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add_at_front(self, data):
        self.head = Node(data, self.head)      

    def add_at_end(self, data):
        if not self.head:
            self.head = Node(data, None)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(data, None)

    def get_last_node(self):
        n = self.head
        while(n.next != None):
            n = n.next
        return n.data

    def is_empty(self):
        return self.head == None

    def print_list(self):
        n = self.head
        while n != None:
            print(n.data, end = " => ")
            n = n.next
        print()


# creating an instance or object of the class
s = LinkedList()

# to check if the LinkedList is empty
s.print_list() 

# this creates the head
s.add_at_front(5)

# Used to add to the end of the list
s.add_at_end(8) 
s.add_at_end(5) 
s.add_at_end(7)

# declares a new head of the list and is link to the previous head
s.add_at_front(9) 

# To see or print what is in the list
s.print_list()

# as noted to get the last node in the list
print(s.get_last_node())

# to check if the list is empty
print(s.is_empty)

