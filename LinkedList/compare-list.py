"""
 Merge two linked list
 head could be None as well for empty list
 Node is defined as
"""
class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

 #return back the head of the linked list in the below method.



def CompareLists(headA, headB):
    if headA is None and headB is None:
        return 1
    else:
        while headA is not None and headB is not None:
            if headA.data == headB.data:
                headA = headA.next
                headB = headB.next
                continue
            else:
                return 0
        else:
            if headA is None and headB is None:
                return 1
    return 0