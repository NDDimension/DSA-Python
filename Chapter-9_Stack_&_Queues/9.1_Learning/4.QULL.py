"""
Queue Implementation Using Singly Linked List in Python

Overview:
---------
A Queue is a linear data structure that follows the **FIFO (First-In, First-Out)** principle.
The first element added to the queue is the first one to be removed — like people standing in line.

This implementation uses a **singly linked list**, where:
- Elements are enqueued (added) at the **rear**.
- Elements are dequeued (removed) from the **front**.

This dynamic structure allows the queue to grow as needed without a fixed size.

Queue Operations:
-----------------
1. enqueue(data): Adds an element to the rear of the queue.
2. dequeue(): Removes and returns the element at the front.
3. peek(): Returns the front element without removing it.
4. is_empty(): Checks whether the queue is empty.
5. display(): Prints all elements from front to rear.

Time Complexity:
----------------
- Enqueue: O(1)
- Dequeue: O(1)
- Peek:    O(1)
- Display: O(n), where n is the number of elements in the queue.

Use Cases:
----------
- Task scheduling
- Asynchronous data handling
- Print/job queues
- BFS (Breadth-First Search) in graphs
"""


class Node:
    """
    A Node in the linked list used for the queue.

    Attributes:
        data: The value stored in the node.
        next: A pointer to the next node.
    """

    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        """
        Checks if the queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return self.front is None

    def enqueue(self, data):
        """
        Adds an item to the rear of the queue.

        Args:
            data: The data to be added to the queue.
        """
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node

        else:
            self.rear.next = new_node
            self.rear = new_node
        print(f"Enqueued : {data}")

    def dequeue(self):
        """
        Removes and returns the item from the front of the queue.

        Returns:
            The data from the dequeued node, or None if the queue is empty.
        """
        if self.is_empty():
            print("Queue is empty cannot Dequeue")
            return None

        removed_data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        print(f"Dequeued : {removed_data}")
        return removed_data

    def peek(self):
        """
        Returns the item at the front without removing it.

        Returns:
            The front item, or None if the queue is empty.
        """
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.front.data

    def display(self):
        """
        Displays the contents of the queue from front to rear.
        """
        if self.is_empty():
            print("Queue is empty")
            return
        print("Queue contents (front -> rear)")
        current = self.front
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()

print("Front item:", q.peek())

q.dequeue()
q.display()
