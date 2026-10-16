class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next

class Linkedlist:
    def __init__(self):
        self.head = None

    def insertAtEnd(self,value):
        temp = Node(value)
        if(self.head != None):
            t = self.head
            while(t.next != None):
                t = t.next
            t.next = temp
        else:
            self.head = temp

    def printLL(self):
        t = self.head
        while(t.next != None):
            print(t.data)
            t = t.next
        print(t.data)

    def search(self,value):
        target = value
        t = self.head
        while(t != None):
            if(t.data == target):
                return True
            t = t.next
        return False


obj = Linkedlist()
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
print(obj.search(50))
obj.printLL()