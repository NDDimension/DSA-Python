"""
"Prime Factorization of a Number (Queries) using Sieve"

=> We are given with Query Q having a value and
    that many numbers are given to us and we need
    to return the Prime Factorization of each number in Query Q.

=> Q = 2 {12 , 16}

Ans : 12 -> 2 , 2 , 3
         16 -> 2 ,2 ,2 ,2

"""


def PrimeFactorization(n):
    lst = []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            while n % i == 0:
                lst.append(i)
                n //= i

    if n > 1:
        lst.append(n)

    return lst


# TC : O(q) x O(sqrt(n))


def lst(queries):
    for i in range(0, len(queries)):
        lists = PrimeFactorization(queries[i])
        print(lists)


lst([12, 16])

"""
Now here we can not optimize the O(q) but with other O(sqrt(n)) 
we can optimize it with the help of SPF ( Smallest Prime Factor)

TC : O(n log (log n)) + O(q x log_2 n)
SC : O(n)
"""


def compute_spf(limit=10**5):
    spf = [i for i in range(limit + 1)]  # Initialize spf[i] = i

    for i in range(2, int(limit**0.5) + 1):
        if spf[i] == i:
            for j in range(i * i, limit + 1, i):
                if spf[j] == j:
                    spf[j] = i
    return spf


def factorize_queries(queries):
    spf = compute_spf(max(queries))  # Precompute up to max query

    for n in queries:
        print(f"Prime factorization of {n}:", end=" ")
        while n != 1:
            print(spf[n], end=" ")
            n //= spf[n]
        print()  # New line after each query


factorize_queries([12, 16])
