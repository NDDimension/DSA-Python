"""
"Search Insert Position"

=> Given an array return index if element present else return index where it should be inserted

Example :
arr = [3,5,8,15,19] ; n = 7 , lb?

=> arr[0] = 3 > 8 => False
=> arr[1] = 5 > 8 => False
=> arr[2] = 8 >= 7 => True
hence the lb = 2 so added at index 2

=> Time Complexity : O(log_base2 n)
=> Space Complexity : O(1)
"""


def SearchInsertPosition(arr, x):
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
n = 7
print(SearchInsertPosition(arr, n))
