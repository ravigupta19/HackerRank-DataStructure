def Insert(head, data):
    new_node = Node(data)
    if head == None:
        head = new_node
    else:
        current = head
        while current.next != None:
            current = current.next
        current.next = new_node
    return head