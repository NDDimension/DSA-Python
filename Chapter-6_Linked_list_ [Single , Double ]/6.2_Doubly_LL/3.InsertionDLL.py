"""
"Insertion in Doubly Linked List

=> Here also we will be having 4 types of Before any node:
    - insert head
    - insert tail
    - insert at kth pos
    - insert node

=> Same way we have After any node also.
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


def DLL(arr):
    if not arr:
        return None

    head = Node(arr[0])
    tail = head
    for i in range(1, len(arr)):
        temp = Node(arr[i])
        tail.next = temp
        temp.prev = tail
        tail = tail.next
    return head


def print_DLL(head):
    if not head:
        return None

    temp = head
    while temp:
        print(temp.val, end=" <-> " if temp.next else "\n")
        temp = temp.next
    print()


# Insert new head
def insertHeadbefore(head, val):
    if not head:
        return Node(val)

    temp = Node(val)
    temp.next = head
    head.prev = temp
    return temp


arr = [1, 2, 3, 4, 5]
head = DLL(arr)
print_DLL(head)

head = insertHeadbefore(head, 0)
print_DLL(head)


# i Insert after Head
def insertafterHead(head, val):
    if not head:
        return Node(val)

    temp = Node(val)
    temp.next = head.next
    head.next = temp
    temp.prev = head
    return head


head = insertafterHead(head, 6)
print_DLL(head)


# Insert after Tail
def insertAfterTail(head, val):
    if not head:
        return Node(val)

    temp = Node(val)
    tail = head
    while tail.next:
        tail = tail.next
    tail.next = temp
    temp.prev = tail
    return head


head = insertAfterTail(head, 7)
print_DLL(head)


# Insert before tail
def insertBeforeTail(head, val):
    if not head:
        return Node(val)

    tail = head
    while tail.next is not None:
        tail = tail.next

    prev = tail.prev
    node = Node(val)
    node.prev = prev
    node.next = tail

    prev.next = node
    tail.prev = node
    return head


head = insertBeforeTail(head, 8)
print_DLL(head)


# Insert before K
def insertBeforeK(head, k, val):
    if not head:
        return Node(val)

    t = head
    count = 1
    while t != None:
        if count == k:
            break
        count += 1
        t = t.next

    if t == None:
        return head

    prev = t.prev

    if prev is None:
        head = insertHeadbefore(head, val)
        return head

    node = Node(val)
    prev.next = node
    node.prev = prev
    node.next = t
    t.prev = node

    return head


head = insertBeforeK(head, 3, 9)
print_DLL(head)

head = insertBeforeK(head, 1, 10)
print_DLL(head)

head = insertBeforeK(head, 7, 11)
print_DLL(head)


# Insert before val
def insertBeforeVal(head, val, newVal):
    if not head:
        return Node(val)

    t = head
    while t != None:
        if t.val == val:
            break
        t = t.next

    if t == None:
        return head

    prev = t.prev

    if prev is None:
        head = insertHeadbefore(head, newVal)
        return head

    node = Node(newVal)
    prev.next = node
    node.prev = prev
    node.next = t
    t.prev = node

    return head


head = insertBeforeVal(head, 10, 12)
print_DLL(head)

head = insertBeforeVal(head, 1, 13)
print_DLL(head)

head = insertBeforeVal(head, 11, 14)
print_DLL(head)
