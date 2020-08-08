# 426. Convert Binary Search Tree to Sorted Doubly Linked List (Medium)

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left, self.right = None, None

def treeToDoublyList(root):
    if not root:
        return None
    stack = []
    curr, pre, head = root, None, None
    while True:
        if curr:
            stack.append(curr)
            curr = curr.left
        elif(stack):
            curr = stack.pop()
            if not pre:
                head = curr
            else:
                pre.right = curr
                curr.left = pre
            pre = curr
            curr = curr.right
        else:
            break
    pre.right = head
    head.left = pre
    return head
    
root = TreeNode(4)
root.right = TreeNode(5)
root.left = TreeNode(2)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

head = treeToDoublyList(root)

headOfList = head
while head:
    print(head.left.key, '<--', head.key, '-->', head.right.key)
    head = head.right
    if head == headOfList:
        break