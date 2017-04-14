"""
 Reverse a linked list
 head could be None as well for empty list
 Node is defined as
"""
class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

 #return back the head of the linked list in the below method.



def Reverse(head):
    # Empty list is always None
    if not head:
        return None

    # List of length 1 is already reversed
    if not head.next:
        return head

    next = head.next

    head.next = None

    rest = Reverse(next)

    next.next = head

    return rest
