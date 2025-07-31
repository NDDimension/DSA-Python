"""
"Median of Two sorted Arrays"

=> Given to sorted array merge them and find its median
"""

# Naive Approach


def Median(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    i, j = 0, 0
    arr3 = []

    while i < n and j < m:
        if arr1[i] < arr2[j]:
            arr3.append(arr1[i])
            i += 1

        else:
            arr3.append(arr2[j])
            j += 1

    while i < n:
        arr3.append(arr1[i])
        i += 1

    while j < m:
        arr3.append(arr2[j])
        j += 1

    a = len(arr3)

    if a % 2 == 1:
        return arr3[a // 2]

    else:
        return (arr3[a // 2] + arr3[a // 2 - 1]) / 2


arr1 = [1, 3, 4, 7, 10, 12]
arr2 = [2, 3, 6, 15]

print(Median(arr1, arr2))

# Better Approach


def median(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)

    n = n1 + n2
    i, j = 0, 0

    ind2 = n / 2
    ind1 = ind2 - 1

    count = 0

    ind1el, ind2el = -1, -1

    while i < n1 and j < n2:
        if arr1[i] < arr2[j]:
            if count == ind1:
                ind1el = arr1[i]

            if count == ind2:
                ind2el = arr1[j]

            count += 1
            i += 1

        else:
            if count == ind1:
                ind1el = arr2[j]

            if count == ind2:
                ind2el = arr2[j]

            count += 1
            j += 1

    while i < n1:
        if count == ind1:
            ind1el = arr1[i]
        if count == ind2:
            ind2el = arr1[i]
        count += 1
        i += 1

    while j < n2:
        if count == ind1:
            ind1el = arr2[j]
        if count == ind2:
            ind2el = arr2[j]
        count += 1
        j += 1

    if n % 2 == 1:
        return float(ind2el)

    return float(ind1el + ind2el) / 2


arr1 = [1, 3, 4, 7, 10, 12]
arr2 = [2, 3, 6, 15]

print(median(arr1, arr2))

# Optimal Binary Search
# TC : O(min(logn , logm))


def optimalBinaryMedian(a, b):
    n1, n2 = len(a), len(b)
    if n1 > n2:
        return optimalBinaryMedian(b, a)

    n = n1 + n2
    left = (n1 + n2 + 1) // 2
    low, high = 0, n1

    while low <= high:
        mid1 = (low + high) // 2
        mid2 = left - mid1

        l1, l2 = float("-inf"), float("-inf")
        r1, r2 = float("inf"), float("inf")

        if mid1 < n1:
            r1 = a[mid1]
        if mid2 < n2:
            r2 = b[mid2]

        if mid1 - 1 >= 0:
            l1 = a[mid1 - 1]
        if mid2 - 1 >= 0:
            l2 = b[mid2 - 1]

        if l1 <= r2 and l2 <= r1:
            if n % 2 == 1:
                return max(l1, l2)

            return (float(max(l1, l2)) + float(min(r1, r2))) / 2.0

        elif l1 > r2:
            high = mid1 - 1

        else:
            low = mid1 + 1

    return 0


a = [1, 3, 4, 7, 10, 12]
b = [2, 3, 6, 15]

print(optimalBinaryMedian(a, b))
