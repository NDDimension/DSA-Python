"""
"Merge Overlapping Sub-intervals"

=> Given an array of subintervals we need to merge overlapping subintervals and
    return the minimum array of subintervals.
"""

"""
=> Brute Force:

    - Iterate and check if subintervals can be merged.
 
=> Time Complexity ~ O(n log n) + O(2n)
=> Space Complexity ~ O(n)
    
"""


def mergeOverlapBrute(arr):
    n = len(arr)
    arr.sort()
    ans = []

    for i in range(n):
        start, end = arr[i][0], arr[i][1]

        if ans and end <= ans[-1][1]:
            continue

        for j in range(i + 1, n):
            if arr[j][0] <= end:
                end = max(end, arr[j][1])

            else:
                break

        ans.append([start, end])

    return ans


arr = [[1, 3], [8, 10], [2, 6], [15, 18]]
mergeOverlapBrute(arr)

"""
=> Optimal Approach:

    - checking the last interval for overlapping

=> Time Complexity ~ O(n log n) + O(n)
=> Space Complexity ~ O(n)

"""


def mergeOverlapOptimal(arr):
    n = len(arr)
    arr.sort()
    ans = []

    for i in range(n):
        if not ans or arr[i][0] > ans[-1][1]:
            ans.append(arr[i])

        else:
            ans[-1][1] = max(ans[-1][1], arr[i][1])

    return ans


arr = [[1, 3], [8, 10], [2, 6], [15, 18]]
mergeOverlapOptimal(arr)
