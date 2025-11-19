"""6. Doubly Linked List
- Requirements:
- Each node must have a reference to the next and to the previous node
- Methods:
append(data): Adds to the end
prepend(data): Adds to the beginning
delete(data): Removes the first node with that value
print_forward() and print_backward(): Prints in both directions"""


class Node:
    data:str
    next:"Node"
    before:"Node"
    def __init__(self, data, before=None, next=None):
        self.data=data
        self.next=next
        self.before=before
        
class DoublyLinkedList:
    head=Node
    def __init__(self):
        self.head=None
        self.tail=None

    def append(self, data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            return
        else:   
            new_node.before=self.tail
            self.tail.next=new_node
            self.tail=new_node
    
    def prepend(self, data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            return
        else:
            new_node.next=self.head
            self.head.before=new_node
            self.head=new_node

    def delete(self, data):
        current_node=self.head
        previous_node=None

        if current_node is None:
            return False
        
        if current_node.data==data:
            self.head=current_node.next
            if self.head is not None:
                self.head.before=None
            else:
                self.tail=None
                return True
            
        while current_node is not None and current_node.data!=data:
            previous_node=current_node
            current_node=current_node.next
        if current_node is not None:
            previous_node.next=current_node.next
            if current_node.next is not None:
                current_node.next.before=previous_node
            else:
                self.tail=previous_node
            return True
        return False
    
    def print_forward(self):
        current_node=self.head
        output=""
        while (current_node is not None):
            output+=str(current_node.data)
            current_node=current_node.next
            if current_node is not None:
                output+= " -> "
        print(output)

    def print_backward(self):
        current_node=self.tail
        output=""
        while (current_node is not None):
            output+=str(current_node.data)
            current_node=current_node.before
            if current_node is not None:
                output+= " -> "
        print(output)

dll=DoublyLinkedList()
dll.append("A")
dll.append("B")
dll.append("C")
dll.print_forward()
dll.print_backward()
dll.delete("B")
dll.print_forward()
dll.print_backward()
