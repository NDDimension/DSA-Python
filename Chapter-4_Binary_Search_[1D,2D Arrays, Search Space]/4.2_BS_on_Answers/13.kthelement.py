"""
Kth element of two sorted arrays"

=> Given two sorted arrays we need to find the kth element.
=> TC : O(min(logn , logm))
"""


def kth_element(a, b, k):
    m = len(a)
    n = len(b)

    if m > n:
        return kth_element(b, a, k)

    left = k
    low = max(0, k - n)
    high = min(k, m)

    while low <= high:
        mid1 = (low + high) // 2
        mid2 = k - mid1

        l1, l2, r1, r2 = float("-inf"), float("-inf"), float("inf"), float("inf")
        if mid1 < m:
            r1 = a[mid1]

        if mid2 < n:
            r2 = b[mid2]

        if mid1 - 1 >= 0:
            l1 = a[mid1 - 1]

        if mid2 - 1 >= 0:
            l2 = b[mid2 - 1]

        if l1 <= r2 and l2 <= r1:
            return max(l1, l2)

        elif l1 > r2:
            high = mid1 - 1

        else:
            low = mid1 + 1

    return 0


a = [2, 3, 6, 7, 9]
b = [1, 4, 8, 10]
kth_element(a, b, 5)
