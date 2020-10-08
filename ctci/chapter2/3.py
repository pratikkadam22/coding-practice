# 2.3: Delete Middle Node

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class linked_list:
    def __init__(self):
        self.head = None
    
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
    
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.val, "->", end = " ")
            temp = temp.next

# Time and Space complexity: O(1)
def delete_node(node):
    node.val = node.next.val
    node.next = node.next.next

# 8->3->6->3->7->4->9->8->2
ll = linked_list()
ll.append(8)
ll.append(3)
ll.append(6)
ll.append(3)
ll.append(7)
ll.append(4)
ll.append(9)
ll.append(8)
ll.append(2)

ll.print_list()
print("")
delete_node(ll.head.next.next.next)
ll.print_list()