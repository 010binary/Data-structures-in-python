class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []
        
    def enqueue(self, item): # the enqueue methods runs in the background just like the push method in stacks
        self.items.insert(0, item)

    def dequeue(self):
        self.items.pop()

    def print_queue(self):
        print(self.items)

q = Queue()
q.enqueue('a')
q.enqueue('b')
q.enqueue('42')
q.print_queue()

q.dequeue()
q.print_queue()