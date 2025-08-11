"""
"Reverse the group of K nodes"

=> We will be given with K value (group size) and linked list, we need to reverse
    the group of size K exactly others leave as it is.

=> Example :

Linked List -> 1 -> 2 -> 3 -> 4 -> 5 -> x
K = 3

Ans : 3 -> 2 -> 1 -> 4 -> 5 -> x
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, arr=None):
        self.head = None
        if arr:
            self.create_LL(arr)

    def create_LL(self, arr):
        self.head = Node(arr[0])
        tail = self.head

        for data in arr[1:]:
            tail.next = Node(data)
            tail = tail.next

    def LL(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("x")


l1 = LinkedList([x for x in range(1, 11)])
l1.LL()

# Simple Approach:
# Time Complexity  : O(2n)
# Space Complexity : O(1)
"""
We first find the kth node and separate that much portion
from LL and reverse it , and proceed in the same and 
also connecting the reversed LL on the go.
"""


def findKthnode(temp, k):
    k -= 1
    while temp and k > 0:
        k -= 1
        temp = temp.next

    return temp


def reverse(head):
    if not head or not head.next:
        return head

    newNode = reverse(head.next)
    front = head.next
    front.next = head
    head.next = None

    return newNode


def reverseK(head, k):
    temp = head
    prevNode = None

    while temp:
        kthnode = findKthnode(temp, k)
        if kthnode is None:
            if prevNode:
                prevNode.next = temp
            break

        nextNode = kthnode.next
        kthnode.next = None
        reverse(temp)

        if temp is head:
            head = kthnode

        else:
            prevNode.next = kthnode

        prevNode = temp
        temp = nextNode

    return head


l1.head = reverseK(l1.head, 3)
l1.LL()
