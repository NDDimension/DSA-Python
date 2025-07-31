"""
"Largest Odd number in String"

=> Given a string num, return the largest odd number in the string or substring.
"""


def largestOddNumber(num):
    n = len(num)
    for i in range(n - 1, -1, -1):
        if int(num[i]) % 2 != 0:
            return num[: i + 1]
    return ""


num = "3579"
print(largestOddNumber(num))
