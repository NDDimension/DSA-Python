"""
"Add 2 numbers in Linked List"

=> We will be given with two linked list l1 and l2 ; we need to reverse them ; consider it as numbers ;
    add l1 and l2 ; return the answer in reverse linked list.

=> Example :

l1 = 3 -> 5 -> X
l2 = 4 -> 5 -> 9 -> 9 -> X

reverse them
l1 => 5 -> 3 -> x
l2 => 9 -> 9 -> 5 -> 4 -> x

Add them
9954 + 53 = 10007

Revers it and form LL
Ans : 7 -> 0 -> 0 -> 0 -> 1 -> x
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


arr1 = [3, 5]
l1 = LinkedList(arr1)
l1.print_LL()

arr2 = [4, 5, 9, 9]
l2 = LinkedList(arr2)
l2.print_LL()


# Brute Force
# Time Complexity : O(max (n1 , n2))
# Space Complexity : O(max (n1 , n2))

"""
we will be taking 3 vars ; t1 = h1 , t2 = h2 and carry = 0 and moving them adding along the way
if any of the linked list exhaust and carry var has some values till present we add them with second 
linked list and add the answer as a new nod.
"""


def Add2LL(h1, h2):
    if not h1 and not h2:
        return None

    t1, t2 = h1, h2
    carry = 0
    dummyNode = Node(-1)
    curr = dummyNode

    while t1 or t2:
        ans = carry
        if t1:
            ans += t1.data

        if t2:
            ans += t2.data

        newNode = Node(ans % 10)
        carry = ans // 10
        curr.next = newNode
        curr = curr.next

        if t1:
            t1 = t1.next

        if t2:
            t2 = t2.next
    if carry:
        newNode = Node(carry)
        curr.next = newNode

    return dummyNode.next


result_head = Add2LL(l1.head, l2.head)
result_list = LinkedList()
result_list.head = result_head
print("Sum List:")
result_list.print_LL()
