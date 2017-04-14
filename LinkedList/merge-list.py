"""
 Merge two linked lists
 head could be None as well for empty list
 Node is defined as
"""
class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

 #return back the head of the linked list in the below method.



def MergeLists(headA, headB):
    head = None
    if headA is None:
        return headB
    elif headB is None:
        return headA
    else:
        while headA is not None and headB is not None:
            new_node = Node()
            if headA.data < headB.data:
                new_node.data = headA.data
                if head is None:
                    head = new_node
                    current = head
                else:
                    current.next = new_node
                    current = current.next
                headA = headA.next
            elif headB.data < headA.data:
                new_node.data = headB.data
                if head is None:
                    head = new_node
                    current = head
                else:
                    current.next = new_node
                    current = current.next
                headB = headB.next
        while headA is not None:
            new_node = Node()
            new_node.data = headA.data
            current.next = new_node
            current = current.next
            headA = headA.next
        while headB is not None:
            new_node = Node()
            new_node.data = headB.data
            current.next = new_node
            current = current.next
            headB = headB.next
    return head







