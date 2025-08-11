"""
"Inserting in Linked List"

=> 4 Types : At Head , Position , Value , Tail
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def conv_to_LL(arr):
    if not arr:
        return None

    head = Node(arr[0])
    mover = head
    for i in range(1, len(arr)):
        temp = Node(arr[i])
        mover.next = temp
        mover = temp
    return head


def printLL(head):
    while head is not None:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


# Insert at Head
def insertHead(head, val):
    temp = Node(val)
    temp.next = head
    return temp


arr = [1, 2, 3, 4, 5]
head = conv_to_LL(arr)
printLL(head)
head = insertHead(head, 0)
printLL(head)


# Insert at Tail
def insertTail(head, val):
    if head is None:
        return Node(val)

    temp = head
    while temp.next != None:
        temp = temp.next
    temp.next = Node(val)
    return head


arr = [1, 2, 3, 4, 5]
head = conv_to_LL(arr)
printLL(head)
head = insertTail(head, 6)
printLL(head)

# Insert a Kth position


def insertatK(head, val, k):
    if head == None:
        if k == 1:
            return Node(val)
        else:
            return None

    if k == 1:
        temp = Node(val)
        temp.next = head
        return temp

    count = 0
    temp = head
    while temp != None:
        count += 1
        if count == k - 1:
            new = Node(val)
            new.next = temp.next
            temp.next = new
            break

        temp = temp.next

    return head


arr = [1, 2, 3, 4, 5]
head = conv_to_LL(arr)
printLL(head)
head = insertatK(head, 6, 3)
printLL(head)

head = insertatK(head, 0, 1)
printLL(head)

head = insertatK(head, 7, 7)
printLL(head)


# Insert before a value
def insertBeforeValue(head, val, ele):
    if head == None:
        return None

    if head.val == ele:
        temp = Node(val)
        temp.next = head
        return temp

    temp = head
    while temp.next != None:
        if temp.next.val == ele:
            new = Node(val)
            new.next = temp.next
            temp.next = new
            break

        temp = temp.next

    return head


arr = [1, 2, 3, 4, 5]
head = conv_to_LL(arr)
printLL(head)
head = insertBeforeValue(head, 6, 3)
printLL(head)

arr = [1, 2, 3, 4, 5]
head = conv_to_LL(arr)
printLL(head)
head = insertBeforeValue(head, 0, 1)
printLL(head)

arr = [1, 2, 3, 4, 5]
head = conv_to_LL(arr)
printLL(head)
head = insertBeforeValue(head, 7, 7)
printLL(head)
