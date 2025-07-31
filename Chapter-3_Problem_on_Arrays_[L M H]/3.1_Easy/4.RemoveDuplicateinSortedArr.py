"""
"Remove Duplicates from a sorted array"

=> Brute Force:
    - Iterate and add to set

    - Time Complexity => O(n log n) + O(n)

=> Optimal Approach:

    - Compare with two pointers and place order wise

    - Time Complexity => O(n)

"""


# This code is is useful for unsorted array as
# it doesnt preserve order
def remDuplicates(arr):
    arr = list(set(arr))
    return arr, len(arr)


# This one is faster and preserves order also memory efficient
def remDuplicates2pointer(arr):
    i = 0
    for j in range(len(arr)):
        if arr[j] != arr[i]:
            arr[i + 1] = arr[j]
            i += 1

    return arr[: i + 1], i + 1


arr = [1, 1, 2, 2, 3, 3]
print(remDuplicates2pointer(arr))
