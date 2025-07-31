"""
Part of Multiple Recursion.

Fibonnaci Time Complexity => O(2^n)

"""


def Fibonacci(n):
    if n <= 1:
        return n
    return Fibonacci(n - 1) + Fibonacci(n - 2)


Fibonacci(1)
