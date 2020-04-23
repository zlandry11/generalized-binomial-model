from binarytree import Node, build

class Tree:
    
    def __init__(self, S, u, d):
        self.S = S
        self.u = u
        self.d = d
        
    def create_tree(self):
        tree = [self.S, self.d*self.S, self.u*self.S, self.d**2*self.S, self.d*self.u*self.S, self.d*self.u*self.S, self.u**2*self.S]
        return build(tree)
        
tree = Tree(110, 1.4, .7)
print(tree.create_tree())
# Node(self.S, left=Node(self.d*self.S), right=Node(self.u*self.S))
