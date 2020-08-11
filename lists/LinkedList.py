# all nodes in the linked list are 0-indexed
# the head node represents the entire linked list

# Functions:

# get(index) : Get the value of the index-th node in the linked list. If the index is invalid, return -1.
# addAtHead(val) : Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
# addAtTail(val) : Append a node of value val to the last element of the linked list.
# addAtIndex(index, val) : Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
# deleteAtIndex(index) : Delete the index-th node in the linked list, if the index is valid.

from . import Node

class MyLinkedList:

    def __init__(self, val=None):
        """
        Initialize your data structure here.
        """
        self.next = None
        self.val = val
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        node = MyLinkedList()
        node.val = val
        if self == None: # empty linked list
            self = node
        else:
            old_root = self
            node.next = old_root
            self = node
        return None
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        node = MyLinkedList()
        node.val = val
        node.next = None
        while self is not None:
            tail = MyLinkedList()
            tail.val = self.val
            tail.next = self.next
            self = tail.next

        tail.next = node
        return None
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index == 0:
            self.addAtHead(val)
            return None
        
        idx = 0
        new_node = MyLinkedList()
        new_node.val = val
        
        while self is not None:
            if idx == index - 1:
                new_node.next = self.next
                self.next = new_node
                return None
            else:
                node = MyLinkedList()
                node.val = self.val
                node.next = self.next
                self = node.next
                idx += 1
        return None
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index == 0:
            self = self.next
            return None
        
        idx = 0
        while self is not None:
            if idx == index - 1:
                self.next = self.next.next
                return None
            else:
                node = MyLinkedList()
                node.val = self.val
                node.next
                self = node.next
                idx += 1
        
        return None


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
