"""
"Find Peak Element"

=> Given an array we need to return the "peak element".

-> Peak Element = arr[i - 1] < arr[i] > arr[i + 1]

Points to remember :
    - there can be multiple peaks
    - assume "-inf" on both sides of array to find out peak.
"""


# Using Linear :
# TC : O(N) , SC : O(1)
def peak_linear(arr):
    n = len(arr)

    for i in range(n):
        if (i == 0 or arr[i] > arr[i + 1]) and (i == n - 1 or arr[i] > arr[i - 1]):
            return str(i) + "th index", "element " + str(arr[i])

    return -1


arr = [1, 2, 3, 4, 5, 4, 3, 2, 1]
print(peak_linear(arr))


# using Binary Search
# TC : O(logN) , SC : O(1)


def peak_binary(arr):
    n = len(arr)
    if n == 1:
        return arr[0]
    if arr[0] > arr[1]:
        return arr[0]
    if arr[n - 1] > arr[n - 2]:
        return arr[n - 1]

    low = 1
    high = n - 2

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
            return arr[mid]

        elif arr[mid] > arr[mid - 1]:
            low = mid + 1

        else:
            high = mid - 1

    return -1


arr = [1, 2, 3, 4, 5, 4, 3, 2, 1]
arr1 = [1, 2, 3, 4, 5, 6]
arr2 = [6, 5, 4, 3, 2, 1]
arr3 = [1, 5, 1, 2, 1]
print(peak_binary(arr3))
print(peak_binary(arr1))
print(peak_binary(arr2))
