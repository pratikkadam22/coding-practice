# Only the length
from collections import defaultdict 
class Graph: 
    def __init__(self):
        self.graph = defaultdict(list) 

    def addEdge(self,u,v): 
        self.graph[u].append(v) 
 
    def dfs(self, node, dp, vis):
        vis[node] = True
        for n in self.graph[node]:
            if (not vis[n]):
                self.dfs(n, dp, vis)
            dp[node] = max(dp[node], 1 + dp[n])

    def findLongestPath(self):
        n = len(self.graph) 
        vis = [False] * (max(self.graph) + 2)
        dp = [0] * (max(self.graph) + 2)
        for i in list(self.graph):
            if not vis[i]:
                self.dfs(i, dp, vis)
        print(dp)

g = Graph() 
# g.addEdge(0, 1) 
# g.addEdge(0, 2) 
# g.addEdge(1, 2) 
# g.addEdge(2, 0) 
# g.addEdge(2, 3) 
# g.addEdge(3, 3)
g.addEdge(1, 2)  
g.addEdge(1, 3)  
g.addEdge(3, 2)  
g.addEdge(2, 4)  
g.addEdge(3, 4)   
  
g.findLongestPath() 
