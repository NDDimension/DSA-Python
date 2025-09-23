"""
Stack Implementation Using Singly Linked List in Python

Overview:
---------
A Stack is a linear data structure that follows the **LIFO (Last-In, First-Out)** principle.
This means the most recently added element is the first one to be removed — like a stack of plates.

This implementation uses a **singly linked list** to represent the stack dynamically.
Each element (node) points to the next one, and elements are added and removed from the head
of the list to ensure O(1) time complexity for push and pop operations.

Advantages:
-----------
- Dynamic memory allocation: No need to define a maximum size.
- Efficient push and pop operations (O(1)).
- Useful when the number of elements isn't known in advance.

Stack Operations:
-----------------
1. push(data): Adds a new element to the top of the stack.
2. pop(): Removes and returns the top element from the stack.
3. peek(): Returns the top element without removing it.
4. is_empty(): Checks whether the stack is empty.
5. display(): Prints the current elements in the stack from top to bottom.

Time Complexity:
----------------
- Push: O(1)
- Pop:  O(1)
- Peek: O(1)
- Display: O(n), where n is the number of elements in the stack.

Common Use Cases:
-----------------
- Function call stack
- Undo/Redo operations
- Expression evaluation (e.g., postfix, infix)
- Backtracking algorithms
"""


class Node:
    """
    A Node in the linked list used for the stack.

    Attributes:
        data: The value stored in the node.
        next: A pointer to the next node.
    """

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        """
        Checks if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return self.top is None

    def push(self, data):
        """
        Adds an item to the top of the stack.

        Args:
            data: The data to be pushed onto the stack.
        """
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print(f"Pushed: {data}")

    def pop(self):
        """
        Removes and returns the top item from the stack.

        Returns:
            The data from the popped node, or None if the stack is empty.
        """
        if self.is_empty():
            print("Stack is empty cannot Pop")
            return None

        popped_node = self.top
        self.top = self.top.next
        print(f"Popped : {popped_node.data}")
        return popped_node.data

    def peek(self):
        """
        Returns the top item without removing it.

        Returns:
            The data at the top of the stack, or None if the stack is empty.
        """
        if self.is_empty():
            print("Stack is empty")
            return None

        return self.top.data

    def display(self):
        """
        Displays the contents of the stack from top to bottom.
        """
        if self.is_empty():
            print("Stack is empty")
            return

        print("Stack contents (top -> bottom)")
        current = self.top
        while current:
            print(current.data)
            current = current.next


s = Stack()

s.push(10)
s.push(20)
s.push(30)

s.display()

print("Top element:", s.peek())

s.pop()
s.display()
