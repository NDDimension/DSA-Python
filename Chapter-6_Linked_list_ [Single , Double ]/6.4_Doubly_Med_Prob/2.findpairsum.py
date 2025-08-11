"""
"Find pairs that can provide the given sum in DLL"

=> Given a sorted DLL we need to return the pair of nodes which can give us the
    provided sum value.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, arr=None):
        self.head = None
        if arr:
            self.create_DLL(arr)

    def create_DLL(self, arr):
        self.head = Node(arr[0])
        tail = self.head

        for d in arr[1:]:
            newNode = Node(d)
            tail.next = newNode
            newNode.prev = tail
            tail = newNode

    def print_F(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("Null")

    def print_B(self):
        temp = self.head
        if not temp:
            print("null")
            return

        while temp.next:
            temp = temp.next

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.prev
        print("null")


dll = DoublyLinkedList([1, 2, 3, 4, 9])
dll.print_F()
dll.print_B()

# Simple Approach:
# Time Complexity : O(n^2)
# Space Complexity : O(1)
"""
we take two variable keep 1st var at point and 2nd var at one
step ahead , check if they provide the given sum or not

if its less we move forward as we get sum or value greater than sum
we stop as our answer can not lie further

we now move the 1st point ahead and 2nd point just ahead of it and
do the same thing.
"""


def sumPairs(head, summ):
    if not head or not head.next:
        return None

    temp1 = head
    ds = []
    while temp1:
        temp2 = temp1.next
        while temp2 and (temp1.data + temp2.data) <= summ:
            if (temp1.data + temp2.data) == summ:
                ds.append({temp1.data, temp2.data})

            temp2 = temp2.next
        temp1 = temp1.next

    return ds


dll.head = sumPairs(dll.head, 5)
dll.head


# Optimal Approach
# Time Complexity : O(n + n)
# Space Complexity : O(1)
"""
We will  be using concept of two pointers ; left = head , right = tail
check if they form a pair if not then check is the value > sum then move right pointer
else left and when they cross each other we stop.
"""


def findTail(head):
    if not head:
        return None

    temp = head
    while temp.next:
        temp = temp.next

    return temp


tail = findTail(dll.head)
print(tail.data)


def findPairs(head, summ):
    if not head or not head.next:
        return None

    left, right = head, findTail(head)
    ds = []
    while left.data < right.data:
        if left.data + right.data == summ:
            ds.append({left.data, right.data})
            left = left.next
            right = right.prev

        elif left.data + right.data < summ:
            left = left.next

        else:
            right = right.prev

    return ds


dll.head = findPairs(dll.head, 5)
dll.head
