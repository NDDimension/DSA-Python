"""
"Linear Search"

=> Time Complexity: O(n)
=> Space Complexity: O(1)


"""


def LinearSearch(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1


arr = [2, 3, 4, 10, 40]
x = 10
print(f"{x} -> index {LinearSearch(arr, x)}")
