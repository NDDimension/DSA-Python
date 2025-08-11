"""
"Add 1 to Linked List"

=> Given a linked list consider it as a number ; add 1 to it ; return the new number
    in form of a linked list.

=> Example:
1 -> 5 -> 9 -> Null  => Number = 159 + 1    => NewNumber = 160      => 1 -> 6 -> 0 -> Null to be returned.
"""

# Brute Force
# Time Complexity : O(3n)
# Space Complexity : O(1)
"""
We first reverse the linked list as in order to add we need to start from end of LL 
but we can not traverse back in singly LL.

Then we take a carry variable = 1 and add it to head of reversed LL i.e.
suppose 9 is the head so 9 + 1 = 10 , carry = 1 and 9 replaced by 0,
take the carry forward do the same .

As soon as the carry becomed 0 , break the loop.

Reverse  back this LL you get the answer.

If at any moment the list ends up and you have still got value in carry keep it there and
reverse the LL then add the carry value as a node as the new head.
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


arr = [1, 5, 9]
l1 = LinkedList(arr)
l1.print_LL()


def reverse(head):
    if not head or not head.next:
        return head

    newNode = reverse(head.next)
    front = head.next
    front.next = head
    head.next = None

    return newNode


l1.head = reverse(l1.head)
l1.print_LL()


def Add1(head):
    if not head or not head.next:
        return None

    head = reverse(head)
    temp = head
    carry = 1

    while temp:
        temp.data += carry
        if temp.data < 10:
            carry = 0
            break

        else:
            temp.data = 0
            carry = 1

        temp = temp.next

    if carry == 1:
        newNode = Node(1)
        head = reverse(head)
        newNode.next = head
        return newNode

    head = reverse(head)
    return head


arr2 = [9, 9, 9, 9]
l1 = LinkedList(arr2)
l1.print_LL()

l1.head = Add1(l1.head)
l1.print_LL()


# Optimal Approach
# Time Complexity : O(n)
# Space Complexity : O(n)
"""
Using recursion we can backtrack and that will help us reach our goal.
"""


def helper(temp):
    if temp is None:
        return 1

    carry = helper(temp.next)
    temp.data += carry

    if temp.data < 10:
        return 0
    temp.data = 0
    return 1


def Add1_Opt(head):
    finalCarry = helper(head)
    if finalCarry == 1:
        newNode = Node(1)
        newNode.next = head
        return newNode
    return head


arr = [9, 9, 9, 9]
l1 = LinkedList(arr)
l1.head = Add1_Opt(l1.head)
l1.print_LL()

arr2 = [1, 5, 9]
l2 = LinkedList(arr2)
l2.head = Add1_Opt(l2.head)
l2.print_LL()
