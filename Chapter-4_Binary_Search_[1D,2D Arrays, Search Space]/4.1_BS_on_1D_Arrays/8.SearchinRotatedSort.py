"""
# Unique Elements
"Search in a Rotated Sorted Array"

=> Given a rotated sorted array we need to find the index of our target.

Example :
arr = [7,8,9,1,2,3,4,5,6]

-> It is sorted from 1 to 6 and rotated from 7
-> Need to find target = 1

Ans -> 1 is at index 3

Trick here is ? -> Identify the sorted half as it will be eliminated.

=> Time Complexity : O(logn)
=> Space Complexity : O(1)
"""


def findXinRotSort(arr, target):
    n = len(arr)
    low, high = 0, n - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid

        # Left Sorted
        if arr[low] <= arr[mid]:
            if arr[low] <= target and arr[mid] >= target:
                high = mid - 1
            else:
                low = mid + 1

        # Right Sorted
        else:
            if arr[mid] <= target and arr[high] >= target:
                low = mid + 1
            else:
                high = mid - 1

    return -1


arr = [7, 8, 9, 1, 2, 3, 4, 5, 6]
target = 1
print(findXinRotSort(arr, target))

"""
# Containing Duplicates
"Search in a Rotated Sorted Array II"

=> The only problem here is the case where;

arr[low] = arr[mid] = arr[high]
and we can not find which part is sorted and which is not .

Trick here is ? -> We shrink the search space if we get caught in problem.
so right after mid check we will do some magic.

=> Time Complexity : O(logn) mostly 
but if there are more duplicates then ~ O(n/2)

=> Space Complexity : O(1)
"""


def findXinRotSortDuplicates(arr, target):
    n = len(arr)
    low, high = 0, n - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return True

        # Magic For catching Duplicates
        if arr[low] == arr[mid] == arr[high]:
            low += 1
            high -= 1
            continue

        # Left Sorted
        if arr[low] <= arr[mid]:
            if arr[low] <= target and arr[mid] >= target:
                high = mid - 1
            else:
                low = mid + 1

        # Right Sorted
        else:
            if arr[mid] <= target and arr[high] >= target:
                low = mid + 1
            else:
                high = mid - 1

    return False


arr = [3, 1, 2, 3, 3, 3, 3]
target = 3
print(findXinRotSortDuplicates(arr, target))
