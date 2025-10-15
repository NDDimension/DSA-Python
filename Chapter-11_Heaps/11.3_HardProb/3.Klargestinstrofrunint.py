"""
Kth Largest Element in a Stream of Integers

Design a class that finds the k-th largest element in a stream of integers.
The class should be initialized with k and an initial list of numbers.
It should support a method add(val) that appends a new integer to the stream and
returns the k-th largest element at that point.
"""

"""
Brute-Force Approach

Logic:
Maintain a list of all elements in the stream.
On each add(val):
Append val to the list.
Sort the entire list in descending order.
Return the element at index k - 1.

Time complexity:
add(val) = O(n log n) for sorting (n is the number of elements so far)
Space = O(n) for storing the full stream"""


class K:
    def __init__(self, k, nums):
        self.k = k
        self.stream = nums.copy()

    def add(self, val):
        self.stream.append(val)
        sortstream = sorted(self.stream, reverse=True)
        return sortstream[self.k - 1]


k = K(3, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(k.add(11))
print(k.add(12))
print(k.add(13))
print(k.add(14))
print(k.add(15))
print(k.add(16))
print(k.add(17))
print(k.add(18))
print(k.add(19))


"""

Optimal Approach

Use a Min Heap (size k):
Maintain a min-heap of the k largest elements seen so far.
The root of the heap is the k-th largest element.
For every new element:
If heap size < k → push to heap.
Else → compare with root: if greater, replace root (pop + push).

Time complexity:
O(log k) per insertion (add)
Space: O(k) for the heap"""

import heapq


class K:
    def __init__(self, k, nums):
        self.k = k
        self.minheap = []
        self.stream = nums.copy()

    def add(self, val):
        heapq.heappush(self.minheap, val)
        if len(self.minheap) > self.k:
            heapq.heappop(self.minheap)
        return self.minheap[0]


"""

Optimal Approach

Use a Min Heap (size k):
Maintain a min-heap of the k largest elements seen so far.
The root of the heap is the k-th largest element.
For every new element:
If heap size < k → push to heap.
Else → compare with root: if greater, replace root (pop + push).

Time complexity:
O(log k) per insertion (add)
Space: O(k) for the heap"""

import heapq


class KLargest:
    def __init__(self, k, nums):
        self.k = k
        self.minheap = []

        for num in nums:
            self.add(num)

    def add(self, val):
        heapq.heappush(self.minheap, val)
        if len(self.minheap) > self.k:
            heapq.heappop(self.minheap)
        return self.minheap[0]


kth = KLargest(3, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(kth.add(11))
print(kth.add(12))
print(kth.add(13))
print(kth.add(14))
print(kth.add(15))
print(kth.add(16))
print(kth.add(17))
print(kth.add(18))
print(kth.add(19))
