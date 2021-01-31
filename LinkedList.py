# Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    # Method to push a new node from the list
    def push(self, data):
        newNode = Node(data)
        # Head is empty
        if self.head == None:
            self.head = newNode
            return
        
        temp = self.head
        # Go to the last node of the list
        # and then push the new node
        while temp.next:
            temp = temp.next
        
        temp.next = newNode

    # Method to Remove a node from the list
    def remove(self, data):
        # if list is empty
        if self.head == None:
            print('Error: Cannot remove the node as list is empty')
            return
        
        # if data of head equals data to be deleted
        if self.head.data == data:
            self.head = self.head.next
            return

        temp = self.head
        
        while temp.next:
            if temp.next.data == data:
                temp.next = temp.next.next
                return
            temp = temp.next
        
        print('Node not found')

    # Method to search a node in the list
    def search(self, data):
        temp = self.head
        i = 1
        
        while (temp is not None):
            if temp.data == data:
                return i
            temp = temp.next
            i = i + 1
            
        return -1
    
    # Method to update data of a node in list
    def update(self, oldData, newData):
        temp = self.head
        
        while temp:
            if temp.data == oldData:
                temp.data = newData
                return
            temp = temp.next
    
    # Method to insert a data to the list at a given position
    def insert(self, data, pos):
        if pos < 1:
            return print('Error: Position cannot be negative or zero')
        
        if pos == 1:
            oldHead = self.head
            self.head = Node(data)
            self.head.next = oldHead
            return
        
        temp = self.head
        
        # Go to the node at position pos-1
        for i in range(1, pos-1):
            temp = temp.next
            if temp == None:
                return print('Error: Position exceeded')
        
        oldNode = temp.next
        temp.next = Node(data)
        temp.next.next = oldNode
    
    # Method to reverse the linked list
    def reverse(self):
        current = self.head
        prev = None
        
        while current != None:
            next = current.next
            current.next = prev
            prev = current
            current = next
         
        self.head = prev
        
    # Recursive methods
    def recursivePrint(self, node):
        if node is None:
            return
        print(node.data)
        # Recursive Call
        self.recursivePrint(node.next)
    
    # Method to print elements using recursion
    def recursiveReversePrint_1(self, node):
        if node is None:
            return
        # Recursive Call
        self.recursiveReversePrint(node.next)
        print(node.data)
    
    # Method to reverse the linked list using recursion - my solution
    def recursiveReverse_1(self, current, prev = None):
        if current is None:
            self.head = prev
            return

        next = current.next
        current.next = prev
        
        self.recursiveReverse_1(next, current)
    
    # Two solutions of Reversing a linked list using recursion
    # Method to reverse the linked list using recursion - solution from mycodeschool
    def recursionReverse_2(self, node):
        if node.next is None:
            self.head = node
            return
        
        self.recursionReverse_2(node.next)
        
        next = node.next
        next.next = node
        node.next = None
        
    # Method to print all the datas of the nodes of the list
    def print(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


list = LinkedList()

list.push(1)
list.push(2)
list.push(3)
list.push(4)
list.push(5)
list.push(6)

# list.remove(2)
# list.remove(4)
# list.remove(5)
# list.remove(11)

# print(list.search(6))

# list.update(2, -2)

# list.insert(9, 4)


# list.reverse()
# list.print()

# list.recursivePrint(list.head)
# list.recursiveReversePrint(list.head)

# list.recursiveReverse_1(list.head)
# list.print()
# print(list.head.data)

list.recursionReverse_2(list.head)
list.print()