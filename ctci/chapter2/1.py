# 2.1: Remove Dups

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

# This method uses a Set as buffer. Time: O(n)
def remove_dups(head):
    s = set()
    temp, prev = head, None
    while temp:
        if temp.val in s:
            prev.next = temp.next
        else:
            s.add(temp.val)
            prev = temp
        temp = temp.next

# This method does not use any buffer space. Time: O(n^2), Space: O(1)
def remove_dups_no_buffer(head):
    current = head
    while current:
        runner = current
        while runner.next:
            if runner.next.val == current.val:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next

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
remove_dups(ll.head)
# remove_dups_no_buffer(ll.head)
print("After removing duplicates:")
ll.print_list()