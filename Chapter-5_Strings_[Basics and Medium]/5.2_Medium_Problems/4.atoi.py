"""
"String to Integer (atoi)"

=>Implement atoi which converts a string to an integer.
"""


def atoi(s):
    s = s.lstrip()
    if not s:
        return 0

    sign, res, i = 1, 0, 0
    if s[0] == "-" or s[0] == "+":
        sign = -1 if s[0] == "-" else 1
        i += 1

    while i < len(s) and s[i].isdigit():
        res = res * 10 + int(s[i])
        i += 1

    res *= sign

    if res < -(2**31):
        return -(2**31)
    elif res > 2**31 - 1:
        return 2**31 - 1
    else:
        return res


print(atoi("42"))
print(atoi("   -42"))
print(atoi("4193 with words"))
print(atoi("words and 987"))
print(atoi("-91283472332"))
