import time

start = time.time()

class Node:
    def __init__(self):
        self.next = None
        self.info = 0

class SLL:
    def __init__(self):
        self.first = None
    
    def insert_at_beg(self, data):
        node = Node()
        node.info = data
        if self.first == None:
            self.first = node
            node.next = None
        else:
            node.next = self.first
            self.first = node
    def inset_at_end(self):
        pass
    def display(self):
        print(*self.info, end=' ')


lst = SLL()
lst.insert_at_beg(5)
lst.insert_at_beg(6)
lst.insert_at_beg(7)
lst.display()
end = time.time()
ms = (end-start) * 10**6
print(f"Elapsed time {ms:.03f} micro secs.")
