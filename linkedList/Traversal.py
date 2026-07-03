class Node:
    def __init__(self,data=None,next=None):
        self.info = data
        self.next = next

class SinglyLinkedlist:
    def __init__(self,head=None):
        self.head = head

    def findingNode(self,value):
        temp = self.head
        while temp != None:
            if temp.info == value:
                return temp
            temp = temp.next
        return None

    def insertAtEnd(self,value):
        newNode = Node(value)
        if(self.head != None):
            temp = self.head
            while(temp.next != None):
                temp = temp.next
            temp.next = newNode
        else:
            self.head = newNode

    def printLL(self):
        temp = self.head
        while(temp != None):
            print(temp.info)
            temp = temp.next

obj = SinglyLinkedlist()
obj.insertAtEnd(5)
obj.insertAtEnd(10)
obj.insertAtEnd(20)
node =  obj.findingNode(10)
if node:
    print(node.info)