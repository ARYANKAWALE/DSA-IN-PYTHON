class Node:
    def __init__(self,data,next =None):
        self.data = data
        self.next = next
    
class Linkedlist:
    def __init__(self):
        self.head = None
    
    def insertAtEnd(self,value):
        temp = Node(value)
        if(self.head != None):
            t1 = self.head
            while(t1.next != None):
                t1 = t1.next
            t1.next = temp
        else:
            self.head = temp

    def printLL(self):
        t1 = self.head
        while(t1.next != None):
            print(t1.data)
            t1 = t1.next
        print(t1.data)

    def countNodes(self):
        count = 0
        t1 = self.head
        while t1 != None:
            count += 1
            t1 = t1.next
        return count

obj = Linkedlist()
obj.insertAtEnd(1)
obj.insertAtEnd(2)
obj.insertAtEnd(3)
obj.countNodes()
obj.printLL()

Total_nodes = obj.countNodes()
print(f"\nLinked List me total {Total_nodes} nodes hain.")