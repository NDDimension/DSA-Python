"""
Stack Data Structure Implementation using Array (Fixed Size)

A Stack is a linear data structure that follows the Last In First Out (LIFO) principle.
This implementation uses a fixed-size list (array) to store elements, along with an integer
'`top`' to track the index of the topmost element in the stack.

Core Operations:
----------------
1. push(x):
   Adds element 'x' to the top of the stack.
   Time Complexity: O(1)

2. pop():
   Removes and returns the top element of the stack.
   Time Complexity: O(1)

3. peek():
   Returns the top element without removing it.
   Time Complexity: O(1)

4. size():
   Returns the number of elements currently in the stack.
   Time Complexity: O(1)

5. is_empty():
   Returns True if the stack is empty, False otherwise.
   Time Complexity: O(1)

Notes:
------
- This version uses a fixed capacity. Attempting to push beyond the capacity will result in an overflow.
- Trying to pop or peek from an empty stack will result in an underflow.

Use Case Examples:
------------------
- Function call stack in recursion
- Undo/redo functionality
- Expression evaluation (postfix/infix)
- Backtracking algorithms (e.g., DFS)

"""


class Stack:
    # Stack Structure
    def __init__(self, cap=1000):
        self.arr = [0] * (cap)
        self.top = -1
        self.cap = cap

    # Push Operation
    def push(self, x):
        if self.top >= self.cap - 1:
            print("Stack Overflow")
            return

        self.top += 1
        self.arr[self.top] = x
        print(f"Pushed {x}")

    # Pop Operation
    def pop(self):
        if self.top == -1:
            print("Stack Underflow")
            return None

        x = self.arr[self.top]
        self.top -= 1
        print(f"Popped {x}")

    # Peek Operation
    def peek(self):
        if self.top == -1:
            print("Stack is Empty")
            return None

        return self.arr[self.top]

    # Size
    def size(self):
        return self.top + 1

    # is_empty
    def is_empty(self):
        return self.top == -1

    def print_stack(self):
        """
        Prints the elements of the stack from top to bottom.
        """
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Stack (top to bottom):")
            for i in range(self.top, -1, -1):
                print(self.arr[i])


stack = Stack()
stack.push(1)
stack.push(2)
stack.size()
stack.print_stack()
stack.pop()
stack.peek()
print(stack)

###############################

import unittest


class Stack:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.arr = [0] * self.capacity
        self.top = -1

    def push(self, x):
        if self.top >= self.capacity - 1:
            raise OverflowError("Stack Overflow")
        self.top += 1
        self.arr[self.top] = x

    def pop(self):
        if self.top == -1:
            raise IndexError("Stack Underflow")
        val = self.arr[self.top]
        self.top -= 1
        return val

    def peek(self):
        if self.top == -1:
            raise IndexError("Stack is empty")
        return self.arr[self.top]

    def size(self):
        return self.top + 1

    def is_empty(self):
        return self.top == -1


class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack(capacity=3)

    def test_push_and_pop(self):
        self.stack.push(10)
        self.stack.push(20)
        self.stack.push(30)
        self.assertEqual(self.stack.pop(), 30)
        self.assertEqual(self.stack.pop(), 20)
        self.assertEqual(self.stack.pop(), 10)

    def test_peek(self):
        self.stack.push(5)
        self.assertEqual(self.stack.peek(), 5)
        self.stack.push(15)
        self.assertEqual(self.stack.peek(), 15)

    def test_size_and_is_empty(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.push(1)
        self.assertFalse(self.stack.is_empty())
        self.assertEqual(self.stack.size(), 1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(self.stack.size(), 3)
        self.stack.pop()
        self.assertEqual(self.stack.size(), 2)

    def test_underflow(self):
        with self.assertRaises(IndexError):
            self.stack.pop()

    def test_overflow(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        with self.assertRaises(OverflowError):
            self.stack.push(4)

    def test_peek_on_empty_stack(self):
        with self.assertRaises(IndexError):
            self.stack.peek()


if __name__ == "__main__":
    unittest.main()
