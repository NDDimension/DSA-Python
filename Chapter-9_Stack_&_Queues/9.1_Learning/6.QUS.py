from queue import LifoQueue


class MyQueue:
    def __init__(self):
        """
        Initialize two LifoQueues to simulate a FIFO queue.
        """
        self.stack_in = LifoQueue()
        self.stack_out = LifoQueue()

    def push(self, x: int) -> None:
        """
        Enqueue element to the back of the queue.
        Time: O(1)
        """
        self.stack_in.put(x)

    def pop(self) -> int:
        """
        Dequeue the element from the front of the queue.
        Time: Amortized O(1)
        """
        if self.empty():
            return -1
        self._transfer()
        return self.stack_out.get()

    def peek(self) -> int:
        """
        Get the front element without removing it.
        Time: Amortized O(1)
        """
        if self.empty():
            return -1
        self._transfer()
        front = self.stack_out.get()
        self.stack_out.put(front)
        # Reorder the stack_out after peeking
        self._reorder_stack_out()
        return front

    def empty(self) -> bool:
        """
        Returns True if the queue is empty.
        Time: O(1)
        """
        return self.stack_in.empty() and self.stack_out.empty()

    def _transfer(self):
        """
        Move all elements from stack_in to stack_out if stack_out is empty.
        This reverses the order for correct FIFO behavior.
        """
        if self.stack_out.empty():
            while not self.stack_in.empty():
                self.stack_out.put(self.stack_in.get())

    def _reorder_stack_out(self):
        """
        Reorders stack_out after peek (since get() removed the top).
        """
        temp = []
        while not self.stack_out.empty():
            temp.append(self.stack_out.get())
        for item in reversed(temp):
            self.stack_out.put(item)

    def display(self):
        """
        Prints the current contents of the queue from front to back.
        Does not modify the original queue.
        """
        # First, transfer if needed to get front items in stack_out
        self._transfer()

        if self.stack_out.empty():
            print("Queue is empty!")
            return

        # Extract items temporarily
        temp = []
        while not self.stack_out.empty():
            temp.append(self.stack_out.get())

        # Print and restore
        print("Queue contents (front to back):")
        for item in temp:
            print(item, end=" ")
        print()

        # Put items back into stack_out
        for item in reversed(temp):
            self.stack_out.put(item)


q = MyQueue()
q.push(10)
q.push(20)
q.push(30)

q.display()
# Output:
# Queue contents (front to back):
# 10 20 30

q.pop()
q.display()
# Output:
# Queue contents (front to back):
# 20 30

from queue import LifoQueue


class Queue:
    """
    Queue implementation using two LIFO stacks (LifoQueue).
    Maintains FIFO behavior by reversing the stack during push.
    """

    def __init__(self):
        self.input = LifoQueue()
        self.output = LifoQueue()

    def push(self, data: int) -> None:
        """
        Enqueue an element to the back of the queue.
        Time complexity: O(n)
        """
        # Move all elements to output
        while not self.input.empty():
            self.output.put(self.input.get())

        print("The element pushed is", data)
        # Push new element
        self.input.put(data)

        # Move everything back
        while not self.output.empty():
            self.input.put(self.output.get())

    def pop(self) -> int:
        """
        Dequeue the front element.
        Returns:
            int: The front element or exits if queue is empty.
        """
        if self.input.empty():
            print("Queue is empty!")
            exit(0)
        return self.input.get()

    def front(self) -> int:
        """
        Returns the front element without removing it.
        Returns:
            int: The front element or exits if queue is empty.
        """
        if self.input.empty():
            print("Queue is empty!")
            exit(0)
        return self.input.queue[-1]  # last in = front

    def size(self) -> int:
        """
        Returns the number of elements in the queue.
        """
        return self.input.qsize()

    def display(self) -> None:
        """
        Prints the queue from front to back.
        Does not modify the queue.
        """
        if self.input.empty():
            print("Queue is empty!")
            return

        print("Queue contents (front to back):")
        for item in reversed(self.input.queue):
            print(item, end=" ")
        print()


if __name__ == "__main__":
    q = Queue()
    q.push(3)
    q.push(4)
    q.display()  # Output: 3 4

    print("The element popped is", q.pop())  # Output: 3
    q.push(5)
    q.display()  # Output: 4 5

    print("The front of the queue is", q.front())  # Output: 4
    print("The size of the queue is", q.size())  # Output: 2
