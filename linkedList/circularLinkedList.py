class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class circularLinkedList:
    def __init__(self):
        self.head = None

    def insertAtEnd(self, value):
        temp = Node(value)
        if self.head != None:
            t1 = self.head
            temp.next = t1
            while t1.next != self.head:
                t1 = t1.next
            t1.next = temp
        else:
            self.head = temp
            temp.next = self.head

    def insertAtBeg(self, value):
        temp = Node(value)
        if self.head == None:
            self.head = temp
            temp.next = self.head
            return
        t1 = self.head
        while t1.next != self.head:
            t1 = t1.next
        temp.next = self.head
        self.head = temp
        t1.next = self.head

    def insertAtMid(self, value, x):
        temp = Node(value)
        t1 = self.head
        while t1.next != self.head:
            if t1.value == x:
                temp.next = t1.next
                t1.next = temp
                return
            t1 = t1.next

        if t1.value == x:
            print("cant insert middle value at the end")

    def deleteCLL(self, value):
        if self.head is None:
            return

        if self.head.value == value:
            current = self.head
            if current.next == self.head:
                self.head = None
                return
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next
            return

        t1 = self.head
        prev = None
        while True:
            prev = t1
            t1 = t1.next
            if t1 == self.head:
                break
            if t1.value == value:
                prev.next = t1.next
                return

    def printCLL(self):
        t1 = self.head
        while t1.next != self.head:
            print(t1.value, end=" <--> ")
            t1 = t1.next
        print(t1.value)


obj = circularLinkedList()
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtBeg(5)
obj.insertAtBeg(7)
obj.insertAtMid(40, 30)
obj.deleteCLL(7)
obj.printCLL()
