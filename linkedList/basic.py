class Node:
    def __init__(self,val,next=None):
        self.data = val
        self.next = next

class Linkedlist:
    def __init__(self):
        self.head = None

    def insertAtBeg(self,value):
        temp = Node(value)
        temp.next = self.head
        self.head = temp
    
    def findMiddle(self):
        slow = self.head
        fast = self.head
        while(fast!= None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
        return slow

    def printLL(self):
        t1 = self.head
        while(t1.next != None):
            print(t1.data)
            t1 = t1.next
        print(t1.data)

    def findCycle(self):
        slow = self.head
        while(fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
            if(slow == fast):
                return True
            else:
                return False


obj = Linkedlist()
obj.insertAtBeg(10)
obj.insertAtBeg(20)
obj.insertAtBeg(30)
obj.insertAtBeg(40)
obj.insertAtBeg(50)
obj.insertAtBeg(60)
obj.insertAtBeg(70)
print(obj.findMiddle().data)
obj.printLL()
print(obj.findCycle())
print(obj.startPoint())
