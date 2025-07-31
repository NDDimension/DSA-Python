"""
"Remove the Outermost Paranthesis"

=> Given a string we need to extract the content by removing the outermost paranthesis.
"""


def removeOuterParentheses(S):
    stack = []
    depth = 0

    for char in S:
        if char == "(":
            if depth > 0:
                stack.append(char)
            depth += 1
        else:
            depth -= 1
            if depth > 0:
                stack.append(char)

    return "".join(stack)


print(removeOuterParentheses("(()())(())"))
