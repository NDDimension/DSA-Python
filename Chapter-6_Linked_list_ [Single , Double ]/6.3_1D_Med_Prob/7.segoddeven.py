"""
"Seggregate Odd and Even Indexes in Linked List"

=> Given a linked list we need to group even index nodes and odd index nodes.
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

# Brute Force : we rearrange the list's data in such a way.
# Time Complexity : O(n/2 + n/2 + n)
# Space Complexity : O(n)


def Seggregate_OE(head):
    if not head or not head.next:
        return head

    temp = head
    arr = []
    while temp and temp.next:
        arr.append(temp.data)

        # collecting odd index
        temp = temp.next.next

    # collecting last left element
    if temp:
        arr.append(temp.data)

    # Collecting Evens
    temp = head.next
    while temp and temp.next:
        arr.append(temp.data)

        temp = temp.next.next

    if temp:
        arr.append(temp.data)

    i = 0
    temp = head
    while temp:
        temp.data = arr[i]
        i += 1
        temp = temp.next

    return head


# Optimal Approach : we change the links
# Time Complexity : O(2 x n/2)
# Space Complexity : O(1)
def Seggregate_OE_Optimal(head):
    if not head or not head.next:
        return head

    odd = head
    even = head.next
    evenHead = even

    while even and even.next:
        odd.next = odd.next.next
        odd = odd.next

        even.next = even.next.next
        even = even.next

    odd.next = evenHead
    return head


arr = [1, 2, 3, 4, 5, 6]
head = LL(arr)
print_LL(head)
head = Seggregate_OE_Optimal(head)
print_LL(head)
