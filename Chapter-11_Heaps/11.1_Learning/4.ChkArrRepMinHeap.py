"""
Check if the given array represents a valid Min Heap.

In a Min Heap, for every node at index i:
    - The value at i should be <= its children (if they exist)

Args:
    arr (List[int]): The array to check.

Returns:
    bool: True if the array is a valid min heap, False otherwise.
"""


def is_MinHeap(nums):
    n = len(nums)
    for i in range((n - 2) // 2 + 1):
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and nums[i] > nums[left]:
            return False
        if right < n and nums[i] > nums[right]:
            return False
    return True


arr = [4, 2, 3, 1, 5]
print(is_MinHeap(arr))

arr = [4, 2, 3, 1, 5, 6]
print(is_MinHeap(arr))

print(is_MinHeap([1, 3, 5, 7, 9, 8]))
