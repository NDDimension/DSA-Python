"""
"Flatten a Linked List"

=> We are given with a different configuration LL having normal nodes
    with each normal node attached a child Linked List of that normal node in sorted
    manner.

    "Flatten.png" : example

    our task is to flatten this into a single Linked List of sorted order and each node
    having child link pointing to Null.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.child = None


class LinkedList:
    def __init__(self):
        self.head = None

    def build_main(self, val):
        if not val:
            return

        self.head = Node(val[0])
        current = self.head
        for val in val[1:]:
            current.next = Node(val)
            current = current.next

    def build_child(self, parent_node, child_val):
        if not parent_node or not child_val:
            return

        child_head = Node(child_val[0])
        current = child_head
        for val in child_val[1:]:
            current.child = Node(val)
            current = current.child

        parent_node.child = child_head

    def print_MLLL(self, node=None, depth=0):
        if node is None:
            node = self.head

        while node:
            print(node.data, end="")

            if node.child:
                print(" -> ", end="")
                self.print_MLLL(node.child, depth + 1)

            if node.next:
                print()
                print("| " * depth, end="")

            node = node.next


l1 = LinkedList()

l1.build_main([5, 10, 12, 7])
l1.print_MLLL()

l1.build_child(l1.head, [14])
l1.build_child(l1.head.next, [4])
l1.build_child(l1.head.next.next, [20, 13])
l1.build_child(l1.head.next.next.next, [17])

l1.print_MLLL()

# Brute Force:
# Time Complexity : O(2 * n * m ) + x log x
# Space Complexity : O(2 * n * m)
"""
Here we will be using a list to store all the values whether its parent
or child and then will sort them up and create a vertical linked list with no child
nodes or child link pointing to none.
"""


def Vertical_LL(arr):
    if len(arr) == 0:
        return None

    head = Node(arr[0])
    temp = head
    for val in arr[1:]:
        newNode = Node(val)
        temp.child = newNode
        temp = temp.child

    return head


def flattenBrute(head):
    t1 = head
    arr = []

    while t1:
        t2 = t1
        while t2:
            arr.append(t2.data)
            t2 = t2.child

        t1 = t1.next

    arr = sorted(arr)

    return Vertical_LL(arr)


def printVertical(head):
    while head:
        print(head.data, end=" -> ")
        head = head.child
    print("x")


printVertical(flattenBrute(l1.head))

# Optimal Approach
# Time Complexity : O(2 * n * m)
# Space Complexity : O(n)
"""
We will be taking advantage of child lists being sorted and 
not gonna sort the whole thing , also we will be merging the lists 
in place.
"""


def flatten_Optimal(head):
    if not head or not head.next:
        return head

    head.next = flatten_Optimal(head.next)
    return merge2lists(head, head.next)


def merge2lists(list1, list2):
    dummyNode = Node(-1)
    res = dummyNode

    while list1 and list2:
        if list1.data < list2.data:
            res.child = list1
            list1 = list1.child
        else:
            res.child = list2
            list2 = list2.child
        res = res.child
        res.next = None

    res.child = list1 if list1 else list2
    return dummyNode.child


l1 = LinkedList()
l1.build_main([5, 10, 12, 7])
l1.build_child(l1.head, [14])
l1.build_child(l1.head.next, [4])
l1.build_child(l1.head.next.next, [20, 13])
l1.build_child(l1.head.next.next.next, [17])


flat_head = flatten_Optimal(l1.head)

printVertical(flat_head)
