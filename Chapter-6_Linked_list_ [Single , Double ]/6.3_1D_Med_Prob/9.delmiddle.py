"""
"Delete the Middle Node from the Linked List"
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

    temp = head
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("Null")

    return None


arr = [1, 2, 3, 4, 5]
head = LL(arr)
print_LL(head)

# Brute Force
"""
Iterate over and find the length of linked list.
Find the node before middle node and change its link to
middle node's next.

Time Complexity : O(n + n/2)
Space Complexity : O(1)
"""
import math


def delMiddle(head):
    if not head or not head.next:
        return None

    temp = head
    count = 0
    while temp:
        temp = temp.next
        count += 1

    midNode_prev = math.floor(count // 2)
    temp = head
    while temp:
        midNode_prev -= 1
        if midNode_prev == 0:
            temp.next = temp.next.next
            break
        temp = temp.next

    return head


delMiddle(head)
print_LL(head)

# Optimal Approach
"""
We use the Tortoise & Hare Algorithm with a slight change,
where we skip the first step for slow to end up at the node
just before the middle.

Time Complexity = O(N/2)
Space Complexity = O(1)
"""


def DelMiddle(head):
    if not head or not head.next:
        return None

    slow, fast = head, head
    fast = fast.next.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    slow.next = slow.next.next

    return head


DelMiddle(head)
print_LL(head)
