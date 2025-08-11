"""
"Find the Length of the Loop in Linked List"

=> We are given with a linked list and we need to find the length of the loop in the linked list if it exists else 0.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def Loop_LL():
    head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)

    # Create a loop from fifth to second
    head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth

    # This creates a loop
    fifth.next = second

    return head


def simple_LL():
    head = Node(1)
    sec = Node(2)
    third = Node(3)

    head.next = sec
    sec.next = third
    third.next = None

    return head


head1 = Loop_LL()
head2 = simple_LL()


# Naive Approach
# Time Complexity : O(n)
# Space Complexity : O(n)
def len_loop(head):
    if not head:
        return None

    temp = head
    timer = 0
    node_set = {}
    while temp:
        if temp in node_set:
            return timer - node_set[temp]
        node_set[temp] = timer
        timer += 1
        temp = temp.next
    return 0


print(len_loop(head1))
print(len_loop(head2))


# Optimal Approach
# Time Complexity : O(n)
# Space Complexity : O(1)
def findLength(slow, fast):
    count = 1
    fast = fast.next
    while slow != fast:
        count += 1
        fast = fast.next
    return count


# Tortoise and Hare Algo
def Tortoise_and_Hare(head):
    if not head:
        return None

    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return findLength(slow, fast)
    return 0
