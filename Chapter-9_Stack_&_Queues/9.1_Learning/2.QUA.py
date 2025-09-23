"""
Queue Data Structure Implementation Using Arrays (Circular Queue)

Overview:
---------
A Queue is a linear data structure that follows the **FIFO (First-In-First-Out)** principle.
This means the element inserted first is the one to be removed first — much like a queue
of people standing in line.

In this implementation, we use a **fixed-size array (Python list)** to build a **circular queue**,
which efficiently uses space by wrapping around the end of the list when needed.

Queue Operations:
-----------------
1. Enqueue: Add an element to the rear of the queue.
2. Dequeue: Remove and return the element at the front of the queue.
3. Peek: View the element at the front without removing it.
4. is_empty: Check whether the queue is empty.
5. is_full: Check whether the queue is full.
6. display: Print all elements in the queue from front to rear.

Circular Queue:
---------------
This implementation uses modulo arithmetic to wrap the `front` and `rear` pointers around
when they reach the end of the array. This allows the queue to reuse previously freed space.

Time Complexity:
----------------
- Enqueue: O(1)
- Dequeue: O(1)
- Peek:    O(1)
- Display: O(n), where n is the number of elements in the queue.

Common Use Cases:
-----------------
- Job scheduling
- Printer queue management
- Handling asynchronous data (like IO Buffers)
- BFS (Breadth-First Search) in graphs

This module is intended for educational purposes or basic queue usage where fixed capacity is sufficient.
"""


class Queue:
    def __init__(self, capacity):
        """
        Initializes the queue with a fixed capacity.

        Args:
            capacity (int): Maximum number of elements the queue can hold.
        """
        self.queue = [None] * capacity
        self.capacity = capacity
        self.front = 0
        self.rear = -1
        self.size = 0

    def is_empty(self):
        """
        Checks if the queue is empty.

        Returns:
            bool: True if queue is empty, False otherwise.
        """
        return self.size == 0

    def is_full(self):
        """
        Checks if the queue is full.

        Returns:
            bool: True if queue is full, False otherwise.
        """
        return self.size == self.capacity

    def enqueue(self, item):
        """
        Adds an item to the rear of the queue.

        Args:
            item: The item to be added to the queue.
        """
        if self.is_full():
            print("Queue is full cannot Enqueue")
            return

        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        self.size += 1
        print(f"Enqueued : {item}")

    def dequeue(self):
        """
        Removes and returns the item from the front of the queue.

        Returns:
            The dequeued item, or None if the queue is empty.
        """
        if self.is_empty():
            print("Queue is empty cannot Dequeue")
            return None

        item = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        print(f"Dequeued : {item}")
        return item

    def peek(self):
        """
        Returns the item at the front of the queue without removing it.

        Returns:
            The front item, or None if the queue is empty.
        """
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.queue[self.front]

    def display(self):
        """
        Displays the current elements in the queue from front to rear.
        """
        if self.is_empty():
            print("Queue is empty")
            return
        print("Queue contents")
        index = self.front
        for _ in range(self.size):
            print(self.queue[index], end=" ")
            index = (index + 1) % self.capacity
        print()


q = Queue(capacity=4)
q.enqueue(1)
q.enqueue(2)
q.peek()
q.display()
q.dequeue()
q.dequeue()
q.dequeue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.size

"""
Dynamic Queue Implementation Using collections.deque

Overview:
---------
This module implements a Queue using Python's built-in `collections.deque`, which provides
an efficient way to perform queue operations in constant time (O(1)).

Unlike array-based (fixed-size) queues, this implementation is **dynamic**, meaning the queue 
can grow or shrink as needed without predefined capacity. This is ideal for general-purpose
applications where the number of elements isn't fixed in advance.

Queue Operations:
-----------------
1. Enqueue: Add an element to the rear of the queue.
2. Dequeue: Remove and return the element at the front of the queue.
3. Peek: View the element at the front without removing it.
4. is_empty: Check whether the queue is empty.
5. size: Return the number of elements in the queue.
6. display: Print all elements from front to rear.

Time Complexity:
----------------
- Enqueue: O(1)
- Dequeue: O(1)
- Peek:    O(1)
- Display: O(n), where n is the number of elements

Advantages:
-----------
- No need to manage front/rear pointers or handle overflow.
- More readable and maintainable.
- Dynamically resizable, unlike fixed-size array-based implementations.

Common Use Cases:
-----------------
- Event-driven programming
- Message queues
- Breadth-First Search (BFS)
- Producer-consumer problems

Note:
-----
Although `deque` supports operations at both ends, this implementation only uses one end 
for enqueue and the other for dequeue, staying true to FIFO behavior.
"""

from collections import deque


class DynamicQueue:
    def __init__(self):
        """
        Initializes an empty dynamic queue.
        """
        self.queue = deque()

    def is_empty(self):
        """
        Checks if the queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return len(self.queue) == 0

    def enqueue(self, item):
        """
        Adds an item to the rear of the queue.

        Args:
            item: The item to be added.
        """
        self.queue.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        """
        Removes and returns the item from the front of the queue.

        Returns:
            The item removed from the front, or None if the queue is empty.
        """
        if self.is_empty():
            print("Queue is empty! Cannot dequeue.")
            return None
        item = self.queue.popleft()
        print(f"Dequeued: {item}")
        return item

    def peek(self):
        """
        Returns the front item without removing it.

        Returns:
            The front item, or None if the queue is empty.
        """
        if self.is_empty():
            print("Queue is empty!")
            return None
        return self.queue[0]

    def size(self):
        """
        Returns the number of elements in the queue.

        Returns:
            int: Current size of the queue.
        """
        return len(self.queue)

    def display(self):
        """
        Displays the contents of the queue from front to rear.
        """
        if self.is_empty():
            print("Queue is empty!")
        else:
            print("Queue contents:")
            for item in self.queue:
                print(item, end=" ")
            print()


q = DynamicQueue()

q.enqueue(100)
q.enqueue(200)
q.enqueue(300)

q.display()

print("Front item:", q.peek())

q.dequeue()
q.display()

print("Queue size:", q.size())
