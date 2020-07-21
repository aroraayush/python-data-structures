# ------------------ Extra Imports ------------------
# import os, sys, inspect
# currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# sys.path.insert(0,currentdir) 
# from bst_node import Node
# ------------------------------------------------------
# from trees.binary_trees.binary_search_tree.bst_node import Node

class Treenode:

    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = None
    
    def insert(self, val):
    
        if self.val:     # If no val empty tree, use base case
            if val < self.val:
                if self.left is None:
                    self.left = Treenode(val)
                else:
                    self.left.insert(val)
            else:
            # elif val > self.val:
                if self.right is None:
                    self.right = Treenode(val)
                else:
                    self.right.insert(val)
        else:
            self.val = val
    
    def print_tree(self):
        if self.left:
            self.left.print_tree()
    
        # base case - root node
        print(self.val)         # printed the left most mode
                                 # now backtracking to previous node
                                 # when left nodes of current subtree are finished
                                 # print(root)
                                 # same for right subtree now
        if self.right:
            self.right.print_tree()

    def print_tree(self):
        if self.left:
            self.left.print_tree()

    # left -> root -> right
    def in_order_traversal(self, root):
        traversed_arr = []
        # base case
        if(root):
            traversed_arr = self.in_order_traversal(root.left)
            traversed_arr.append(root.data)
            traversed_arr += self.in_order_traversal(root.right)
        return traversed_arr

root = Treenode(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
print(root.in_order_traversal(root))
