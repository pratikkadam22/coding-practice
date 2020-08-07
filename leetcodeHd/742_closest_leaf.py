from collections import defaultdict

class Node: 
    def __init__(self, key): 
        self.key = key 
        self.left, self.right = None, None

class Solution:
    def __init__(self):
        self.start, self.k = None, 0
        self.adjList = defaultdict(list)

    def closestLeaf(self, root, k):
        self.k = k
        self.buildGraph(root, None)
        visited = set()
        queue = []
        queue.append(self.start)
        visited.add(self.start)
        while queue:
            x = queue.pop(0)
            visited.add(x)
            if x.left is None and x.right is None:
                return x.key
            for nextNode in self.adjList[x]:
                if nextNode not in visited:
                    visited.add(nextNode)
                    queue.append(nextNode)
        return -1

    def buildGraph(self, curr_node, parent):
        if curr_node is None:
            return
        if curr_node.key == self.k:
            self.start = curr_node
        if parent:
            self.adjList[parent].append(curr_node)
            self.adjList[curr_node].append(parent)
        self.buildGraph(curr_node.left, curr_node)
        self.buildGraph(curr_node.right, curr_node)

root = Node(1)
root.right = Node(3)
root.left = Node(2)
root.left.left = Node(4)
root.left.left.left = Node(5)
root.left.left.left.left = Node(6)

s = Solution()
print(s.closestLeaf(root, 2))

# Description of the question:
# https://protegejj.gitbook.io/algorithm-practice/leetcode/tree/742-closest-leaf-in-a-binary-tree

