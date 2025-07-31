"""
"Next Permutation"

=> Given [1,2,3]
=> Next Permutation is [1,3,2]

=> All possible permutations: [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]

=> Brute Force :

    - Generate all possible permutations
    = Find the next permutation

=> Time Complexity => O(n! x n)

=> Optimal Approach :

    - try to find the longest prefix match till breakpoint a[i] < a[i + 1]
    - find the next higher than breakpoint but smallest
    - arrange the remaining in ascending order to keep the number small

=> Time Complexity = O(n) + O(n) + O(n) = O(3n)
=> Space Complexity = O(1)

"""


def next_perm(arr):
    ind = -1

    for i in range(len(arr) - 2, -1, -1):
        if arr[i] < arr[i + 1]:
            ind = i
            break

    if ind == -1:
        arr.reverse()
        return arr

    for i in range(len(arr) - 1, ind, -1):
        if arr[i] > arr[ind]:
            arr[i], arr[ind] = arr[ind], arr[i]
            break

    arr[ind + 1 :] = reversed(arr[ind + 1 :])

    return arr


arr = [2, 1, 5, 4, 3, 0, 0]
print(next_perm(arr))
