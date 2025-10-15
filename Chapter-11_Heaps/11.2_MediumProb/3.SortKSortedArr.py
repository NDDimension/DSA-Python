"""
Sort a K-Sorted (Nearly Sorted) Array — Optimal (Priority Queue / Min-Heap)

Definition:
- A K-sorted array is one where each element is at most k positions away from its
  target position in the fully sorted array.

Approach:
- Use a min-heap of size k + 1:
  1) Heapify the first k + 1 elements.
  2) For each remaining element x:
     - Push x and pop the smallest to the output (heappushpop).
  3) Pop and append all remaining elements from the heap.
- This leverages the fact that the smallest element among the next k + 1 candidates
  will be the next in sorted order.

Complexity:
- Time: O(n log (k + 1)), where n = len(arr).
- Space: O(k) for the heap.

Constraints:
- k >= 0. If k >= n - 1, this reduces to a standard sort.

Example:
>>> sort_k_sorted_optimal([6, 5, 3, 2, 8, 10, 9], 3)
[2, 3, 5, 6, 8, 9, 10]
"""

import heapq


def sort_k_sorted_optimal(arr, k):
    n = len(arr)
    if n == 0:
        return []
    if k < 0:
        raise ValueError("k must be non-negative")

    k = min(k, n - 1)  # handle k >= n
    heap = arr[: k + 1]
    heapq.heapify(heap)

    result = []

    for x in arr[k + 1 :]:
        result.append(heapq.heappushpop(heap, x))  # push new, pop smallest

    # Drain the remaining heap
    while heap:
        result.append(heapq.heappop(heap))

    return result


sort_k_sorted_optimal([6, 5, 3, 2, 8, 10, 9], 3)
