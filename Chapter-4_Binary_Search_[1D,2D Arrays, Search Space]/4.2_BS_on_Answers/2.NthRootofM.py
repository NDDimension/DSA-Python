"""
"Find the Nth root of M"

=> Given N and M find it :

Example :

N = 3 , M = 27 ====> (27) ^ 1/3 = 3
"""


# using Naive Linear Search
# TC : O(m log_base2 n)
# SC : O(1)
def nthRoot(n, m):
    for i in range(1, m + 1):
        if i**n == m:
            return i

        elif i**n > m:
            break

    return -1


n, m = 4, 69
print(nthRoot(n, m))

# using Optimal Binary Search
# TC : O(log_base2 m)
# SC : O(1)


def nthRoot_BS(n, m):
    low = 1
    high = m

    while low <= high:
        mid = (low + high) // 2

        if mid.__pow__(n) == m:
            return mid

        elif mid.__pow__(n) < m:
            low = mid + 1

        else:
            high = mid - 1

    return -1


n, m = 3, 99999
print(nthRoot_BS(n, m))


def power(mid, n, m):
    result = 1
    for _ in range(n):
        result *= mid
        if result > m:
            return result  # early exit
    return result


def nthRoot_BS(n, m):
    if m == 0:
        return 0
    if n == 1:
        return m

    low, high = 1, m
    while low <= high:
        mid = (low + high) // 2
        curr = power(mid, n, m)

        if curr == m:
            return mid
        elif curr < m:
            low = mid + 1
        else:
            high = mid - 1

    return -1
