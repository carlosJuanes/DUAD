"""4 - Create an object structure that represents a basic queue (Queue) with linked objects."""

class Node:
    data: str
    next: "Node"
    
    def __init__(self, data, next=None):
        self.data=data
        self.next=next

class Queue:
    head: Node

    def __init__(self):
        self.head=None

    def enqueue(self, data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        current_node=self.head
        while current_node.next is not None:
            current_node=current_node.next
        current_node.next=new_node

    def dequeue(self):
        if self.head is None:
            return None
        remove_data=self.head.data
        self.head=self.head.next
        print(f'"{remove_data}"')
        return remove_data
    
    def print_all(self):
        current_node=self.head
        output=" "
        while current_node is not None:
            output+=str(current_node.data)
            current_node=current_node.next
            if current_node is not None:
                output+=" -> "
        print(output)

q=Queue()
print("_____ADDING DATA_____")
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.enqueue("D")
q.enqueue("E")
q.enqueue("F")
q.print_all()
print("_____DELETING DATA_____")
q.dequeue()
q.dequeue()
print("_____FINAL PRINT_____")
q.print_all()