"""
"Generate Parenthesis"

=> Given n we need to print the valid , well-formed parenthesis
"""

# Approach
# Time Complexity : O(4^n / sqrt(n)) ~ O(C_n) catalan number
# Space Complexity : O(C_n * 2n) + O(n)
"""
We will check for lengths of close and open with n , until they are same we keep adding the opening and closing.
At the same time first open will be entered then close , as close is compared with open to be added .
In this way we will generate and check at the same time.
"""


def generateParenthesis(n):
    result = []

    def backtrack(current, open_b, close_b):
        if len(current) == 2 * n:
            result.append(current)
            return

        if open_b < n:
            backtrack(current + "(", open_b + 1, close_b)

        if close_b < open_b:
            backtrack(current + ")", open_b, close_b + 1)

    backtrack("", 0, 0)
    return result


generateParenthesis(3)
