"""
"Left Rotate an Array by D places"

=> Brute Force :

    - Store D ele in temp array
    - Iterate for remaining and store them at "i-d"
    - Now place the temp array ele in  n-dth position

=> Time Complexity => O(n + d)
=> Space Complexity => O(d)

=> Optimal Approach :

    - Reverse array 0 to d
    - Reverse array d to n-1
    - Reverse the whole array

=> Time Complexity => ~ O(n)
=> Space Complexity => O(1)

"""


def LeftRotBrute(arr, d):
    temp = arr[:d]
    for i in range(d, len(arr)):
        arr[i - d] = arr[i]

    for i in range(len(arr) - d, len(arr)):
        arr[i] = temp[i - len(arr) + d]

    return arr


def LeftRotOptimal(arr, d):
    d = d % len(arr)  # Handle cases where d > len(arr)
    return arr[d:] + arr[:d]


def RightRotateOptimal(arr, d):
    d = d % len(arr)  # To handle cases where d > len(arr)
    return arr[-d:] + arr[:-d]


arr = [1, 2, 3, 4, 5, 6, 7]
d = 8
print(LeftRotOptimal(arr, d))
