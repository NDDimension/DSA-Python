# "Second Largest in an Array"

"""
=> Brute Force :

    -Sort
    -Find Largest
    -Iterate from back if found any number != largest
    -Its Second Largest

    -Time Complexity => O(n log n ) + O(n)
"""


def SecLargeBrute(arr):
    temp = sorted(arr)
    largest = temp[len(temp) - 1]

    for i in range(len(temp) - 2, -1, -1):
        if temp[i] != largest:
            secondLargest = temp[i]
            break

    return secondLargest


"""
=> Better  :

    -Find Largest
    -Iterate again comparing every element and it being not largest
    -Its Second Largest

    -Time Complexity => O(n) + O(n) = O(2n)
"""


def SecLargeBetter(arr):
    # To avoid all these just use max(arr)
    largest = arr[0]
    for i in range(len(arr)):
        if arr[i] > largest:
            largest = arr[i]

    secondLargest = float("-inf")
    for i in range(len(arr)):
        if arr[i] > secondLargest and arr[i] != largest:
            secondLargest = arr[i]

    return secondLargest


"""
=> Optimal :

    -Take two var largest and secondLargest as -infinity
    
    -Iterate and find largest and if on next iteration you 
      find a number larger than largest then update largest 
      and put the value of largest to second largest
      

    -Time Complexity => O(n)
"""


def SecLargeOptimal(arr):
    largest = arr[0]
    secondLargest = float("-inf")

    for i in range(len(arr)):
        if arr[i] > largest:
            secondLargest = largest
            largest = arr[i]

        elif arr[i] < largest and arr[i] > secondLargest:
            secondLargest = arr[i]

    return secondLargest


def SecSmallestOptimal(arr):
    smallest = arr[0]
    secondSmallest = float("inf")

    for i in range(len(arr)):
        if arr[i] < smallest:
            secondSmallest = smallest
            smallest = arr[i]

        elif arr[i] > smallest and arr[i] < secondSmallest:
            secondSmallest = arr[i]

    return secondSmallest


arr = [1, 2, 4, 7, 7, 5]
SecLargeOptimal(arr)
SecSmallestOptimal(arr)
