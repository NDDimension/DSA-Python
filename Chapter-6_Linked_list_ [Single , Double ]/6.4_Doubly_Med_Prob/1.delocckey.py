"""
"Delete all occurences of a Key in Doubly Linked List"

=> Given a DLL and a key value we need to delete all the nodes having that key value.
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
            self.CreateDLL(arr)

    def CreateDLL(self, arr):
        self.head = Node(arr[0])
        tail = self.head

        for data in arr[1:]:
            newNode = Node(data)
            tail.next = newNode
            newNode.prev = tail
            tail = newNode

    def print_Forward(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("Null")

    def print_Backward(self):
        temp = self.head
        if not temp:
            print("Null")
            return

        while temp.next:
            temp = temp.next

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.prev
        print("Null")


dll = DoublyLinkedList([10, 8, 2, 10, 10, 50, 10])
dll.print_Forward()
dll.print_Backward()

# Simple Approach
# Time Complexity : O(N)
# Space Complexity : O(1)
"""
We will be traversing through the DLL and as we find the key
we delete it and update the links.
"""


def deleteKey(head, key):
    if not head or not head.next:
        return head

    temp = head
    while temp:
        if temp.data == key:
            if temp == head:
                head = head.next

            nextNode = temp.next
            prevNode = temp.prev

            if nextNode:
                nextNode.prev = prevNode

            if prevNode:
                prevNode.next = nextNode

            temp = nextNode

        else:
            temp = temp.next

    return head


dll.head = deleteKey(dll.head, 10)
dll.print_Backward()
dll.print_Forward()
