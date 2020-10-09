# 2.5: Sum Lists
# Refer Leetcode #2

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def add_lists(l1, l2):
    p, q = l1, l2
    carry = 0
    dummy = Node(0)
    curr = dummy
    while p is not None or q is not None:
        x = p.val if p else 0
        y = q.val if q else 0
        s = x + y + carry
        carry = s // 10
        curr.next = Node(s % 10)
        curr = curr.next
        if p: p = p.next
        if q: q = q.next
    if carry > 0:
        curr.next = Node(carry)
    return dummy.next

head1 = Node(2)
head1.next = Node(4)
head1.next.next = Node(3)

head2 = Node(5)
head2.next = Node(6)
head2.next.next = Node(4)

res = add_lists(head1, head2)

# Print the output list
while res:
    print(res.val, "->", end="")
    res = res.next