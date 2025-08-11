"""
"Deletion in Linked List"

=> 4 Types : Delete Head , Position , Value , Last
"""
# Delete Head


# Structure
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List Creator
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


# Printer LL
def printLL(head):
    while head is not None:
        print(head.data, end=" -> ")
        head = head.next
    print("None")


# Delete Head
def removeHead(head):
    if head is None:
        return head

    temp = head
    head = head.next

    return head


arr = [1, 2, 3, 4, 5]
head = conv_to_LL(arr)  # Creating Linked List
print("Current Head -> ", head.data)  # Check for current head
head = removeHead(head)  # Removing previous head
print("New Head -> ", head.data)  # Checking Latest Head

head = None
head = removeHead(head)
print("New Head -> ", head)  # Checking Latest Head


# Deleting Tail


def removeTail(head):
    if head is None or head.next is None:
        return head

    temp = head
    while temp.next.next != None:
        temp = temp.next
    temp.next = None
    return head


arr = [1, 2, 3, 4, 5]
head = conv_to_LL(arr)
printLL(head)
head = removeTail(head)
printLL(head)

# Delete the Kth positional element


def removeK(head, k):
    if head is None:
        return head

    if k == 1:
        head = head.next
        return head

    temp = head
    count = 0
    prev = None
    while temp != None:
        count += 1
        if count == k:
            prev.next = prev.next.next
            break

        prev = temp
        temp = temp.next
    return head


arr = [1, 2, 3, 4, 5]
head = conv_to_LL(arr)
printLL(head)
head = removeK(head, 3)
printLL(head)

arr = [1, 2, 3, 4, 5]
head = conv_to_LL(arr)
printLL(head)
head = removeK(head, 1)
printLL(head)

arr = [1, 2, 3, 4, 5]
head = conv_to_LL(arr)
printLL(head)
head = removeK(head, 5)
printLL(head)


# Delete element


def removeElement(head, val):
    if head is None:
        return head

    if head.data == val:
        head = head.next
        return head

    temp = head
    prev = None
    while temp != None:
        if temp.data == val:
            prev.next = prev.next.next
            break
        prev = temp
        temp = temp.next
    return head


arr = [1, 2, 3, 4, 5]
head = conv_to_LL(arr)
printLL(head)
head = removeElement(head, 3)
printLL(head)

arr = [1, 2, 3, 4, 5]
head = conv_to_LL(arr)
printLL(head)
head = removeElement(head, 1)
printLL(head)

arr = [1, 2, 3, 4, 5]
head = conv_to_LL(arr)
printLL(head)
head = removeElement(head, 5)
printLL(head)
