"""
                                                    "Selection Sort"
=> Select Minimum + Swap Positions

[13, 46 , 25, 52, 20, 9] -> Min = 9

Place it at first index => [9 , 46, 25, 52 ,20 , 13] -> Swap 9's position with 13
Other as it is . This is step 1 done .

Now new array is interpreted as => [9](sorted)  [46, 25, 52 , 20 , 13]
[46, 25, 52 , 20 , 13] => Apply the same => Min = 13

13 to position 1 of new array => [9] [13, 25, 52, 20, 46] => 13 and 46 swapped
Step 2 done .

Now new array => [9, 13] sorted [25 , 52 , 20 , 46] and same logic applied

Time complexity :

As we go inside the loops it runs for "n" then "n-1" then "n-2" like wise
~ n + n-1 + n-2...1 => Summation of the first "n" natural numbers
= (n * (n + 1)) / 2
= (n^2 + n) / 2

"~ O(n^2) [Worst / Average / Best Case]"
"""

size = int(input("Size of the array: "))
array = list(map(int, input("Enter elements : ").split()))
print("Original => ", array)


# Selection Sort
def SelectionSort(array):
    for i in range(size - 1):
        mini = i
        for j in range(i + 1, size):
            if array[j] < array[mini]:
                mini = j
        array[i], array[mini] = array[mini], array[i]


print("Sorted => ", SelectionSort(array))
