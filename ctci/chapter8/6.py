class Tower:
    def __init__(self, tnum):
        self.stack = []
        self.tnum = tnum

    def get_num(self):
        return self.num
    
    def add(self, num):
        if len(self.stack) > 0 and self.stack[-1] <= num:
            print("Invalid Disk Placement!")
        else:
            self.stack.append(num)
    
    def move_top(self, destination):
        t = self.stack.pop()
        destination.add(t)
    
    def move_disks(self, n, destination, buffer):
        if n <= 0:
            return
        self.move_disks(n - 1, buffer, destination)
        self.move_top(destination)
        buffer.move_disks(n - 1, destination, self)

def towers_of_hanoi(num_of_disks):
    towers = [Tower(i) for i in range(3)]
    for i in range(num_of_disks, 0, -1):
        towers[0].add(i)
    print(towers[0].stack, towers[1].stack, towers[2].stack)

    towers[0].move_disks(num_of_disks, towers[2], towers[1])
    
    print(towers[0].stack, towers[1].stack, towers[2].stack)

towers_of_hanoi(6)

