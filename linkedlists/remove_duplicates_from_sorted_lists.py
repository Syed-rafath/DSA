from linkedlist import SinglyNode, LinkedList,list_to_linkedlist
import copy 

testcase = [1,1,2,3,3]

ll = list_to_linkedlist(testcase)
temp_ll = copy.deepcopy(ll)

head = ll.head
def deleteDuplicates(head):
    curr = head.next 

    #edge cases
    if not head or not head.next:
        return
    
    while curr:
        if curr.val == head.val:
            head.next = curr.next
        else:
            head = curr.next
        curr = curr.next

def deleteDuplicates2(head):
    curr = head
    while curr.next:
        if curr.val == curr.next.val:
            curr.next = curr.next.next
        else:
            curr = curr.next 
    

deleteDuplicates2(head)
ll.display()
temp_ll.display()