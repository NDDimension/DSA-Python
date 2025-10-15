class MaxHeap:
    """
    A simple Max Heap implementation using a list.

    In a Max Heap, the largest element is always at the root (index 0).
    Each parent node is greater than or equal to its child nodes.

    Attributes:
        heap (List[int]): Internal list representing the heap.
    """

    def __init__(self):
        """Initialize an empty Max Heap."""
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
        Remove and return the largest value (root) from the heap.

        Returns:
            int: The largest value in the heap.

        Raises:
            IndexError: If the heap is empty.
        """
        if not self.heap:
            raise IndexError("Heap is empty")

        max_val = self.heap[0]
        last_val = self.heap.pop()

        if self.heap:
            self.heap[0] = last_val
            self._heapify_down(0)

        return max_val

    def peek(self):
        """
        Return the largest value without removing it.

        Returns:
            int: The largest value in the heap.

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
        if index > 0 and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)

    def _heapify_down(self, index):
        """
        Move the value at the given index down to maintain heap property.

        Args:
            index (int): Index of the element to heapify down.
        """
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2
        size = len(self.heap)

        if left < size and self.heap[left] > self.heap[largest]:
            largest = left
        if right < size and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

    def __len__(self):
        """
        Return the number of elements in the heap.

        Returns:
            int: Size of the heap.
        """
        return len(self.heap)


heap = MaxHeap()
heap.insert(10)
heap.insert(5)
heap.insert(15)

print(heap.peek())
print(heap.pop())
print(heap.pop())

"""Max Heap using heapq"""
import heapq


class MaxHeap:
    """
    A Max Heap wrapper using Python's heapq module by inverting values.

    Since heapq only supports Min Heap, we invert values to simulate Max Heap behavior.

    Attributes:
        heap (List[int]): Internal list used as the heap (with negated values).
    """

    def __init__(self):
        """Initialize an empty Max Heap."""
        self.heap = []

    def insert(self, val):
        """
        Insert a new value into the heap.

        Args:
            val (int): The value to be inserted.
        """
        heapq.heappush(self.heap, -val)

    def pop(self):
        """
        Remove and return the largest value from the heap.

        Returns:
            int: The largest value in the heap.

        Raises:
            IndexError: If the heap is empty.
        """
        if not self.heap:
            raise IndexError("Heap is empty")
        return -heapq.heappop(self.heap)

    def peek(self):
        """
        Return the largest value without removing it.

        Returns:
            int: The largest value in the heap.

        Raises:
            IndexError: If the heap is empty.
        """
        if not self.heap:
            raise IndexError("Heap is empty")
        return -self.heap[0]

    def __len__(self):
        """
        Return the number of elements in the heap.

        Returns:
            int: Size of the heap.
        """
        return len(self.heap)


heap = MaxHeap()
heap.insert(10)
heap.insert(5)
heap.insert(15)

print(heap.peek())
print(heap.pop())
print(heap.pop())
