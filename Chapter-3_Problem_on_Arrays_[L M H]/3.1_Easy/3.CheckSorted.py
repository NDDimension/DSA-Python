"""
"Check whether the given array is Sorted or Not"

  - Iterate and compare each element with the next one.
  - If any element is greater than the next one, return False.

  - Time Complexity => O(n)
"""


def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True


arr = [1, 2, 1, 4]
print(is_sorted(arr))
