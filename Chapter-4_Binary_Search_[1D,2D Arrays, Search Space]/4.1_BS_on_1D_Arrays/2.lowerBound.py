"""
"Lower Bound"

=> Given an array return the lower bound => smallest index such that 'arr[index] >= n'.

Example :
arr = [3,5,8,15,19] ; n = 8 , lb?

=> arr[0] = 3 > 8 => False
=> arr[1] = 5 > 8 => False
=> arr[2] = 8 >= 8 => True
hence the lb = 2

=> Time Complexity : O(log_base2 n)
=> Space Complexity : O(1)
"""


def lower_bound(arr, x):
    n = len(arr)
    low = 0
    high = n - 1
    ans = n

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans


arr = [3, 5, 8, 15, 19]
n = 8
print(lower_bound(arr, n))
