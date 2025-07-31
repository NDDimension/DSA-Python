"""
"Move all 0s to end "

=> Brute Force:

    - Iterate and append non-zero elements to a new list
    - Move all non zero to front of the list
    - Iterate from size of non zero to end of list and append 0s

=> Time Complexity => O(n) + O(x) + O(n - x) = O(2n)
=> Space Complexity => O(x) (for new list)

=> Optimal Approach:

    - Iterate through the list
    - Use two pointers, one -> non-zero , another -> zero
    - Swap non-zero with zero if pointer is at zero

=> Time Complexity => O(n)
=> Space Complexity => O(1)
"""


def nonzBrute(arr):
    temp = []

    for i in range(len(arr)):
        if arr[i] != 0:
            temp.append(arr[i])

    for i in range(len(temp)):
        arr[i] = temp[i]

    for i in range(len(temp), len(arr)):
        arr[i] = 0

    return arr


def nonzOptimal(arr):
    j = -1
    for i in range(len(arr)):
        if arr[i] == 0:
            j = i
            break

    for i in range(j + 1, len(arr)):
        if arr[i] != 0:
            arr[j], arr[i] = arr[i], arr[j]
            j += 1

    return arr


arr = [1, 0, 2, 0, 3, 4, 0, 5]
print(nonzOptimal(arr))
