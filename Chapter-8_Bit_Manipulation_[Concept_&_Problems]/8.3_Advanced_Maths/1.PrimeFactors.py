"""
"Prime Factors of a given Number"

=> We are given a number N and we need to return the prime numbers that divides N leaving remainder as 0.
"""

# Naive Approach
"""
We generate all the factor for N and then differentiate the primes out of it.

TC : O(N x Sqrt(N))
SC : O(Prime Factors of N)
"""


def isPrime(N):
    if N <= 1:
        return False
    for i in range(2, int(N**0.5) + 1):
        if N % i == 0:
            return False
    return True


def PrimeFactors(N):
    lst = []
    for i in range(2, N + 1):
        if N % i == 0 and isPrime(i):
            lst.append(i)
    return lst


PrimeFactors(780)


# Approx TC : O(2 x sqrt(N) x sqrt(N))
def PrimeFactors2(N):
    lst = []
    for i in range(1, int(N**0.5) + 1):
        if N % i == 0 and isPrime(i):
            lst.append(i)
            if N / i != i and isPrime(N / i):
                lst.append(i)

    return lst


PrimeFactors2(780)


# Little Optimized by doing the prime factorization method
def PrimeFactors3(N):
    lst = []
    for i in range(2, N + 1):
        if N % i == 0:
            lst.append(i)
            while N % i == 0:
                N /= i

    return lst


PrimeFactors3(780)


# Optimized Version TC : O(sqrt(N) x log N)
def PrimeFactors4(N):
    lst = []
    for i in range(2, int(N**0.5) + 1):
        if N % i == 0:
            lst.append(i)
            while N % i == 0:
                N /= i
    if N != 1:
        lst.append(N)
    return lst


PrimeFactors4(37)
