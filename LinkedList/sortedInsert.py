class Node(object):
    def __init__(self, data=None, next_node=None, prev_node=None):
        self.data = data
        self.next = next_node
        self.prev = prev_node

def SortedInsert(data, head = None):
    new_node = Node(data)
    if head is None: #creating a new list
        head = new_node
    elif data <= head.data: #inserting a node Start
        new_node.next = head
        head.prev = new_node
        head  = new_node
    else:
        current = head
        while current is not None:
            if data <= current.data:
                break
            previous = current
            current = current.next
        if current is not None:
            previous.next = new_node
            new_node.prev = previous
            new_node.next = current
            current.prev = new_node
        else:
            previous.next = new_node
            new_node.prev = previous
    return head

head = SortedInsert(2)
head = SortedInsert(1,head)
head = SortedInsert(4, head)
head = SortedInsert(3,head)
while head is not None:
    print(head.data)
    head = head.next
