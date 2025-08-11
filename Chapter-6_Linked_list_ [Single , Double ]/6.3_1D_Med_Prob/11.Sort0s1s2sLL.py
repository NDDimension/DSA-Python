"""
"Sort a Linked List consisting of only 0s , 1s and 2s"

=> Given a LL of only 0s 1s and 2s we need to sort them and return
    return the LL.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, arr=None):
        self.head = None
        if arr:
            self.LL(arr)

    def LL(self, arr):
        self.head = Node(arr[0])
        tail = self.head

        for data in arr[1:]:
            tail.next = Node(data)
            tail = tail.next

    def print_LL(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("Null")


arr = [1, 0, 1, 0, 2, 0, 2]
l1 = LinkedList(arr)
l1.print_LL()

# Brute Force
# Time Complexity = O(2n)
# Space Complexity = O(1)
"""
We will be iterating and counting the number of 0s,1s and 2s
and then imputing them in the list.
"""


def count(head):
    temp = head
    c0, c1, c2 = 0, 0, 0

    while temp:
        if temp.data == 0:
            c0 += 1

        elif temp.data == 1:
            c1 += 1

        else:
            c2 += 1

        temp = temp.next

    temp = head
    while temp:
        if c0:
            temp.data = 0
            c0 -= 1

        elif c1:
            temp.data = 1
            c1 -= 1

        else:
            temp.data = 2
            c2 -= 1

        temp = temp.next

    return head


count(l1.head)
l1.print_LL()

# Optimal Approach
# Time Complexity : O(n)
# Space Complexity : O(1)
"""
We will be changing the links this time by seggregating 3
different lists l0 , l1 and l2.
"""


def sort_0s1s2s(head):
    if not head or not head.next:
        return head

    head0 = Node(-1)
    head1 = Node(-1)
    head2 = Node(-1)

    zero, one, two = head0, head1, head2
    temp = head

    while temp:
        if temp.data == 0:
            zero.next = temp
            zero = temp
        elif temp.data == 1:
            one.next = temp
            one = temp
        else:
            two.next = temp
            two = temp
        temp = temp.next

    zero.next = head1.next if head1.next else head2.next
    one.next = head2.next
    two.next = None

    return head0.next


arr = [1, 0, 1, 0, 2, 0, 2]
l1 = LinkedList(arr)

print("Before sorting:")
l1.print_LL()

l1.head = sort_0s1s2s(l1.head)

print("After sorting:")
l1.print_LL()
