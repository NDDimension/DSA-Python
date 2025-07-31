"""
                                                                        "Bubble Sort"

=> Pushes the max value to the end of the array.

Array = [13 ,46 , 25 , 52 , 20 , 9]

It performs swap between adjacent elements if they are in wrong order.
Let's proceed and see this step by step.

1. [13,46] Correct or Not ? => Correct ; Go forward
2. [46, 25] Correct or Not ? => Not ; Swap => [25,46]
3. [46,52] Correct or Not ? => Correct ; Go forward
4. [52,20] Correct or Not ? => Not ; Swap => [20,52]
5. [52, 9] Correct or Not ? => Not ; Swap => [9,52]

Therefore after 1st Pass => [13, 25, 46, 20, 9 ,52]
Here the largest number was thrown at the end.

In the same fashion we repeat this process for the remaining elements i.e. [13, 25, 46, 20, 9] ( as [52] is sorted)


Time Complexity:

Here it is same as Selection sort => O(n^2) [ Worst / Average] as here we need to perform swaps.

But if the array is already sorted, then it will take O(n) time as no swaps.
"""

array = [13, 46, 25, 52, 20, 9]
n = len(array)

print("Original array is:", array)


def BubbleSort(array):
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


sorted_array = BubbleSort(
    array.copy()
)  # use .copy() to keep original array unchanged if needed
print("Sorted array using Bubble Sort is:", sorted_array)
