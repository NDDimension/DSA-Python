"""
"Maximum Depth Paranthesis"

=> Given a paranthesis string we need to find the maximum nested depth paranthesis count.
"""


def maxDepth(s):
    n = len(s)

    res, current = 0, 0
    for i in range(n):
        if s[i] == "(":
            current += 1
        elif s[i] == ")":
            current -= 1
        res = max(res, current)

    return res


s = "(1+(2*3)+((8)/4))+1"
print(maxDepth(s))
