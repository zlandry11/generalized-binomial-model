from binarytree import Node

u = 1.5
d = .5

root = Node(110)
root.left = Node(d*root.value)
root.right = Node(u*root.value)

print('Stock Tree:', root)