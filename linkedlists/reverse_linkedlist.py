from linkedlist import SinglyNode, LinkedList,list_to_linkedlist
import copy 

testcase = [1,1,2,3,3]

ll = list_to_linkedlist(testcase)

temp_ll = copy.deepcopy(ll)

head = ll.head

ll.display()
temp_ll.display()