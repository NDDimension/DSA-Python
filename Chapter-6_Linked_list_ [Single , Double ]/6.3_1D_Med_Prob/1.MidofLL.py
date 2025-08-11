"""
"Middle of A Linked List"

=> Given a LL find the median of it.

=> Odd length then middle is easy to return
    but for Even length we will be having two m1 and m2 and we are going ot return
    m2.

=> We need to find the N len of LL then simply [(N/2) + 1]th node is middle.
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
    while temp.next is not None:
        print(temp.data, end=" -> ")
        temp = temp.next
    print(None)

    return None


arr = [1, 2, 3, 4, 5]
head = LL(arr)
print_LL(head)


# Middle of LL using Naive Solution of traversal
# Time Complexity = O(n + n/2)
# Space Complexity = O(1)


def middle_of_LL(head):
    if not head:
        return None

    temp = head
    count = 1

    while temp.next is not None:
        temp = temp.next
        count += 1

    midNode = count // 2 + 1
    temp = head
    while temp.next is not None:
        midNode -= 1
        if midNode == 0:
            break
        temp = temp.next

    return temp.data


arr1 = [1, 2, 3, 7, 5, 6]
arr2 = [8, 1, 2, 10, 15]
head1 = LL(arr2)
print_LL(head1)
print(middle_of_LL(head1))


# Optimal Solution using algorithm called "Tortoise & Hare"
# Time Complexity = O(n / 2)
# Space Complexity = O(1)
"""
Two pointers will be there fast and slow where 
slow moves 1 step and fast 2 .

Both are moving Simultaneously and as soon as fast reaches end slow will
be pointing to middle.

Odd length -> fast on last element
Even length -> fast on None

=> To return the value of middle = slow.data
=> To return the list from the middle node till end = slow
"""


def middle_of_LL_opt(head):
    if not head:
        return None

    slow, fast = head, head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow.data


arr1 = [1, 2, 3, 7, 5, 9]
head1 = LL(arr1)
print_LL(head1)
print(middle_of_LL_opt(head1))

arr2 = [8, 1, 2, 10, 15]
head2 = LL(arr2)
print_LL(head2)
print(middle_of_LL_opt(head2))
