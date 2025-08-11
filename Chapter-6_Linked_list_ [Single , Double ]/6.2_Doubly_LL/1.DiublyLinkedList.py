"""
"Doubly Linked List"

=> Extension to single linked list having one more think to move backward also.
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


def toDLL(arr):
    if not arr:
        return None

    head = Node(arr[0])
    mover = head
    for i in range(1, len(arr)):
        temp = Node(arr[i])
        mover.next = temp
        temp.prev = mover
        mover = temp
    return head


def printDLL(head):
    print("Forward Traversal")
    tail = None
    while head is not None:
        print(head.val, end=" <-> " if head.next else "\n")
        tail = head
        head = head.next

    print("Backward Traversal")
    while tail is not None:
        print(tail.val, end=" <-> " if tail.prev else "\n")
        tail = tail.prev


arr = [10, 20, 30, 40, 50]
head = toDLL(arr)
printDLL(head)
