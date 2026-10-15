class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class Linkedlist:
    def __init__(self):
        self.head = None

    def printAllNumbers(self):
        # nums = 0
        t = self.head
        while(t != None):
            print(t.data,end=" ")
            t = t.next
        print()

        if(t == None):
            return
    def printWithAddress(self):
        t = self.head
        while t != None:
            print(f"Data: {t.data} -> Memory Address: {hex(id(t))}")
            t = t.next
        print()

obj = Linkedlist()
second = Node(20)
third = Node(30)
fourth = Node(40)
obj.head = Node(10,second)
second.next = third
third.next = fourth
obj.printAllNumbers()
obj.printWithAddress()