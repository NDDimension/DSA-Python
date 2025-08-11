"""
"Creating Linked List in python"
"""


# Mimicking Linked List Node Structure of C++
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f"Node({self.data})"


# Creating a new Node having value = 2 , next_add = None
y = Node(2)

# Printing the value at y and next_add at y
y, y.data, y.next


##############################


# Linked List in python
# Define a Node class to store data and a reference to the next node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Function to convert a list of integers into a linked list
def LinkedList(arr):
    if not arr:
        return None  # Return None for empty input list

    head = Node(arr[0])  # Create the head node with the first element
    mover = head  # Pointer to keep track of the last node
    for i in range(1, len(arr)):
        temp = Node(arr[i])  # Create a new node for each remaining element
        mover.next = temp  # Link the current node to the new node
        mover = temp  # Move the pointer to the new last node
    return head  # Return the head of the constructed linked list


# Length of Linked List
def LL_Length(head):
    count = 0
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
        count += 1
    return count


# Finding element in Linked List
def element_in_LL(head, val):
    temp = head
    while temp:
        if temp.data == val:
            return True
        temp = temp.next
    return False


arr = [1, 2, 3, 4, 5]
head = LinkedList(arr)


def print_LL(node):
    while node:
        print(node.data, end=" -> ")
        node = node.next
    print("None")


element_in_LL(head, 3)
element_in_LL(head, 30)
LL_Length(head)
print_LL(head)
