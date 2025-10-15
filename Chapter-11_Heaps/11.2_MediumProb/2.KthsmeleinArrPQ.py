"""Kth Smallest Element in an Array"""

from typing import List
import heapq


def findKthSmallest_bruteforce(nums: List[int], k: int) -> int:
    """
    Kth Smallest Element in an Array — Brute Force (Sort)

    Approach:
    - Sort the array and take the element at index k - 1 (0-based indexing).

    Complexity:
    - Time: O(n log n), where n = len(nums).
    - Space: O(n) if using sorted(); O(1) extra if you sort in-place.

    Example:
    >>> findKthSmallest_bruteforce([1, 2, 6, 4, 5, 3], 3)
    3
    """
    return sorted(nums)[k - 1]


def findKthSmallest_optimal(nums: List[int], k: int) -> int:
    """
    Kth Smallest Element in an Array — Optimal (Priority Queue / Max-Heap)

    Approach:
    - Maintain a max-heap of size k containing the k smallest elements seen so far.
      Since Python's heapq is a min-heap, store values as negatives to simulate a max-heap.
    - Initialize the heap with the first k elements (negated) and heapify (O(k)).
    - For each remaining element x:
        - If x is smaller than the current largest among the k smallest (-heap[0]),
          replace the root with -x (heapreplace).
    - After processing, -heap[0] is the k-th smallest.

    Complexity:
    - Time: O(n log k), where n = len(nums).
    - Space: O(k) additional space for the heap.

    Example:
    >>> findKthSmallest_optimal([1, 2, 6, 4, 5, 3], 3)
    3
    """
    if not 1 <= k <= len(nums):
        raise ValueError("k must be between 1 and len(nums)")

    # Max-heap of size k via negation
    heap = [-x for x in nums[:k]]
    heapq.heapify(heap)  # O(k)

    for x in nums[k:]:
        if x < -heap[0]:  # x is smaller than the current largest of the k smallest
            heapq.heapreplace(heap, -x)  # O(log k)

    return -heap[0]


# Quick checks
assert findKthSmallest_bruteforce([1, 2, 6, 4, 5, 3], 3) == 3
assert findKthSmallest_optimal([1, 2, 6, 4, 5, 3], 3) == 3
