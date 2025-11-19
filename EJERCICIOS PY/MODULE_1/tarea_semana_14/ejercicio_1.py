"""1. Create an object structure that resembles a Stack.
    1. It must include the methods `push` (to add nodes) and `pop` (to remove nodes).
    2. It must include a method to `print` the entire structure.
    3. The use of composite data types such as `lists`, `dicts`, or `tuples`, or modules like `collections` is not allowed."""

class Node:
    data:str
    def __init__(self, data, next=None):
        self.data=data
        self.next=next

class LinkedList:
    head=Node
    def __init__(self, head=None):
        self.head=head

    def print_structure(self):
        current_node=self.head
        print("_______stack contents_______")
        while (current_node is not None):
            print(current_node.data)
            current_node=current_node.next
        print("________________________")

class Stack(LinkedList):

    def push(self, new_node):
        new_node.next=self.head
        self.head=new_node
    
    def pop(self):
        if self.head is None:
            return "the stack is empty"
        
        popped_node=self.head

        self.head=self.head.next
        print (f"removed item: {popped_node.data}")
        return popped_node.data
        


print("Stacking Cards")
card_a=Node("card 1(A♥)")
card_b=Node("card 2(A♦)")
card_c=Node("card 3(A♣)")
card_d=Node("card 4(A♠)")

stack=Stack()
stack.push(card_a)
stack.push(card_b)
stack.push(card_c)
stack.push(card_d)
stack.print_structure()

print("removing cards (POP)")
stack.pop()
stack.pop()
stack.print_structure()