# 314. Binary Tree Vertical Order Traversal (Medium)
from collections import defaultdict
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left, self.right = None, None

def verticalTraversal(root):
    dic = defaultdict(list)
    queue = [(root, 0)]
    minD, maxD = float('inf'), float('-inf')
    res = []
    while queue:
        curr, D = queue.pop(0)
        dic[D].append(curr.key)
        minD = min(minD, D)
        maxD = max(maxD, D)
        if curr.left:
            queue.append((curr.left, D - 1))
        if curr.right:
            queue.append((curr.right, D + 1))
    for i in range(minD, maxD + 1):
        res.append(dic[i])
    return res

# root = TreeNode(3)
# root.left = TreeNode(9)
# root.right = TreeNode(20)
# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)

root = TreeNode(0)
root.right = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.left.left = TreeNode(4)
root.left.left.right = TreeNode(5)
root.left.left.left.right = TreeNode(7)
root.left.left.right.left = TreeNode(6)
root.left.left.left.right.left = TreeNode(10)
root.left.left.left.right.right = TreeNode(8)
root.left.left.right.left.left = TreeNode(11)
root.left.left.right.left.right = TreeNode(9)


ans = verticalTraversal(root)
print(ans)




