'''
Time Complexity : O(n)
Space Complexity : O(n) 
'''

# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = None  
        
class LinkedList: 
  
    def __init__(self): 
        self.head = None
  
    def push(self, new_data):
        temp = Node(data=new_data)
        if self.head:
            dummy = self.head
            while(dummy):
                if(not dummy.next):
                    dummy.next = temp
                    break
                dummy = dummy.next
        else:
            self.head = temp
        d = self.head

    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        len_ll = 0
        traverse_ct = 0
        dummy = self.head
        while(dummy):
            len_ll += 1
            dummy = dummy.next
        d = self.head
        while(traverse_ct<round(len_ll/2)):
            d = d.next
            traverse_ct += 1
        print(d.data)


# Driver code 
list1 = LinkedList() 
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle() 
