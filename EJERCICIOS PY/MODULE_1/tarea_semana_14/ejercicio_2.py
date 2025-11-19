"""2. Create an object structure that resembles a Double Ended Queue (Deque).
    1. It must include the methods `push_left` and `push_right` (to add nodes to the front and back) and `pop_left` and `pop_right` (to remove nodes from the front and back).
    2. It must include a method to `print` the entire structure.
    3. The use of composite data types such as `lists`, `dicts`, or `tuples`, or modules like `collections` is not allowed."""


class Node:
    data:str
    def __init__(self, data, next=None):
        self.data=data
        self.next=next


class Deque:
    def __init__(self):
        self.head=None
        self.tail=None
        


    def print_structure(self):
        current_node=self.head
        print("\n--- Deque Contents")
        while (current_node is not None):
            print(current_node.data)
            current_node=current_node.next
        print("___________________________________")

    def push_right(self, new_node):
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            return

        self.tail.next=new_node
        self.tail=new_node

    def push_left(self, new_node):
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            return
        
        new_node.next=self.head
        self.head=new_node

    def pop_left(self):
        if self.head is None:
            return "the Deque is empty"
        
        popped_node=self.head
        data_to_return=popped_node.data
        if self.head == self.tail:
            self.head=None
            self.tail=None
            return data_to_return
        
        self.head=self.head.next
        return data_to_return
    
    def pop_right(self):
        if self.head is None:
            return "the Deque is empty"
        
        if self.head==self.tail:
            data=self.head.data
            data_to_return=self.head.data
            self.head=self.tail=None
            return data_to_return
        
        current_node=self.head
        while (current_node.next is not self.tail):
            current_node=current_node.next
        popped_data=self.tail.data
        current_node.next=None
        self.tail=current_node
        return popped_data
    
deque=Deque()
print("_____NUMERICAL RULE_____")
print("ADDING POSITIVE NUMBERS")
deque.push_left(Node("0"))
deque.push_left(Node("1"))
deque.push_left(Node("2"))
deque.push_left(Node("3"))
deque.push_left(Node("4"))
deque.push_left(Node("5"))
deque.print_structure()
print("ADDING NEGATIVE NUMBERS")
deque.push_right(Node("-1"))
deque.push_right(Node("-2"))
deque.push_right(Node("-3"))
deque.push_right(Node("-4"))
deque.push_right(Node("-5"))
deque.print_structure()
print("REMOVING POSITIVE NUMBERS")
deque.pop_left()
deque.pop_left()
deque.print_structure()
print("REMOVING NEGATIVE NUMBERS")
deque.pop_right()
deque.pop_right()
deque.print_structure()