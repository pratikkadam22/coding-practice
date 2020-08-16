# Prints the longest path in acyclic directed graph
from collections import defaultdict 
class Graph:
    def __init__(self, n):
        self.V = n
        self.graph = defaultdict(list)
        self.inDegree = [True] * (self.V + 1)
        self.outDegree = [True] * (self.V + 1)
        self.paths = set()

    def addEdge(self, u, v): 
        self.graph[u].append(v)
        self.inDegree[v], self.outDegree[u] = False, False
 
    def dfs(self, s, visited, path):
        path.append(s) 
        visited[s] = True
        if self.outDegree[s] and self.inDegree[path[0]]:
            self.paths.add(tuple(path))
        for node in self.graph[s]: 
            if not visited[node]: 
                self.dfs(node, visited, path)
        path.pop() 
        visited[s] = False

    def findLongestPath(self):
        for i in list(self.graph):
            if self.inDegree[i] and self.graph[i]: 
                path = [] 
                visited = [False] * (self.V + 1) 
                self.dfs(i, visited, path)
        print(self.paths)

g = Graph(4) 
g.addEdge(1, 2)  
g.addEdge(1, 3)  
g.addEdge(3, 2)  
g.addEdge(2, 4)  
g.addEdge(3, 4)   
  
g.findLongestPath()
