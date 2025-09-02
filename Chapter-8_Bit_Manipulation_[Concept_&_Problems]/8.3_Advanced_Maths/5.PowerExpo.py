"""
"Power Exponentiation"

=> Given two values X and N we need to return the pow(x , n) = x ^ n
"""


# TC: O(log_2 |n|)
def PowerExpo(x, n):
    ans = 1
    is_negative = n < 0
    n = abs(n)

    while n > 0:
        if n % 2 == 1:
            ans *= x
            n -= 1
        else:
            x *= x
            n //= 2

    return 1 / ans if is_negative else ans


PowerExpo(5, -2)
PowerExpo(3, 9)

pow(5, -2)
