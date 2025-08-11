"""
"Finding the starting of Loop in Linked List"

=> Given a Linked List find its loop's starting node.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def Loop_LL():
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


head = Loop_LL()

# Naive Approach
# Time Complexity : O(2N)
# Space Complexity : O(n)


def Loop_Start(head):
    if not head:
        return None

    temp = head
    nodeset = set()

    while temp:
        if temp in nodeset:
            return temp.data
        nodeset.add(temp)
        temp = temp.next

    return None


print(Loop_Start(head))


def Tortoise_Hare(head):
    if not head:
        return None

    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next

            return slow.data

    return None


print(Tortoise_Hare(head))
