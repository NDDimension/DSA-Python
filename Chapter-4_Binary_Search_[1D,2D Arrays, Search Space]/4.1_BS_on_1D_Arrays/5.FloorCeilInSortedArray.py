"""
"Floor and Ceil in Sorted Array"

Floor -> largest num >= target
Ceil -> smallest num >= target

=> Given an array we need to fit the target by considering floor and ceil

Example:
arr = [10, 20 , 30 , 40 , 50]
target = 25

ceil[25] = 30
floor[25] = 20

hence it should be inserted between 20 and 30.
"""


def floor(nums, target):
    # Floor -> greates <= target
    n = len(nums)
    low = 0
    high = n - 1
    floor = -1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] <= target:
            floor = nums[mid]
            low = mid + 1

        else:
            high = mid - 1

    return floor


def ceil(nums, target):
    # Ceil -> smallest >= target
    n = len(nums)
    low = 0
    high = n - 1
    ceil = -1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] >= target:
            ceil = nums[mid]
            high = mid - 1

        else:
            low = mid + 1

    return ceil


def getFloorAndCeil(arr, target):
    f = floor(nums, target)
    c = ceil(nums, target)
    return (f, c)


nums = [10, 20, 30, 40, 50]
target = 25
print(getFloorAndCeil(nums, target))
