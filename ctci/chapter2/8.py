# 2.8: Loop Detection
# Refer Leetcode #142
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def has_cycle(head):
    slow = fast = finder = head
    while (fast and fast.next):
        slow = slow.next
        fast = fast.next.next
        if(slow == fast):
            while finder != slow:
                finder = finder.next
                slow = slow.next
            return finder
    return None

head1 = Node(3)
head1.next = Node(1)
inter = Node(5)
head1.next.next = inter
head1.next.next.next = Node(9)
head1.next.next.next.next = Node(7)
head1.next.next.next.next.next = Node(2)
head1.next.next.next.next.next.next = inter

res = has_cycle(head1)
print(res.val)
