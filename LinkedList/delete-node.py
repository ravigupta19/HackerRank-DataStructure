"""
 Delete Node at a given position in a linked list
 Node is defined as
"""
class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

 #return back the head of the linked list in the below method.



def Delete(head, position):
    current = head
    if position == 0:
        next_node = current.next
        current.next = None
        head = next_node
    else:
        previous = None
        current_position = 0
        while current_position != position:
            previous = current
            current = current.next
            current_position += 1
        next_node = None
        if current.next != None:
            next_node = current.next
        current.next = None
        previous.next = next_node
    return head