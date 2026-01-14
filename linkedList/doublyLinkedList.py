class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLL:
    def __init__(self):
        self.head = None

    def insertAtEnd(self, value):
        temp = Node(value)
        if self.head == None:
            self.head = temp
            return

        t = self.head
        while t.next != None:
            t = t.next

        t.next = temp
        temp.prev = t

    def insertAtBeg(self, value):
        temp = Node(value)
        if self.head == None:
            self.head = temp
            return
        temp.next = self.head
        self.head.prev = temp
        self.head = temp

    def insertAtMid(self, value, x):
        t = self.head
        while t.next != None:
            if t.value == x:
                break
            t = t.next
        if t == None:
            print(f"Node with {x} not found")
            return
        temp = Node(value)
        temp.next = t.next
        t.next.prev = temp
        t.next = temp
        temp.prev = t

    def deleteDLL(self, value):
        if self.head == None:
            print("Linked list is Empty")
            return

        t = self.head
        if t.value == value:
            self.head = t.next
            if self.head != None:
                self.head.prev = None
            return
        while t != None:
            if t.value == value:
                t.prev.next = t.next
                if t.next != None:
                    t.next.prev = t.prev
                return
            else:
                t = t.next

    def printDLL(self):
        t1 = self.head
        while t1.next != None:
            print(t1.value, end=" <--> ")
            t1 = t1.next
        print(t1.value)


obj = DoublyLL()
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtEnd(40)
obj.insertAtBeg(5)
obj.insertAtMid(15, 10)
obj.deleteDLL(30)
obj.printDLL()
