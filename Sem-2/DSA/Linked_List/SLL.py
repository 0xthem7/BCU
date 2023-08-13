class Node:
    def __init__(self):
        self.next = None
        self.first = None
        self.info = 0

class SLList:
    def __init__(self):
        self.first = None
        self.last = None

    def insert_beg(self):
        element = int(input("Enter an element to insert : "))
        node = Node()
        node.info = element
        if self.first == None:
            self.first = self.last = node
            node.next = None
            print(self.first)
        else:
            node.next = self.next
            self.first = node
        if self.first == node:
            print("Beloow")

    def insert_last(self):
        element = int(input("Enter an element: "))
        node = Node()
        node.info = element
        if self.first == None:
            self.first = self.last= node
            node.next = None
        else:
            self.last.next = node
            self.last = node
            node.Next = None


    def display(self):
        if self.first == None:
            print("Empty list")
        else:
            temp = self.first
            while temp != None:
                print(temp.info, end=' ')
                temp = temp.next


lst = SLList()
lst.insert_beg()
lst.insert_beg()
lst.display()


