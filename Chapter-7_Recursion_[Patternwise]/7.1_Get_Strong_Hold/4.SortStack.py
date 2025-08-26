"""
"Sort the Stack using Recursion"

=> We are given with an unsorted stack and we need to sort it using recursion.
"""

# Approach
# Time Complexity : O(n^2)
# Space Complexity : O(n)
"""
Using two function one to sort and one to insert into stack by performing comparison.
"""


def insert_Stack(stack, top):
    if not stack or top > stack[-1]:
        stack.append(top)
        return

    temp = stack.pop()
    insert_Stack(stack, top)
    stack.append(temp)


def sort_Stack(stack):
    if stack:
        top = stack.pop()
        sort_Stack(stack)
        insert_Stack(stack, top)

    return stack


sort_Stack([5, 4, 3, 2, 1])
