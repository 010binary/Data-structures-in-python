# Data Structures in python


## Python graph
This code defines a `Graph` class that represents an undirected graph using an adjacency matrix. The class has the following methods:

Here is a concise explanation of the code:

- **`__init__(self, size)`**: Initializes the graph with a given size (number of vertices) and creates an empty 2-dimensional list called `adj` with all values set to 0.

- **`add_edge(self, orig, destination)`**: Adds an edge between two vertices by setting the corresponding elements in the adjacency matrix to 1. The vertices are represented by their indices (starting from 1).

- **`remove_edge(self, orig, destination)`**: Removes an edge between two vertices by setting the corresponding elements in the adjacency matrix to 0.

- **`display(self)`**: Displays the adjacency matrix of the graph.

The code then creates an instance of the `Graph` class with a size of 4. It adds several edges between vertices using the `add_edge` method, and finally, it displays the adjacency matrix using the `display` method.

The adjacency matrix represents the connections between vertices in the graph. If there is an edge between two vertices, the corresponding element in the matrix is 1; otherwise, it is 0.


## Python queue
The code defines a `Queue` class that implements a basic queue data structure **[FIFO] `FISRT IN FIRST OUT `** using a list. It provides methods to check if the queue is empty, enqueue (add) an item to the queue, dequeue (remove) an item from the queue, and print the contents of the queue.

Here is a concise explanation of the code:

- **`__init__(self)`**: Initializes the queue with an empty list as the underlying data structure.

- **`is_empty(self)`**: Checks if the queue is empty by returning `True` if the `items` list is empty, `False` otherwise.

- **`enqueue(self, item)`**: Adds an item to the queue by inserting it at the beginning of the `items` list using the `insert` method.

- **`dequeue(self)`**: Removes an item from the queue by using the `pop` method on the `items` list without specifying an index (which removes the first item).

- **`print_queue(self)`**: Prints the contents of the queue by displaying the `items` list.

The code creates an instance of the `Queue` class, enqueues three items ('a', 'b', and '42'), and prints the contents of the queue after each enqueue operation. Then it dequeues an item and prints the updated queue.


## Python stacks
The code defines a `Stack` class that implements a basic stack data structure **[LIFO] `LAST IN FIRST OUT`** using a list. It includes methods to check if the stack is empty, push (add) an item onto the stack, pop (remove) an item from the stack, and print the contents of the stack.

Here's a concise explanation of the code:

- **`__init__(self)`**: Initializes the stack with an empty list named `items`.

- **`is_empty(self)`**: Checks if the stack is empty by comparing the `items` list to an empty list.

- **`push(self, item)`**: Adds an item to the stack by inserting it at the beginning of the `items` list.

- **`pop(self)`**: Removes and returns the top item from the stack by using the `pop` method on the `items` list with an index of 0.

- **`print_stack(self)`**: Displays the contents of the stack by printing the `items` list.

The code creates a `Stack` instance, pushes three items ('a', 'b', and 'c') onto the stack, and prints the stack after each push operation. It then pops an item from the stack and prints the updated stack.


## Python linked list
The code defines a `Node` class that represents a single node in a linked list, and a `LinkedList` class that implements basic operations on the linked list. The code creates an instance of the `LinkedList` class, adds nodes to the front and end of the list, retrieves the last node's data, checks if the list is empty, and prints the contents of the list.

Here's a condensed explanation of the code:

- **`Node`** class: Represents a node in the linked list, with `data` and `next` attributes.

- **`LinkedList`** class: Represents a linked list with a `head` attribute initially set to `None`.

- **`add_at_front(self, data)`**: Adds a new node with the given data at the front of the list by updating the `head` pointer.

- **`add_at_end(self, data)`**: Adds a new node with the given data at the end of the list by traversing the list and updating the `next` pointers.

- **`get_last_node(self)`**: Traverses the list to find and return the data of the last node.

- **`is_empty(self)`**: Checks if the list is empty by comparing the `head` pointer to `None`.

- **`print_list(self)`**: Prints the contents of the list by traversing the list and displaying the data of each node.

The code creates an instance of the `LinkedList` class, prints an empty list, adds nodes to the front and end of the list, prints the updated list, retrieves and prints the data of the last node, and checks if the list is empty.
### [for more on linked list](https://www.tutorialspoint.com/python_data_structure/python_linked_lists.htm#:~:text=Singly%20linked%20lists%20can%20be,to%20the%20current%20data%20element.)
