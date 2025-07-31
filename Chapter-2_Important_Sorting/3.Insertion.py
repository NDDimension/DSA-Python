"""
                                                "Insertion Sort"

=> Takes an element and place it in its correct position.

Array = [14, 9, 15, 12, 6, 8, 13]

Lets see it step by step:

1, [14] => 14 At correct ? Yes -> No change

2. [14, 9] => 9 At correct ? No -> Move 9 to left of 14

3. [9, 14, 15] => 15 At correct ? Yes -> No change

4. [9, 14, 15 ,12] => 12 At correct ? No -> Move 12 to left of 15
    [9, 14, 12, 15] => 12 At correct ? No -> Move 12 to left of 14
    [9, 12, 14, 15] => 12 At correct ? Yes -> No change

5. [9, 12, 14, 15, 6] => 6 At correct ? No -> Move 6 to left of 15
    [9 , 12, 14, 6, 15] => 6 At correct ? No -> Move 6 to left of 14
    [9, 12, 6, 14, 15] => 6 At correct ? No -> Move 6 to left of 12
    [9, 6, 12, 14, 15] => 6 At correct? No -> Move 6 to left of 9
    [6, 9, 12, 14, 15] => 6 At correct? Yes -> No change

In this fashion we will move till the end and do swaps if needed till we sort the array.

Time Complexity:

This one is also same as Selection and Bubble sort.
Hence the time complexity is O(n^2) [Worst / Average ]

But if the array is sorted then it will take O(n) time as it only
iteraters over the array once and no comparison and swaps are made.
"""

array = [14, 9, 15, 12, 6, 8, 13]
n = len(array)

print("Original Array =>", array)


def InsertionSort(array):
    for i in range(n):
        j = i
        while j > 0 and array[j - 1] > array[j]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1

    return array


print("Sorted Array =>", InsertionSort(array))
