"""
"A to I -> atoi()"

=> Here we are given with a "string" and we need to convert it into "integer" i.e.
    "1234" -> 1234.

=> Ignore the white spaces ,  read sign and display in output , remove leading 0s and lastly rounding.
"""

# Approach
# Time Complexity : O(n)
# Space Complexity : O(n)
"""
We will be taking each character -> turning into digit * 10 + next number 
"""


def atoi(string):
    # Removing leading/trailing white spaces
    string = string.strip()

    if not string:
        return 0

    sign = 1
    if string[0] == "-":
        sign = -1
        string = string[1:]

    elif string[0] == "+":
        string = string[1:]

    def helper(idx, res):
        if idx == len(string):
            return res

        char = string[idx]
        if not char.isdigit():
            return res

        digit = int(char)
        res = res * 10 + digit

        return helper(idx + 1, res)

    result = sign * helper(0, 0)

    # Clamp to 32-bit signed integer range
    INT_MIN, INT_MAX = -(2**31), 2**31 - 1
    return max(min(result, INT_MAX), INT_MIN)


atoi("1234")
