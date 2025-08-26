"""
"Reverse Stack using Recursion"

=> Given a stack we need to reverse it using recursion
"""

# Approach
# Time Complexity : O(n^2)
# Space Complexity : O(n)
"""
Popping each element until empty , inserting from end.
"""


def insertStack(stack, top):
    if not stack:
        stack.append(top)

    else:
        temp = stack.pop()
        insertStack(stack, top)
        stack.append(temp)


def reverseStack(stack):
    if stack:
        top = stack.pop()
        reverseStack(stack)
        insertStack(stack, top)

    return stack


reverseStack([5, 4, 3, 2, 1])
