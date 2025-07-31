"""
                                                                                    "Merge Sort"

=> Divide + Merge

Given array = [ 3 , 1 ,  2 ,  4 ,  1 , 5 ,  2 , 6 , 4]    => n = 9

                                                                                    [ 3, 1 , 2 , 4 , 1 , 5 , 2 , 6 , 4 ]     => Divide into 2 halves : either 5/4 or 4/5

                                                                             [3, 1, 2, 4, 1]                     [5, 2, 6, 4]

                                                                        [3, 1, 2]      [4, 1]                 [5,2]    [6, 4]

                                                                 [3, 1 ]     [2]     [4]  [1]              [5] [2]     [6]   [4]

        No further division possible             [3]       [1]

Now as single elements can't be divided further so we "Merge" them but in "Sorted" order.

=> Merge Step                                         [3]  [1] => [1,3]

                                                                   [1,3]       [2] => [1,2,3]     [4]  [1] => [1,4]             [5] [2] => [2,5]  [6] [4] => [4,6]

                                                                [1,2,3]   [4,1] => [1,1,2,3,4]                                    [2,5] [4,6] => [2,4,5,6]

                                                                 [1,1,2,3,4]   [2,4,5,6] => [1,1,2,3,4,2,4,5,6]

Hence we get sorted array : [1,1,2,2,3,3,4,4,5,6]

Time Complexity:

Here we are dividing the array into two halves => O(log n)
Merging also takes place for n elements => O(n)

Hence the Time Complexity => O(n log n) ~ O(n log_2 n)

Space Complexity:

Only Merge part takes place by storing in temporary array => O(n)
"""


def MergeSort(array, low, high):
    if low >= high:
        return

    mid = (low + high) // 2
    MergeSort(array, low, mid)
    MergeSort(array, mid + 1, high)
    Merge(array, low, mid, high)


def Merge(array, low, mid, high):
    temp = []
    left, right = low, mid + 1

    while left <= mid and right <= high:
        if array[left] <= array[right]:
            temp.append(array[left])
            left += 1

        else:
            temp.append(array[right])
            right += 1

    while left <= mid:
        temp.append(array[left])
        left += 1

    while right <= high:
        temp.append(array[right])
        right += 1

    for i in range(low, high + 1):
        array[i] = temp[i - low]

    return array


array = [3, 1, 2, 4, 1, 5, 2, 6, 4]
MergeSort(array, 0, len(array) - 1)

print("Sorted Array : ", array)
