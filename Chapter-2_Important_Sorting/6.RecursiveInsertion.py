def RecursiveInsertionSort(arr, i, n):
    if i == n:
        return

    j = i
    while j > 0 and arr[j - 1] > arr[j]:
        arr[j], arr[j - 1] = arr[j - 1], arr[j]
        j -= 1

    RecursiveInsertionSort(arr, i + 1, n)
    return arr


arr = [12, 11, 13, 5, 6]
print("Sorted array is:", RecursiveInsertionSort(arr, 0, len(arr)))
