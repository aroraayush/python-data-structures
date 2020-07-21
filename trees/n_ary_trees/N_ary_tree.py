# Ref : https://github.com/joaohelis/n_ary_tree_with_python/blob/master/n_ary_tree.py

# Treenode => val, children
# n_ary_tree => size

class Treenode:
    def __init__(self, val, children = None):
        self.val = val
        self.children = children or []
    
    # The repr() function returns a printable 
    # representational string of the given object.
    # repr() is mainly used for debugging and development
    def __str__(self):
        return repr(self.val)

class NodeNotFoundException(Exception):
	def __init__(self, value):
		self.value = value
	
	def __str__(self):
		return repr(self.value)

class N_Ary_Tree:
    
    def __init__(self):
        self.root = None
        self.size = 0
    
    def __str__(self):
        return self.print_tree(self,root, "")

    def find_node(self,node, val):
        if node == None or node.val == val:
            return node
        
        # checking for node at every level
        for child in node.children:
            return_node = self.find_node(child, val)
            
            if return_node:
                return return_node
            
            return None
    
    def add_child(self, new_val, parent_val = None):
        node = Treenode(new_val)
        
        # Tree is empty
        if parent_val == None:
            self.root = node
            self.size = 1
        else:
            parent_node = self.find_node(self.root, parent_val)
            if not parent_node:
                raise NodeNotFoundException("No element was found with the informed parent val")
            
            parent_node.children.append(node)
            self.size += 1


n_ary_tree = N_Ary_Tree()

# Only 1 parameter, adding parent
n_ary_tree.add_child(10)

# 2 parameters, adding parent and child
n_ary_tree.add_child(20, 10)
n_ary_tree.add_child(30, 10)
n_ary_tree.add_child(50, 20)
n_ary_tree.add_child(40, 20)
n_ary_tree.add_child(70, 20)
n_ary_tree.add_child(78, 20)
n_ary_tree.add_child(11, 30)

print('n_ary_tree.size: ', n_ary_tree.size)  # 7