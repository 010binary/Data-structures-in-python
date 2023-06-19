class Graph(): 
    #adj is the name of the empty 2 dimension list
    def __init__(self, size): 
        self.adj = [ [0] * size for i in range(size)] #list comprehension to get the size and set all values to 0
        self.size = size # the size of the Graph vertically
    
    def add_edge(self, orig, destination): 
        if (orig > self.size) or (destination > self.size) or (orig < 0 or destination < 0): 
            print("Invalid Edge") 
        else: 
            self.adj[orig-1][destination-1] = 1 
            self.adj[destination-1][orig-1] = 1 
        
    def remove_edge(self, orig, destination): 
        if (orig > self.size) or (destination > self.size) or (orig < 0 or destination < 0): 
            print("Invalid Edge") 
        else: 
            self.adj[orig-1][destination-1] = 0 
            self.adj[destination-1][orig-1] = 0 
            
    def display(self): 
        for row in self.adj: 
            print() 
            for val in row: 
                print('{:4}'.format(val),end="") 

#a sample Graph 
G = Graph(4) # This controls the number of colunms an the default values is 0
G.add_edge(1, 3) 
G.add_edge(3, 4)
G.add_edge(2, 4)
G.display()