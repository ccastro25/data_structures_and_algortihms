class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.length =0

class Que:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length =0 
    
    def enqueue(self,data):
        new_node = Node(data)
        self.length +=1
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return 
        
        tail = self.tail 
        tail.next = new_node
        self.tail = new_node
        
    def deque(self):
        head = self.head
        self.head = head.next
        self.length -=1
        return head.data

    def peek(self):
        return self.head.data