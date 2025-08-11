"""
"Find the Intersection Y of Linked List"

=> We will be given with two linked list having a common point between them
    we need to return that only.

=> If they collide we will be returning the first intersecting node
    else Null.
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
    temp = head
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("Null")


# Step 1: Create common part [4, 5]
common = LL([4, 5])

# Step 2: Create List A [1, 2, 3] and attach common
listA = LL([1, 2, 3])
tempA = listA
while tempA.next:
    tempA = tempA.next
tempA.next = common  # Attach common part

# Step 3: Create List B [6, 7] and attach common
listB = LL([6, 7])
tempB = listB
while tempB.next:
    tempB = tempB.next
tempB.next = common  # Attach common part

# Print the lists
print("List A:")
print_LL(listA)

print("List B:")
print_LL(listB)

# Brute Force
# Time Complexity: O(n x m)
# Space Complexity : O(1)
"""
We will be iterating over the two and along the way comparing also as soon as we get 
common element we straight away return it.
"""


def intersectionPresent(head1, head2):
    while head2:
        temp = head1
        while temp:
            if temp == head2:
                return head2
            temp = temp.next
        head2 = head2.next

    return None


intersection = intersectionPresent(tempA, tempB)
intersection.data

# Better Approach
# Time Complexity : O(n1 + n2)
# Space Complexity : O(n1)
"""
Hasing to memorize the count of elements and checking if it exceeds that 
means we have something in common.
"""


def intersectionBetter(h1, h2):
    visited = set()

    while h1:
        visited.add(h1)
        h1 = h1.next

    while h2:
        if h2 in visited:
            return h2
        h2 = h2.next

    return None


intersection = intersectionBetter(tempA, tempB)
intersection.data

# More Better Approach
# Time Complexity : O(n1 + 2n2)
# Space Complexity : O(1)
"""
We straight away compare the elements during traversal if same found then return.
But for that we need to be that the same position for comparison hence we need to first compute
the lengths and find difference .

Start the longer linked list from that difference point for comparison.
"""


def collisionPoint(smaller, greater, distance):
    while distance:
        distance -= 1
        greater = greater.next

    while smaller != greater:
        smaller = smaller.next
        greater = greater.next

    return smaller


def Intersection(h1, h2):
    t1 = h1
    t2 = h2
    n1, n2 = 0, 0

    while t1:
        n1 += 1
        t1 = t1.next

    while t2:
        n2 += 1
        t2 = t2.next

    if n1 < n2:
        return collisionPoint(h1, h2, n2 - n1)

    else:
        return collisionPoint(h2, h1, n1 - n2)


intersection = Intersection(tempA, tempB)
intersection.data

# Optimal Approach
# Time Complexity : O(n1 + n2)
# Space Complexity : O(1)
"""
We will be taking 2 variables for storing heads and then we move both one step at a time
as soon as one of the var reached last node switch it to another head and again do the same
with this both the var will reach at the same point after some time and it will be our common point.
"""


def intersection_Optimal(h1, h2):
    if not h1 and not h2:
        return None

    t1, t2 = h1, h2
    while t1 != t2:
        t1 = t1.next
        t2 = t2.next

        if t1 is t2:
            return t1

        if t1 is None:
            t1 = h2

        if t2 is None:
            t2 = h1

    return t1


intersection = intersection_Optimal(tempA, tempB)
intersection.data
