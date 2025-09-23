from queue import Queue


class StackUsingQueue:
    """
    Stack implementation using a single queue (FIFO) from Python's queue module.

    Logic:
    - push(x): Add element and rotate the queue to simulate LIFO.
    - pop(): Remove the front element (which is the top of the stack).
    - top(): Peek the front element.
    - size(): Return the current size of the stack.
    """

    def __init__(self):
        self.q = Queue()

    def push(self, x):
        """
        Pushes an element onto the stack.

        Args:
            x: Element to be pushed.
        """
        s = self.q.qsize()
        self.q.put(x)
        for _ in range(s):
            self.q.put(self.q.get())
        print(f"Pushed : {x}")

    def pop(self):
        """
        Removes and returns the top element from the stack.

        Returns:
            The top element, or None if the stack is empty.
        """
        if self.q.empty():
            print("Stack is empty cannot Pop")
            return None
        print(f"Popped : {self.q.get()}")

    def top(self):
        """
        Returns the top element without removing it.

        Returns:
            The top element, or None if the stack is empty.
        """
        if self.q.empty():
            print("Stack is empty")
            return None
        return self.q.queue[0]

    def size(self):
        """
        Returns the size of the stack.

        Returns:
            int: Number of elements in the stack.
        """
        return self.q.qsize()

    def print_stack(self):
        """
        Prints the contents of the stack from top to bottom.
        Does not modify the original stack.
        """

        if self.q.empty():
            print("Stack is empty!")
            return

        print("Stack contents (top to bottom):")
        # Convert queue to a list to safely iterate
        temp_list = list(self.q.queue)
        for item in temp_list:
            print(item)


s = StackUsingQueue()
s.push(1)
s.push(2)
s.push(3)
s.print_stack()
s.top()
s.pop()
s.size()
