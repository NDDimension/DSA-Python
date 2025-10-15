def min_to_max(nums):
    def heapify(nums, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and nums[left] > nums[largest]:
            largest = left

        if right < n and nums[right] > nums[largest]:
            largest = right

        if largest != i:
            nums[i], nums[largest] = nums[largest], nums[i]
            heapify(nums, n, largest)

    n = len(nums)
    maxheap = nums[:]

    for i in reversed(range(n // 2)):
        heapify(maxheap, n, i)

    return maxheap


min_heap = [1, 3, 5, 7, 9, 8]
max_heap = min_to_max(min_heap)

print("Original Min Heap:", min_heap)
print("Converted Max Heap:", max_heap)
