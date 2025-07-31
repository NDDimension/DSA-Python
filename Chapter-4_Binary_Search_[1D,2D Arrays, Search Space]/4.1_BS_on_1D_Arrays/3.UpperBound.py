"""
"Upper Bound"

=> Given an array return the upper bound => smallest index such that 'arr[index] > n'.

Example :
arr = [3,5,8,15,19] ; n = 8 , ub?

=> arr[0] = 3 > 8 => False
=> arr[1] = 5 > 8 => False
=> arr[2] = 8 > 8 => False
=> arr[3] = 15 > 8 => True
hence the ub = 3

=> Time Complexity : O(log_base2 n)
=> Space Complexity : O(1)
"""


def upper_bound(arr, x):
    n = len(arr)
    low = 0
    high = n - 1
    ans = n

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans


arr = [3, 5, 8, 15, 19]
n = 8
print(upper_bound(arr, n))
