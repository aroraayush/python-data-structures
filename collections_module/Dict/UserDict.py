from collections import UserList 

class MyList(UserList): 
      
    # Function to stop deleltion 
    # from List 
    def remove(self, s = None): 
        raise RuntimeError("Deletion not allowed") 
          
    # Function to stop pop from  
    # List 
    def pop(self, s = None): 
        raise RuntimeError("Deletion not allowed") 
      
# Driver's code 
L = MyList([1, 2, 3, 4]) 
  
print("Original List",L) 
  
# Inserting to List" 
L.append(5) 
print("After Insertion", L) 
  
# Deliting From List 
L.remove() 