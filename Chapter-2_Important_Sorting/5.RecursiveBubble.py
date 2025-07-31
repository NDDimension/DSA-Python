# Time Complexity => O(n^2)
def RecursiveBubbleSort(arr, n):
    if n == 1:
        return

    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

    RecursiveBubbleSort(arr, n - 1)
    return arr


arr = [64, 34, 25, 12, 22, 11, 90]
print("Sorted array:", RecursiveBubbleSort(arr, len(arr)))

# Optimized Version


def OptimizedBubbleSort(arr, n):
    if n == 1:
        return arr

    didSwap = 0
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            didSwap = 1

    if didSwap == 0:
        return arr

    OptimizedBubbleSort(arr, n - 1)
    return arr


arr = [1, 2, 3, 4, 5, 6]
print("Optimized Sorted array:", OptimizedBubbleSort(arr, len(arr)))
