"""
"Deletion in Doubly Linked List"

=> We will be covering 4 types of problems here :
    - deleting head
    - deleting tail
    - deleting given kth position
    - deleting given value
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
        newNode = Node(arr[i])
        tail.next = newNode
        newNode.prev = tail
        tail = newNode

    return head


def print_DLL(head):
    if not head:
        return None

    tail = None
    while head is not None:
        print(head.val, end=" <-> " if head.next else "\n")
        tail = head
        head = head.next
    print()


arr = [10, 20, 30, 40]
head = DLL(arr)
print_DLL(head)


# Delete Head
def deleteHead(head):
    if head is None or head.next is None:
        return None

    prev = head
    head = head.next
    head.prev = None
    prev.next = None
    return head


head = deleteHead(head)
print_DLL(head)


# Delete Tail
def deleteTail(head):
    if head is None or head.next is None:
        return None

    tail = head
    while tail.next is not None:
        tail = tail.next

    tail.prev.next = None
    tail.prev = None
    return head


head = deleteTail(head)
print_DLL(head)


# Delete kth position
def deleteKth(head, k):
    if head is None:
        return None

    count = 1
    temp = head
    while temp is not None:
        if count == k:
            break
        count += 1
        temp = temp.next

    if temp is None:
        return head  # k is out of bounds

    prev = temp.prev
    front = temp.next

    if prev is None:  # Deleting head
        head = deleteHead(head)
        return head

    elif front is None:  # Deleting tail
        head = deleteTail(head)
        return head

    else:  # Deleting middle node
        prev.next = front
        front.prev = prev
        temp.next = None
        temp.prev = None

    return head


head = deleteKth(head, 3)
print_DLL(head)

head = deleteKth(head, 1)
print_DLL(head)

head = deleteKth(head, 4)
print_DLL(head)

# Delete Node


def deleteNode(head, val):
    if head is None:
        return None

    temp = head

    # Find the node with the given value
    while temp is not None:
        if temp.val == val:
            break
        temp = temp.next

    if temp is None:
        return head  # Value not found

    # Case 1: Delete head
    if temp.prev is None:
        head = deleteHead(head)
        return head

    # Case 2: Delete tail
    if temp.next is None:
        head = deleteTail(head)
        return head

    # Case 3: Delete middle node
    prev = temp.prev
    front = temp.next
    prev.next = front
    front.prev = prev
    temp.next = None
    temp.prev = None

    return head


head = deleteNode(head, 20)
print_DLL(head)
