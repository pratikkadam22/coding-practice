# 2.7: Intersection
# Refer Leetcode #160
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def find_intersection(headA, headB):
    if headA is None or headB is None:
        return None
    pa = headA
    pb = headB
    
    while (pa != pb):
        if(pa is None):
            pa = headB
        else:
            pa = pa.next  
        if(pb is None):
            pb = headA
        else:
            pb = pb.next
    return pa

head1 = Node(3)
head1.next = Node(1)
head1.next.next = Node(5)
head1.next.next.next = Node(9)
inter = Node(7)
head1.next.next.next.next = inter
head1.next.next.next.next.next = Node(2)
head1.next.next.next.next.next.next = Node(1)

head2 = Node(4)
head2.next = Node(6)
head2.next.next = inter
head2.next.next.next = Node(2)
head2.next.next.next.next = Node(1)

res = find_intersection(head1, head2)
print(res.val)