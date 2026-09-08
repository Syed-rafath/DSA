class SinglyNode:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)

    def display(self):
            elements = []
            curr = self
            while curr:
                elements.append(str(f"({curr})"))
                curr = curr.next
    
            print('->'.join(elements))

class LinkedList:
    def __init__(self):
        self.head=None

    #adding node to the end
    def append(self,val):
        new_node = SinglyNode(val)

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



def list_to_linkedlist(arr):
    ll = LinkedList()

    for n in arr:
        ll.append(n)

    return ll.head

     