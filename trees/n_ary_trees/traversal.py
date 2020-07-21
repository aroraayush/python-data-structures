#  Directed Acyclic Graph

class Treenode:
    def __init__(self, data, children = None):
        self.data = data
        self.children = children or []
    
    def add_child(self, obj):
        self.children.append(obj)
    