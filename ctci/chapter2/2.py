# 2.2: Return Kth to the Last

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

# This recursive function takes O(n) space.
def kth_to_last(head, k):
    if not head:
        return 0
    index = kth_to_last(head.next, k) + 1
    if index == k:
        print("The kth last element is:", head.val)
    return index

# This iterative two pointer approach takes O(n) time and O(1) space
def nth_to_last(head, k):
    p1, p2 = head, head
    for i in range(k):
        if not p1:
            return None
        p1 = p1.next
    while p1:
        p1 = p1.next
        p2 = p2.next
    return p2

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
kth_to_last(ll.head, 2)
res = nth_to_last(ll.head, 4)
print(res.val)