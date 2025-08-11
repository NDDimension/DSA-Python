"""
"Rotate the Linked List K times"

=> We will be given with K value and a Linked List and we need to perform
    rotation on the LL K times , return the new LL.
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

    def p_LL(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("x")


l1 = LinkedList([1, 2, 3, 4, 5])
l1.p_LL()

# Simple Approach:
# Time Complexity : O(2n)
# Space Complexity : O(1)
"""
We will finding the length , then will subract the
k from len and will reach the resultant node;
then its next node will be our new head , and its next 
will be pointed to null.
"""


def findNthNode(temp, k):
    count = 1
    while temp:
        if count == k:
            return temp
        count += 1
        temp = temp.next
    return None


def rotate_LL(head, k):
    if not head or not head.next or k == 0:
        return head

    tail = head
    length = 1
    while tail.next:
        tail = tail.next
        length += 1

    k = k % length
    if k == 0:
        return head

    tail.next = head
    new_tail = findNthNode(head, length - k)
    new_head = new_tail.next
    new_tail.next = None

    return new_head


l1.head = rotate_LL(l1.head, 2)
l1.p_LL()
