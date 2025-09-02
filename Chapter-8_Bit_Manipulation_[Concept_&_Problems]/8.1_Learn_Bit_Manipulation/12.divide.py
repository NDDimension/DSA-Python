"""
"Divide two Integers without using * , / , // , and % operator"

=> We are given with Dividend , Divisor in range [-2^31 , 2^31 - 1] return the integer value after dividing.

TC : O(log_2 N)^2
SC : O(1)
"""


def divideNos(dividend, divisor):
    INT_MAX = 2**31 - 1
    INT_MIN = -(2**31)

    # Edge case: overflow
    if dividend == INT_MIN and divisor == -1:
        return INT_MAX

    # Determine the sign
    sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

    n = abs(dividend)
    d = abs(divisor)
    ans = 0

    while n >= d:
        count = 0
        while n >= (d << (count + 1)):
            count += 1

        ans += 1 << count
        n -= d << count

    result = sign * ans

    return result


divideNos(22, 3)
