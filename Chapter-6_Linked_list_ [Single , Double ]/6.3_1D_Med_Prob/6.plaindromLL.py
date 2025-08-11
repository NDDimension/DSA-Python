"""
"Check whether Linked List if Palindrome or not"

=> Given  a linked list we need to find if its palindrome or not.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def LL(arr):
    if not arr:
        return None

    head = Node(arr[0])
    curr = head
    for i in range(1, len(arr)):
        curr.next = Node(arr[i])
        curr = curr.next
    return head


def print_LL(head):
    if not head:
        return None

    temp = head
    while temp:
        print(temp.data, end="  -> ")
        temp = temp.next
    print("Null")


arr = [1, 2, 3, 4, 5, 6]
head = LL(arr)
print_LL(head)


# Brute Force using Stack for comparison
# Time Complexity : O(2n)
# Space Complexity : O(n)


def Palindrome(head):
    if not head:
        return None

    stack = []
    temp = head
    while temp:
        stack.append(temp.data)
        temp = temp.next

    temp = head
    while temp:
        if temp.data != stack.pop():
            return False
        temp = temp.next
    return True


print(Palindrome(head))
arr1 = [1, 2, 1]
head = LL(arr1)


# Optimal Approach
# Time Complexity = O(2 x (n / 2))
# Space Complexity = O(1)
"""
We will be using Tortoise and Hare Algo for finding middle first but this time
m1 , from m2 we reverse the linked list and using 2 pointer approach we start 
comparing if its same we return True else False.

-> In case of even length fast stops at second last 
-> In odd it will stop at last
"""


def reverse(head):
    if not head or not head.next:
        return None

    newHead = reverse(head.next)
    front = head.next
    front.next = head
    head.next = None
    return newHead


def Palindrome_Optimal(head):
    if not head:
        return None

    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    newHead = reverse(slow.next)

    first, second = head, newHead
    while second:
        if first.data != second.data:
            reverse(newHead)
            return False
        first = first.next
        second = second.next
    reverse(newHead)
    return True


print(Palindrome_Optimal(head))
