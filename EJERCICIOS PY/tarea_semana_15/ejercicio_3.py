"""- Implement a working bubble_sort for @LinkedLists
- Modify your implementation of `bubble_sort` so that:
- It counts how many iterations (passes) the algorithm performs
- It counts how many swaps were made in total"""

class Node:
    data:int

    def __init__(self, data, next=None):
        self.data=data
        self.next=None


class LinkedList:
    head=Node
    def __init__(self, head):
        self.head=head

    def print_structure(self):
        current_node=self.head
        output=""
        while(current_node is not None):
            output+=str(current_node.data)
            current_node=current_node.next
            if current_node is not None:
                output+=" -> "
        print(output)

    def bubble_sort_steps(self):
        head=self.head
        if self.head is None:
            return head
        
        iterations_count = 0 
        swaps_count = 0

        while True:
            iterations_count+=1
            has_made_change=False
            prev=None
            current=self.head

            while current and current.next is not None:
                next_node=current.next       
                
                if current.data>next_node.data:
                    if prev is None:
                        self.head=next_node
                    else:
                        prev.next=next_node
                        
                    current.next=next_node.next
                    next_node.next=current
                    prev = next_node
                    swaps_count+=1
                    has_made_change=True
                
                else:
                    prev=current
                    current=current.next
            if not has_made_change:
                break
        return iterations_count, swaps_count 



N1=Node(5)
N2=Node(4)
N3=Node(2)
N4=Node(3)
N5=Node(1)

N1.next=N2
N2.next=N3
N3.next=N4
N4.next=N5

my_list=LinkedList(N1)
iterations_count, swaps_count=my_list.bubble_sort_steps()

print("ordered list:")
my_list.print_structure()
print(f"iterations: {iterations_count}")
print(f"swaps: {swaps_count}")

