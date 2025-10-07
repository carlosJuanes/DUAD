"""3. Create an object structure that resembles a Binary Tree.
    1. It must include a method to print the entire structure.
    2. The use of composite data types such as `lists`, `dicts`, or `tuples`, or modules like `collections` is not allowed."""

class Node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None

class BinaryTree:
    def __init__(self):
        self.root=None

    def insert(self, root, new_data):
        if root is None:
            return Node(new_data)
        
        if new_data< root.data:
            root.left= self.insert(root.left, new_data)
        else:
            root.right=self.insert(root.right, new_data)
        return root
    def print(self, node):
        if node is not None:
            self.print(node.left)
            print(node.data, end=" ")
            self.print(node.right)

tree_root = None 
datos = [50, 30, 70, 20, 40, 60, 80]
tree=BinaryTree()
print("--- CONSTRUYENDO EL ÁRBOL ---")

for dato in datos:
    tree_root = tree.insert(tree_root, dato)
    print(f"Insertando: {dato}")

print("\n--- IMPRESIÓN COMPLETA (IN-ORDER) ---")
tree.print(tree_root)
print("\n-------------------------------------")


