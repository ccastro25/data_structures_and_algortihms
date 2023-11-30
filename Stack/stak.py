class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.length =0

    def push(self,data):
        new_node = Node(data)
        self.length +=1
        if not self.head:
             self.head = new_node
             return 

        head = self.head
        new_node.next = head
        self.head = new_node
        
    def pop(self):
        head = self.head
        self.head = head.next
        self.length -=1
        return head.data


    def peek(self):
        return self.head.data