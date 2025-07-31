"""
"Sort an Array of 0s, 1s and 2s"

=> Brute Force / Better Approach :

    - Iterate and count 0,1 and 2
    - Fill the the number of places in array according to count

=> Time Complexity => O(n)
=> Space Complexity => O(1)

=> Optimal Approach:

    - Using Dutch National Flag Algorithm

3 Rules of Algo:
    - [0 to low - 1] => 0s Extreme left
    - [low to mid - 1] => 1s
    -[high + 1 to n - 1] => 2s Extreme right

=> Time Complexity => O(n)
=> Space Complexity => O(1)
"""


def sort_arraybrute(arr):
    count_0, count_1, count_2 = 0, 0, 0

    for num in arr:
        if num == 0:
            count_0 += 1
        elif num == 1:
            count_1 += 1
        else:
            count_2 += 1

    for i in range(count_0):
        arr[i] = 0

    for i in range(count_0, count_0 + count_1):
        arr[i] = 1

    for i in range(count_0 + count_1, len(arr)):
        arr[i] = 2

    return arr


from collections import Counter


def sort_array_with_counter(arr):
    count = Counter(arr)  # counts of 0s, 1s, and 2s

    index = 0
    for num in [0, 1, 2]:
        for _ in range(count.get(num, 0)):
            arr[index] = num
            index += 1

    return arr


def sort_array_with_dutch_national_flag(arr):
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1

        elif arr[mid] == 1:
            mid += 1

        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr


arr = [0, 1, 2, 0, 1, 2, 0, 1, 2]
print(sort_array_with_dutch_national_flag(arr))
