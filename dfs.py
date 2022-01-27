from collections import defaultdict 
  
# This class represents a directed 
# using adjacency list representation 
class Graph: 
  
    # Constructor 
    def __init__(self): 
  
        # default dictionary to store graph 
        self.graph = defaultdict(list) 
  
    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    # Function to print a DFS of graph 
    def DFS(self, s): 
  
        # Mark all the vertices as not visited 
        visited = [False] * (len(self.graph)) 
  
        # Create a stack for DFS 
        stack = [] 
  
        # Mark the source node as  
        # visited and enstack it 
        stack.append(s) 
  
        while(len(stack)): 
  
            # Destack a vertex from  
            # stack and print it 
            s = stack[-1]
            stack.pop() 

            if (not visited[s]):
                print(s,end=' ') 
                visited[s] = True

            for node in self.graph[s]:  
                if (not visited[node]):  
                    stack.append(node)
  
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
g.DFS(2) 
