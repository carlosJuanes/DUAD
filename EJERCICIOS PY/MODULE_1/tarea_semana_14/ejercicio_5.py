"""Create a LinkedList class with the following methods:

insert_front(data): Inserts at the beginning (front).
insert_back(data): Inserts at the end (back).
delete(data): Removes the first node with the given value.
print_all(): Prints all values."""

class Node:
    data:str
    next:"Node"
    def __init__(self, data, next=None):
        self.data=data
        self.next=next

class LinkedList:
    head=Node
    def __init__(self):
        self.head=None

    def insert_front(self, data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def insert_back(self, data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        current_node=self.head
        while(current_node.next is not None):
            current_node=current_node.next
        current_node.next=new_node

    def delete(self, data):
        current_node=self.head
        previous_node=None
        if current_node is None:
            return False
        
        if current_node.data==data:
            self.head=current_node.next
            return True
        
        while current_node is not None and current_node.data!=data:
            previous_node=current_node
            current_node=current_node.next

        if current_node is not None:
            previous_node.next=current_node.next
            return True
        return False

    def print_all(self):
        current_node=self.head
        output=" "
        while(current_node is not None):
            output+=str(current_node.data)
            current_node=current_node.next
            if current_node is not None:
                output+=" -> "
        print(output)
ll=LinkedList()
ll.insert_front(10)
ll.insert_front(20)
ll.insert_front(30)
ll.insert_front(40)
ll.insert_front(50)
ll.print_all()
ll.delete(10)
ll.print_all()