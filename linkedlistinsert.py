class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

#if __name__=='__main__':
llist = linkedlist()
llist.head = Node(2)
second = Node(5)
third = Node(8)

llist.head.next = second
second.next = third
while(llist.head):
    # print('{} -> '.format(llist.head.data), end=' ')
    print(llist.head.data, end = ' -> ')
    llist.head = llist.head.next
    # print("This is the created linkedlist:")
    # print("{0} -> {1} -> {2}".format(llist.head.data, second.data, third.data))