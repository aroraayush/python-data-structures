# all nodes in the linked list are 0-indexed
# the head node represents the entire linked list

# Functions:

# get(index) : Get the value of the index-th node in the linked list. If the index is invalid, return -1.
# addAtHead(val) : Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
# addAtTail(val) : Append a node of value val to the last element of the linked list.
# addAtIndex(index, val) : Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
# deleteAtIndex(index) : Delete the index-th node in the linked list, if the index is valid.

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def traverse_list(self):
    if self.head is None:
        print("List has no element")
        return None
    else:
        temp = self.head
        while temp is not None:
            print(temp.val , " ")
            temp = temp.next

    def addAtHead(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head= new_node

	def addAtTail(self, val):
		new_node = Node(val)
		if self.head is None:
		    self.head = new_node
		    return None
		temp = self.head
		while temp.next is not None:
		    n= temp.next
		temp.next = new_node;

    def insert_after_val(self, x, val):

        temp = self.head
        print(temp.next)
        while temp is not None:
            if temp.val == x:
                break
            temp = temp.next
        if temp is None:
            print("val not itemp the list")
        else:
            new_node = Node(val)
            new_node.next = temp.next
            temp.next = new_node

    def addAtIndex (self, index, val):
        if index == 1:
            new_node = Node(val)
            new_node.next = self.head
            self.head = new_node
        i = 1
        temp = self.head
        while i < index-1 and temp is not None:
            temp = temp.next
            i = i+1
        if temp is None:
            print("Index out of bound")
        else: 
            new_node = Node(val)
            new_node.next = temp.next
            temp.next = new_node
    
    def insert_before_val(self, x, val):
        if self.head is None:
            print("List has no element")
            return

        if x == self.head.val:
            new_node = Node(val)
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head
        print(temp.next)
        while temp.next is not None:
            if temp.next.val == x:
                break
            temp = temp.next
        if temp.next is None:
            print("val not itemp the list")
        else:
            new_node = Node(val)
            new_node.next = temp.next
            temp.next = new_node

new_linked_list = LinkedList()
new_linked_list.addAtTail(5)
new_linked_list.addAtTail(10)
new_linked_list.addAtTail(15)
new_linked_list.traverse_list()
new_linked_list.addAtHead(20)

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
