"""Min Heap using a list"""


class MinHeap:
    """
    A simple Min Heap implementation using a list.

    In a Min Heap, the smallest element is always at the root (index 0).
    Each parent node is less than or equal to its child nodes.

    Attributes:
        heap (List[int]): Internal list representing the heap.
    """

    def __init__(self):
        """Initialize an empty Min Heap."""
        self.heap = []

    def insert(self, val):
        """
        Insert a new value into the heap.

        Args:
            val (int): The value to be inserted.
        """
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        """
        Remove and return the smallest value (root) from the heap.

        Returns:
            int: The smallest value in the heap.

        Raises:
            IndexError: If the heap is empty.
        """
        if not self.heap:
            raise IndexError("Heap is empty")

        min_val = self.heap[0]
        last_val = self.heap.pop()

        if self.heap:
            self.heap[0] = last_val
            self._heapify_down(0)

        return min_val

    def peek(self):
        """
        Return the smallest value without removing it.

        Returns:
            int: The smallest value in the heap.

        Raises:
            IndexError: If the heap is empty.
        """
        if not self.heap:
            raise IndexError("Heap is empty")
        return self.heap[0]

    def _heapify_up(self, index):
        """
        Move the value at the given index up to maintain heap property.

        Args:
            index (int): Index of the element to heapify up.
        """
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)

    def _heapify_down(self, index):
        """
        Move the value at the given index down to maintain heap property.

        Args:
            index (int): Index of the element to heapify down.
        """
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2
        size = len(self.heap)

        if left < size and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < size and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.heap[index], self.heap[smallest] = (
                self.heap[smallest],
                self.heap[index],
            )
            self._heapify_down(smallest)

    def __len__(self):
        """
        Return the number of elements in the heap.

        Returns:
            int: Size of the heap.
        """
        return len(self.heap)


heap = MinHeap()
heap.insert(10)
heap.insert(5)
heap.insert(7)

print(heap.peek())
print(heap.pop())
print(heap.peek())
print(heap.pop())


"""Min Heap using heapq"""
import heapq


class MinHeapq:
    """
    A Min Heap wrapper using Python's built-in heapq module.

    The heapq module provides an efficient implementation of a binary min-heap
    using a regular Python list.

    Attributes:
        heap (List[int]): Internal list used as the heap.
    """

    def __init__(self):
        """Initialize an empty Min Heap."""
        self.heap = []

    def insert(self, val):
        """
        Insert a new value into the heap.

        Args:
            val (int): The value to be inserted.
        """
        heapq.heappush(self.heap, val)

    def pop(self):
        """
        Remove and return the smallest value from the heap.

        Returns:
            int: The smallest value in the heap.

        Raises:
            IndexError: If the heap is empty.
        """
        if not self.heap:
            raise IndexError("Heap is empty")
        return heapq.heappop(self.heap)

    def peek(self):
        """
        Return the smallest value without removing it.

        Returns:
            int: The smallest value in the heap.

        Raises:
            IndexError: If the heap is empty.
        """
        if not self.heap:
            raise IndexError("Heap is empty")
        return self.heap[0]

    def __len__(self):
        """
        Return the number of elements in the heap.

        Returns:
            int: Size of the heap.
        """
        return len(self.heap)


heap = MinHeapq()
heap.insert(10)
heap.insert(5)
heap.insert(7)

print(heap.peek())
print(heap.pop())
print(heap.pop())
