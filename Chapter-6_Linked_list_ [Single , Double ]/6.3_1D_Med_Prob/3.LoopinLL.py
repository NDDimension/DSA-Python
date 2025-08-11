"""
"Loop in a Linked List"

=> Given a linked list we need to find if there exists a loop in it or not.
=> Loop : if a node has both starting and ending in same.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def sample_LL():
    head = Node(1)
    sec = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)

    head.next = sec
    sec.next = third
    third.next = fourth
    fourth.next = fifth
    fifth.next = third

    return head


# Dont run as it goes into loop.
# def print_LL(head):
#     if not head:
#         return None

#     temp = head
#     while temp:
#         print(temp.data, end=" ->  ")
#         temp = temp.next
#     print("Null")

#     return None

head = sample_LL()
# print_LL(head)


# Naive approach
# Time Complexity : O(n)
# Space Complexity : O(n)
def detectLoop(head):
    if not head:
        return False

    temp = head
    visited = set()
    while temp:
        if temp in visited:
            return True
        visited.add(temp)
        temp = temp.next
    return False


print(detectLoop(head))

# Optimal Approach using Tortoise and Hare algo
# Time Complexity : O(n)
# Space Complexity : O(1)


def loop_Tortoise_Hare(head):
    if not head:
        return False

    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


print(loop_Tortoise_Hare(head))
