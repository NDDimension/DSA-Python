"""
"Remove the Nth node from the back"

=> Given a linked list and N we need to remove the Nth node from the end of the linked list.
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


arr = [1, 2, 3, 4, 5, 6]
head = LL(arr)
print_LL(head)

# Brute Force:
"""
Iterate over the whole and count the length
, then we subtract N from len and store it in result.

Now we again iterate over and find the result and change
its links to next of next.

Time Complexity : O(len) + O(len - N)
Space Complexity : O(1)
"""


def remove_Nth(head, n):
    if not head or not head.next:
        return head

    temp = head
    count = 0
    while temp:
        count += 1
        temp = temp.next

    if count == n:
        newHead = head.next
        return newHead

    res = count - n
    temp = head
    while temp:
        res -= 1

        if res == 0:
            break
        temp = temp.next

    delNode = temp.next
    temp.next = temp.next.next
    return head


remove_Nth(head, 3)
print_LL(head)

# Optimal approach
"""
We move fast pointer two steps ahead and then we move slow
and fast pointer simultaneously one step ahead.

As fast reaches last node we stop and our slow will be pointing to
the node one step before nth node.

Then we perform the same steps as brute.

Time Complexity = O(len)
Space Complexity = O(1)
"""


def remove_KthOpt(head, n):
    fast = head
    for i in range(n):
        fast = fast.next

    if fast == None:
        return head.next

    slow = head
    while fast.next:
        slow = slow.next
        fast = fast.next

    delNode = slow.next
    slow.next = slow.next.next
    delNode = None

    return head


remove_KthOpt(head, 3)
print_LL(head)
