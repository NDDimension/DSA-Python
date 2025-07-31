"""
"Quick Sort"

=> Sort in Asc -> Minor Tweak -> Can sort in Desc Order also.

Given array => [4, 6, 2, 5, 7, 9, 1, 3]

1. Pick a pivot element .
    -- Pivot can be -> 1st ele , Last ele , Median , Random ele.

2. Put it at its correct place in sorted array.
    -- Here, we are using 1st element as pivot.

So its like => [4, 6, 2, 5, 7, 9, 1, 3]
sorted array => [1, 2, 3, 4, 5, 6, 7, 9]

Pick "4" -> Correct place is 4th position in sorted array -> Place it there.

Now, repeat this process for remaining elements.
At the end, array will be sorted.

3. Remeber this -> Smaller on Left / Larger on Right. -> Need to do this for one step

ex=> We picked 4 as pivot. -> Placed it at 4th position.
Now on its left => [2, 1, 3] i.e. SMALLER
On its right => [6, 5, 7, 9] i.e. LARGER

Hence after 1st pass One element is in its correct position.

Let us see this one more time:
now for the smaller array [2, 1, 3]
We pick 1 as pivot. -> Correct place is 2nd position in sorted array -> Place it there.    [1, 2, 3]
Smaller on left => [1] and Larger on right => [3] done.

Time Complexity:

Same as Merge Sort => O(n log n)

Space Complexity: => O(1)

"""


def QuickSort(array, low, high):
    if low < high:
        partition_index = partition(array, low, high)
        QuickSort(array, low, partition_index - 1)
        QuickSort(array, partition_index + 1, high)
    return array


def partition(array, low, high):
    pivot = array[low]  # pivot value, not index
    i = low + 1
    j = high

    while True:
        while i <= high and array[i] <= pivot:
            i += 1
        while j >= low and array[j] > pivot:
            j -= 1

        if i >= j:
            break
        array[i], array[j] = array[j], array[i]

    array[low], array[j] = array[j], array[low]
    return j


array = [4, 6, 2, 5, 7, 9, 1, 3]
QuickSort(array, 0, len(array) - 1)
print(array)
