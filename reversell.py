class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, newdata):
        newnode = Node(newdata)
        newnode.next = self.head
        self.head = newnode

    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def recursivereverse(self, head):
        if (head is None or head.next is None):
            return head
        p = self.recursivereverse(head.next)
        head.next.next = head
        head.next = None
        return p

    def printlist(self):
        lastone = self.head
        while(lastone is not None):
            print(lastone.data, end=' ')
            lastone = lastone.next

llist = LinkedList()
llist.push(4)
llist.push(5)
llist.push(6)
llist.push(7)
llist.printlist()
llist.reverse()
print("")
llist.printlist()
print("")
list2 = LinkedList()
list2.head = llist.recursivereverse(llist.head)
#llist.recursivereverse(llist.head)
list2.printlist()