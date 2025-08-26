"""
"Count Good Numbers"

=> We need to return the good numbers for given n by doing modulo 10^9 + 7.

=> A good number is a number where the even indices are even numbers and odd indices are having prime numbers.
"""

# Approach
# Time Complexity : O(Logn)
# Space Complexity : O(1)
"""
We will first find the even and odd positions , then we use pow( 5 , even , mod) for even and 
pow(4 , odd , mod) .

5 -> as 5 choices 0 , 2 , 4 , 6 , 8
4 -> as 4 choices 2 , 3 , 5 , 7
in terms of position.

Returning the result by even * odd % mod
"""


def goodNumbers(n):
    mod = pow(10, 9) + 7

    even = (n + 1) // 2
    odd = n // 2

    even_part = pow(5, even, mod)
    odd_part = pow(4, odd, mod)

    return (even_part * odd_part) % mod


goodNumbers(1)
