"""
Kth Largest Element in an Array (Priority Queue / Min-Heap)

Given an integer array nums and an integer k, return the k-th largest element in the array (1-indexed).
Note: It is the k-th largest in sorted order, not the k-th distinct element.

Approach (Priority Queue / Min-Heap):
- Maintain a min-heap of size k containing the k largest elements seen so far.
- Initialize the heap with the first k elements (heapify in O(k)).
- For each remaining element x in nums[k:], if x > heap[0], replace the smallest element with x (heapreplace).
- After processing all elements, heap[0] is the k-th largest.

Complexity:
- Time: O(n log k), where n = len(nums). Heapify is O(k); each replacement is O(log k).
- Space: O(k) additional space for the heap.

Constraints:
- 1 <= k <= len(nums)

Examples:
>>> findKthLargest([3, 2, 1, 5, 6, 4], 2)
5
>>> findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
4
"""

"""Brute Force
    Approach:
    - Sort the array and take the element at index -k.

    Complexity:
    - Time: O(n log n), where n = len(nums).
    - Space: O(n) if using sorted(); O(1) extra if you sort in-place."""


def findKthLargest(nums, k):
    return sorted(nums)[-k]


findKthLargest([3, 2, 1, 5, 6, 4], 2)

"""Optimal Approach
    Approach:
    - Maintain a min-heap of the k largest elements seen so far.
    - Heapify the first k elements (O(k)).
    - For each remaining element x, if x > heap[0], replace heap[0] with x (heapreplace).
    - The root of the heap (heap[0]) is the k-th largest.

    Complexity:
    - Time: O(n log k), where n = len(nums).
    - Space: O(k) additional space for the heap."""


def findKthLargest(nums, k):
    import heapq

    heap = nums[:k]
    heapq.heapify(heap)
    for x in nums[k:]:
        if x > heap[0]:
            heapq.heapreplace(heap, x)
    return heap[0]


findKthLargest([3, 2, 1, 5, 6, 4], 2)
