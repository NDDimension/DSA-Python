"""
"Sieve of Eratosthenes"

=> Given a Number N , print all Primes till N
"""

"""
Naive Approach

-> Checking primes in the given range and printing them.

TC : O(n x sqrt(n))
SC : O(1)
"""


def isPrime(N):
    if N <= 1:
        return False
    for i in range(2, int(N**0.5) + 1):
        if N % i == 0:
            return False
    return True


def Sieve_of_Eratosthenes(n):
    for i in range(2, n + 1):
        if isPrime(i):
            print(i, end=" ")


Sieve_of_Eratosthenes(100)

"""
Sieve of Eratosthenes 
Here we take a prime array of size N+1 and mark everyone as 1
and as we iterate we take a number check for prime and mark 
its multiples as 0 leaving only the primes.

TC : O(n log (log n))
"""


def SOE(n):
    prime = [1] * (n + 1)
    prime[0] = prime[1] = 0  # 0 and 1 are not primes

    for i in range(2, int(n**0.5) + 1):
        if prime[i] == 1:
            for j in range(2 * i, n + 1, i):
                prime[j] = 0

    # Return the list of prime numbers
    return [i for i in range(n + 1) if prime[i] == 1]


SOE(100)
