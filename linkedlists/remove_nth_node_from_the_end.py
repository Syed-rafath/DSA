from linkedlist import SinglyNode,list_to_linkedlist
from typing import Optional
tc1 = [[1,2,3,4,5], 2]
tc2 = [[1], 1]
tc3 = [[1,2], 1]
tc4 = [[1,2], 2]


def removeNthFromEnd(head: Optional[SinglyNode], n: int) -> Optional[SinglyNode]:
    #two pointers (l,r), have n space between them and keep moving until r is null
    dummy = SinglyNode(0,head)
    left = dummy
    right = head

    for _ in range(n):
        right = right.next 

    while right and left:
        right = right.next
        left = left.next

    left.next = left.next.next

    return dummy.next

for value in ([tc1,tc2,tc3,tc4]):

    print(value[0])
    print(value[1])
    try:
        removeNthFromEnd(head=list_to_linkedlist(value[0]),n=value[1]).display()
    except:
        print(f"error at")
        print(value)
