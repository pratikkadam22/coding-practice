# 2.6: Palindrome
# Refer Leetcode #234
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def is_palindrome(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    node = None
    while slow:
        nxt = slow.next
        slow.next = node
        node = slow
        slow = nxt
    while node:
        if node.val != head.val:
            return False
        node = node.next
        head = head.next
    return True

head1 = Node(1)
head1.next = Node(2)
head1.next.next = Node(2)
head1.next.next.next = Node(1)

head2 = Node(1)
head2.next = Node(2)
head2.next.next = Node(3)
head2.next.next.next = Node(1)

head3 = Node(4)
head3.next = Node(3)
head3.next.next = Node(10)
head3.next.next.next = Node(3)
head3.next.next.next.next = Node(4)

print(is_palindrome(head1))
print(is_palindrome(head2))
print(is_palindrome(head3))

