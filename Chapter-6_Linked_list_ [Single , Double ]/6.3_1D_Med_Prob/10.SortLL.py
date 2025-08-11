"""
"Sort the given Linked List"

=> Given  a linked list we need to first sort it and then return the head.
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


arr = [2, 3, 1, 4, 5]
head = LL(arr)
print_LL(head=LL(arr))

# Naive Approach
# Time Complexity = O(n + nlogn + n)
# Space Complexity = O(n)
"""
We will be iterating over the list and storing each
element in an array.

Then either we can sort and convert our array to new LL
or we can again iterate and change the elements of previous
linked list.

At last return the head.
"""


def giveArr_LL(head):
    if not head or not head.next:
        return head

    temp = head
    arr = []
    while temp:
        arr.append(temp.data)
        temp = temp.next

    return arr


giveArr_LL(head)

# Sort and create new arr and linked list
arr = sorted(arr)
head = LL(arr)
print_LL(head)
head.data


# Changing in that LL only
def sort_LL(head):
    if not head or not head.next:
        return head

    temp = head
    arr = []
    while temp:
        arr.append(temp.data)
        temp = temp.next

    arr = sorted(arr)
    i = 0
    temp = head
    while temp:
        temp.data = arr[i]
        i += 1
        temp = temp.next

    return head


arr = [5, 3, 4, 5, 6, 78]
head = LL(arr)
sorted_LL = sort_LL(head)
print_LL(sorted_LL)

# Optimal Approach
# Time Complexity = O(logn x (n + n/2))
# Space Complexity = O(1)
"""
Now we need to optimize it so we need to do something 
in the LL itself.

Two good sorting techniques are "Merge Sort" & "Quick Sort"
we will be using Merge Sort as its feasible to apply here easily.

Hence we will be using Merge Sort for sorting , Tortoise & Hare algo
for finding Middle and will be Simply returing the Merged LL. 
"""


def findMiddle(head):
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def Merge(leftHead, rightHead):
    dummy = Node(-1)
    temp = dummy

    while leftHead and rightHead:
        if leftHead.data < rightHead.data:
            temp.next = leftHead
            temp = leftHead
            leftHead = leftHead.next

        else:
            temp.next = rightHead
            temp = rightHead
            rightHead = rightHead.next

    if leftHead:
        temp.next = leftHead
    else:
        temp.next = rightHead

    return dummy.next


def MergeSort(head):
    if not head or not head.next:
        return head

    middle = findMiddle(head)
    leftHead = head
    rightHead = middle.next

    middle.next = None
    leftHead = MergeSort(leftHead)
    rightHead = MergeSort(rightHead)

    return Merge(leftHead, rightHead)


arr = [5, 4, 3, 2, 1]
head = LL(arr)
print_LL(head)

print_LL(MergeSort(head))
