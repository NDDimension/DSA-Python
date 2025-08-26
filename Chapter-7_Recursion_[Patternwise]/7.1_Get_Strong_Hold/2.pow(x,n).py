"""
"Power (x , n)"

=> We will be given with X = integer , n = Power we need to return X^n
"""

# Brute Force
# Time Complexity : O(n)
# Space Complexity : O(1)
"""
Iterate and multiply the X with X n times.
"""


def Brute_Power(x, n):
    ans = 1.0
    for i in range(n):
        ans *= x

    return ans


Brute_Power(2, 4)

# Better Approach
# Time Complexity : O(logn)
# Space Complexity : O(1)
"""
Using Binary Exponentiation 
Keep on iterating until nn is greater than zero, 
now if nn is an odd power then multiply x with ans ans reduce nn by 1. 
Else multiply x with itself and divide nn by two.

Now after the entire binary exponentiation is complete 
and nn becomes zero, check if n is a negative value we 
know the answer will be 1 by and.
"""


def Power_Optimal(x, n):
    ans = 1.0
    num = n
    if num < 0:
        num *= -1

    while num:
        if num % 2:
            ans *= x
            num -= 1

        else:
            x *= x
            num //= 2

    if n < 0:
        ans = 1.0 / ans
    return ans


Power_Optimal(2, 10)
