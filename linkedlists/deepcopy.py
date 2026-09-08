import copy 
from typing import Optional
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(0)
        hp = {None:None}
        curr = head 
        
        while curr is not None:
            hp[curr]  = Node(curr.val)
            curr = curr.next 

        curr = head 
        cp = dummy
        #print(hp)

        while curr is not None:
            cp.next = hp[curr]
            cp = cp.next
            #print(hp[hp[curr].random])
            cp.random = hp[curr.random]
            curr = curr.next
        
        return dummy.next

            

        
            
class LinkedList:
    def __init__(self):
        self.head=None

    #adding node to the end
    def append(self,val):
        new_node = Node(val)

        if self.head == None:
            self.head = new_node
            return

        #traverse to the end to append
        curr = self.head
        while curr.next:
            curr = curr.next 

        curr.next = new_node
    
    def display(self):
        elements = []
        curr = self.head
        while curr:
            elements.append(str(f"({curr})"))
            curr = curr.next

        print('->'.join(elements))


            
            