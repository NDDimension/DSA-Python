"""
"Remove Duplicates from a Doubly Linked List"

=> We are given a sorted dll and we need to return it after deleting all occurences
    of duplicates.

-> Example

l1 : 1 1 1 2 2 3 3 3 x
ans : 1 2 3 x
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


dll = DoublyLinkedList([1, 1, 1, 2, 2, 3, 3, 3])
dll.print_F()
dll.print_B()

# Simple Approach
# Time Complexity : O(N)
# Space Complexity : O(1)
"""
We will use two variables 1st temp 2nd nextNode
and compare them if they are same then nextNode will
move farther till it becomes different from temp
then we do the link changes to remove the in between
duplicates.
"""


def remDupli(head):
    if not head or not head.next:
        return None

    temp = head
    while temp and temp.next:
        nextNode = temp.next
        while nextNode and nextNode.data == temp.data:
            nextNode = nextNode.next

        temp.next = nextNode
        if nextNode:
            nextNode.prev = temp

        temp = temp.next

    return head


dll.head = remDupli(dll.head)
dll.print_F()
