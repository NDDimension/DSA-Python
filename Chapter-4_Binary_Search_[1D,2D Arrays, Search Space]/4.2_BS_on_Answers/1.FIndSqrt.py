"""
"Find the Square Root of Given Number N"

=> Given N we need to return the sqrt of it if its perfect square else nearest possible sqrt's floor value.
"""

"""
=> Naive Approach : using Linear Search

TC : O(n)
SC : O(1)
"""


def sqrt(n):
    ans = 1
    for i in range(1, n + 1):
        if i * i <= n:
            ans = i

        else:
            break
    return ans


n = 28
print(sqrt(n))

"""
=> Using Binary Search

TC : O(logn)
SC : O(1)
"""


def sqrt_BS(n):
    low = 1
    high = n
    ans = 1

    while low <= high:
        mid = (low + high) // 2

        if mid * mid <= n:
            ans = mid
            low = mid + 1

        else:
            high = mid - 1

    return ans


n = 28
print(sqrt_BS(n))
