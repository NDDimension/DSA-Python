"""
"Generate all Binary String using Recursion"

=> We are given with value of n and we need to generate all possible binary strings
    for it.

=> Example:
n = 3 -> 2^3 - 1 = 8 - 1 = 7 possibilties ( from 000 -> 111 )
"""

# Simple Approach
# Time Complexity : O(2^n)
# Space Complexity : O(n)
"""
Generated all combination until a base condition matched.
"""


def generateAllBinary(n, current):
    if len(current) == n:
        print(current)
        return

    generateAllBinary(n, current + "0")
    generateAllBinary(n, current + "1")


generateAllBinary(3, "")
