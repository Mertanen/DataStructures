class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
  
class LinkedList:
    def __init__(self):
        self.head = None
            
    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node
        
    def insertAtIndex(self, data, index):
        new_node = Node(data)
        current_node = self.head
        position = 0
        if position == index:
            self.insertAtBegin(data)
        else:
            while current_node != None and position + 1 != index :
                position += 1
                current_node = current_node.next
                
            if current_node != None:
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                raise ValueError("Index not defined")
            
    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return 
        
        current_node = self.head
        while(current_node.next):
            current_node = current_node.next
            
        current_node.next = new_node
        
    def updateNode(self, newData, index):
        current_node = self.head
        position = 0
        if position == index:
            current_node.data = newData
            return 
        else:
            while current_node != None and position != index:
                position += 1
                current_node = current_node.next
                
            if current_node != None:
                current_node.data = newData
            else:
                raise ValueError("Index not defined")
            
    def removeFirstNode(self):
        if self.head == None:
            return
        
        self.head = self.head.next
        
    def removeLastNode(self):
        current_node = self.head
        while current_node.next.next:
            current_node = current_node.next
            
        current_node.next = None
        
    def removeNodeAtIndex(self, index):
        if self.head == None:
            return
        
        current_node = self.head
        position = 0
        if position == index:
            self.removeFirstNode()
        else:
            while current_node != None and position + 1 != index:
                position += 1
                current_node = current_node.next
                
            if current_node != None:
                current_node.next = current_node.next.next
            else:
                raise ValueError("Index not defined")
            
    def removeNode(self, data):
        current_node = self.head
        
        while current_node != None and current_node.next.data != data:
            current_node = current_node.next
            
        if current_node == None:
            return
        else:
            current_node.next = current_node.next.next
            
    def sizeOfLinkedList(self):
        size = 0
        current_node = self.head
        while current_node:
            current_node = current_node.next
            size += 1
            
        return size
    
    def printLinkedList(self):
        linkedList = []
        current_node = self.head
        while current_node:
            linkedList.append(current_node.data)
            current_node = current_node.next
        
        if len(linkedList) == 0:
            print("List is empty")
        else:
            print(' -> '.join(linkedList))
            
            
llist = LinkedList()

llist.insertAtEnd('a')
llist.insertAtEnd('b')
llist.insertAtBegin('c')
llist.insertAtEnd('d')
llist.insertAtIndex('g', 2)
 
print("Node Data")
llist.printLinkedList()
 
print("\nRemove First Node")
llist.removeFirstNode()
print("Remove Last Node")
llist.removeLastNode()
print("Remove Node at Index 1")
llist.removeNodeAtIndex(1)
 
 
print("\nLinked list after removing a node:")
llist.printLinkedList()
 
print("\nUpdate node Value")
llist.updateNode('z', 0)
llist.printLinkedList()
 
print("\nSize of linked list :", end=" ")
print(llist.sizeOfLinkedList())