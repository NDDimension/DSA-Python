"""
"Largest element in the Array"

=> Brute Force approach :

    - Sort in ascending
    - Last element is the largest

    -Time Complexity => O(n log n)

=> Optimal Approach:

    - Take a variable to store largest.
    - Iterate over doing comparison and store the largest

    - Time Complexity => O(n)
"""


def LargestinArr(arr):
    largest = arr[0]

    for i in range(len(arr)):
        if arr[i] > largest:
            largest = arr[i]

    return largest


arr = [3, 4, 5, 2, 1, 100]
print(f"Largest found in array is => {LargestinArr(arr)}")
