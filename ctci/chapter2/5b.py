# 2.5: Sum Lists (Follow Up)
# Refer Leetcode #445
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def add_lists(l1, l2):
    len1, len2 = 0, 0
    t1, t2 = l1, l2
    while t1:
        len1 += 1
        t1 = t1.next
    while t2:
        len2 += 1
        t2 = t2.next
    t1, t2, head1 = l1, l2, None
    while len1 > 0 or len2 > 0:
        val = 0
        if len1 >= len2:
            val += t1.val
            len1 -= 1
            t1 = t1.next
        if len2 > len1:
            val += t2.val
            len2 -= 1
            t2 = t2.next
        curr = Node(val)
        curr.next = head1
        head1 = curr
    curr1, head, carry = head1, None, 0
    while curr1:
        val = (curr1.val + carry) % 10
        carry = (curr1.val + carry) // 10
        curr2 = Node(val)
        curr2.next = head
        head = curr2
        curr1 = curr1.next
    if carry > 0:
        curr = Node(carry)
        curr.next = head
        head = curr
    return head

head1 = Node(7)
head1.next = Node(2)
head1.next.next = Node(4)
head1.next.next.next = Node(3)

head2 = Node(5)
head2.next = Node(6)
head2.next.next = Node(4)

res = add_lists(head1, head2)

# Print the output list
while res:
    print(res.val, "->", end="")
    res = res.next