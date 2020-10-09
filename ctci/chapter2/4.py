# 2.4: Partition

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

def print_list(head):
    temp = head
    while temp:
        print(temp.val, "->", end = " ")
        temp = temp.next

def partition(node, x):
    head, tail = node, node
    while node:
        next = node.next
        if node.val < x:
            node.next = head
            head = node
        else:
            tail.next = node
            tail = node
        node = next
    tail.next = None
    return head

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
print_list(ll.head)
print("")
print("After Partition:")
res = partition(ll.head, 6)
print_list(res)