"""
"Give All Divisors of the Number N"
"""

"""
Naive Approach
TC : O(n)
"""


def Divisors(n):
    lst = []
    for i in range(1, n + 1):
        if n % i == 0:
            lst.append(i)

    return lst


Divisors(36)

"""
Little Optimized
TC : O(sqrt(N))
"""


def Divisors2(n):
    lst = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            lst.append(i)
            if n // i is not i:
                lst.append(n // i)

    return lst


Divisors2(36)
