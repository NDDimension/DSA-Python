"""
"Left Rotate by 1 place"

array = [1, 2, 3, 4, 5]
left rotated array = [2,3,4,5,1]

=> Time Complexity: O(n)
=> Space Complexity: O(1) [ no extra space]
=> Space Complexity : O(n) [ for algo ]

"""


def leftRot1(arr):
    temp = arr[0]

    for i in range(1, len(arr)):
        arr[i - 1] = arr[i]

    arr[len(arr) - 1] = temp
    return arr


arr = [1, 2, 3, 4, 5]
print("Left rotated array is: ", leftRot1(arr))
