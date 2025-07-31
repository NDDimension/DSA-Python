"""
"Binary Search to find out X in Sorted Array"

=> Given an array which is sorted we need to find an element using binary search.
=> How it works ? so first split into two halves -> check if middle is our X -> if not then check for gt or lt
=> According to that if greater then right side of middle else left side of middle.
=> Do this until low and high points to the same index.
=> Search space is available from low -> high if they cross each other we are done and no more space to search

=> Time Complexity : O(log_base2 n)
=> Space Complexity : O(1)

=> For overflow cases use :
    middle = low  + (high - low) // 2
"""

"""
=> Iterative Method
    - basic loop structure to find X
"""


def bs_iterative(nums, target):
    n = len(nums)
    low = 0
    high = n - 1

    while low <= high:
        middle = (low + high) // 2

        if nums[middle] == target:
            return middle
        elif nums[middle] < target:
            low = middle + 1
        else:
            high = middle - 1
    return -1


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target1 = 5
target2 = 1
target3 = 10
target4 = 11

print("Binary Search All Cases\n")
print("Middle => ", bs_iterative(nums, target1))
print("Low => ", bs_iterative(nums, target2))
print("High => ", bs_iterative(nums, target3))
print("Not present => ", bs_iterative(nums, target4))

"""
=> Recursive Method
    - using main steps in direct function calling
"""


def bs_recursive(nums, target, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2
    if nums[mid] == target:
        return mid

    elif target > nums[mid]:
        return bs_recursive(nums, target, mid + 1, high)

    return bs_recursive(nums, target, low, mid - 1)


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

target1 = 5
target2 = 1
target3 = 10
target4 = 11

print("\nBinary Search All Cases\n")
print("Middle => ", bs_recursive(nums, target1, 0, len(nums) - 1))
print("Low => ", bs_recursive(nums, target2, 0, len(nums) - 1))
print("High => ", bs_recursive(nums, target3, 0, len(nums) - 1))
print("Not present => ", bs_recursive(nums, target4, 0, len(nums) - 1))
