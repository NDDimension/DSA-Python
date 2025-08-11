"""
"Reverse a Linked List"

=> Given a linked list we need to reverse it and return the new head.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def LL(arr):
    if not arr:
        return None

    head = Node(arr[0])
    tail = head

    for i in range(1, len(arr)):
        tail.next = Node(arr[i])
        tail = tail.next

    return head


def print_LL(head):
    if not head:
        return None

    while head:
        print(head.data, end=" ->  ")
        head = head.next
    print("Null")

    return None


""" Iterative Methods """

# Doing reversal in terms of data.
# Time Complexity = O(2n)
# Space Complexity = O(n)


def reverse_LL(head):
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


arr = [1, 2, 3, 4, 5]
head = LL(arr)
print_LL(head)
head = reverse_LL(head)
print_LL(head)


# Changing the links
# Time Complexity = O(n)
# Space Complexity = O(1)
"""
front = temp.next
temp.next = prev
prev = temp
temp = front
"""


def reverse_LL_links(head):
    if not head:
        return None

    temp = head
    prev = None
    while temp:
        front = temp.next
        temp.next = prev
        prev = temp
        temp = front

    return prev


head = LL(arr)
print_LL(head)
head = reverse_LL_links(head)
print_LL(head)


""" Recursive Methods """
# Time Complexity :  O(n)
# Space Complexity : O(n)


def recursive_reverse(head):
    if head is None or head.next is None:
        return head

    newNode = recursive_reverse(head.next)
    front = head.next
    front.next = head
    head.next = None

    return newNode


head = LL(arr)
print_LL(head)
head = recursive_reverse(head)
print_LL(head)
