"""
"Balanced Parenthesis"

Problem Statement: Check Balanced Parentheses. Given string str containing just the characters '(', ')', '{', '}', '[' and ']',
                                check if the input string is valid and return true if the string is balanced otherwise return false.

Note: string str is valid if:

    - Open brackets must be closed by the same type of brackets.
    - Open brackets must be closed in the correct order.

Example 1:

Input: str = “( )[ { } ( ) ]”

Output: True

Explanation: As every open bracket has its corresponding
close bracket. Match parentheses are in correct order
hence they are balanced.

TC : O(n)
SC : O(n)

"""


def BalancedParenthesis(s):
    stack = []
    for i in s:
        if i == "(" or i == "[" or i == "{":
            stack.append(i)

        else:
            if not stack:
                return False
            ch = stack.pop()
            if (
                (i == ")" and ch == "(")
                or (i == "]" and ch == "[")
                or (i == "}" and ch == "{")
            ):
                continue
            else:
                return False
    return not stack


if BalancedParenthesis("()[{}()]"):
    print("True")
else:
    print("False")
