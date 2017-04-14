"""
 Insert Node at a specific position in a linked list
 head input could be None as well for empty list
 Node is defined as
"""
class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

 #return back the head of the linked list in the below method.
"""


# This is a "method-only" submission.
# You only need to complete this method.
def InsertNth(head, data, position):
    new_node = Node(data)
    if head == None:
        head = new_node
    else:
        if position == 0:
            new_node.next = head
            head = new_node
        else:
            current = head
            current_position = 1
            while current_position != position:
                current = current.next
                current_position += 1
            next_node = None
            if current.next != None:
                next_node = current.next
            current.next = new_node
            new_node.next = next_node
    return head
