"""
"Reverse a Doubly Linked List"
"""


# Doubly LinKed List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


def DLL(arr):
    if not arr:
        return None

    head = Node(arr[0])
    tail = head

    for i in range(1, len(arr)):
        new_node = Node(arr[i])
        new_node.prev = tail
        tail.next = new_node
        tail = new_node
    return head


def printDLL(head):
    if not head:
        return None

    temp = head
    while temp:
        print(temp.data, end=" <-> " if temp.data else "\n")
        temp = temp.next
    print("None")
    return None


arr = [1, 2, 3, 4, 5]
head = DLL(arr)
printDLL(head)


# For reversing extreme brute force is using stack to push and then pop.
# Time Complexity = O(n) + O(n)
# Space Complexity = O(n)


def reverseDLL(head):
    if not head:
        return None

    temp = head
    stack = []
    while temp:
        stack.append(temp.data)
        temp = temp.next

    temp = head
    while temp:
        temp.data = stack.pop()
        temp = temp.next
    return head


printDLL(head)
head = reverseDLL(head)
printDLL(head)


# Optimized approach would be reversing the links .
"""
last = current's back 
current's back = currents's next
current's next = last
current = current's back 

final -> new Head = last's back
"""
# Time Complexity = O(n)
# Space Complexity = O(1)


def reverseDLL_optimized(head):
    if not head:
        return None

    prev = None
    current = head
    while current is not None:
        prev = current.prev
        current.prev = current.next
        current.next = prev
        current = current.prev
    if prev is not None:
        head = prev.prev
    return head


printDLL(head)
head = reverseDLL_optimized(head)
printDLL(head)
