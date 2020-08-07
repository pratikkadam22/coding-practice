from collections import defaultdict 
  
# This class represents a directed graph 
# using adjacency list representation 
class Graph: 
  
    # Constructor 
    def __init__(self): 
  
        # default dictionary to store graph 
        self.graph = defaultdict(list) 
  
    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    # Function to print a BFS of graph 
    def BFS(self, s, d): 
  
        # Mark all the vertices as not visited 
        visited = [False] * (len(self.graph)) 

        distance = [0] * (len(self.graph))
  
        # Create a queue for BFS 
        queue = [] 
  
        # Mark the source node as  
        # visited and enqueue it 
        queue.append(s) 
        visited[s] = True
        distance[s] = 0
        levels = {}
        while queue: 
  
            # Dequeue a vertex from  
            # queue and print it 
            s = queue.pop(0) 
            # print (s, end = " ")
            levels[s] = 0 

            # Get all adjacent vertices of the 
            # dequeued vertex s. If a adjacent 
            # has not been visited, then mark it 
            # visited and enqueue it 
            for i in range(len(self.graph[s])): 
                if visited[self.graph[s][i]] == False:
                    distance[self.graph[s][i]] = distance[s] + 1
                    queue.append(self.graph[s][i]) 
                    visited[self.graph[s][i]] = True
        for i in levels.keys():
            levels[i] = distance[i]
        print(levels[d])
  
# Driver code 
  
# Create a graph given in 
# the above diagram 
g = Graph()
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
  
print ("Following is Breadth First Traversal"
                  " (starting from vertex 2)") 
g.BFS(2, 1) 