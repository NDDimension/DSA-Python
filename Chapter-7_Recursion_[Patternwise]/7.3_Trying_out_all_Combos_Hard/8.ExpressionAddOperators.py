"""
"Expression Add Operators"

=> Given a string num that contains only digits and an integer target,
    return all possibilities to insert the binary operators '+', '-', and/or '*'
    between the digits of num so that the resultant expression evaluates to the target value.

Note that operands in the returned expressions should not contain leading zeros.
Note that a number can contain multiple digits.

=> Example :

Input: num = "123", target = 6

Output: ["1*2*3","1+2+3"]

Explanation: Both "1*2*3" and "1+2+3" evaluate to 6.

=> Time Complexity : O(4^n)
=> Space Complexity : O(4^n * n)
"""


def add_operators(num, target):
    result = []

    def backtrack(path, pos, eval_val, prev):
        if pos == len(num):
            if eval_val == target:
                result.append(path)
            return

        for i in range(pos, len(num)):
            # Skip numbers with leading zeros
            if i != pos and num[pos] == "0":
                break

            curr_str = num[pos : i + 1]
            curr = int(curr_str)

            if pos == 0:
                # First number, no operator
                backtrack(curr_str, i + 1, curr, curr)
            else:
                # Addition
                backtrack(path + "+" + curr_str, i + 1, eval_val + curr, curr)
                # Subtraction
                backtrack(path + "-" + curr_str, i + 1, eval_val - curr, -curr)
                # Multiplication
                backtrack(
                    path + "*" + curr_str,
                    i + 1,
                    eval_val - prev + (prev * curr),
                    prev * curr,
                )

    backtrack("", 0, 0, 0)
    return result


# Example usage:
num = "123"
target = 6
output = add_operators(num, target)
print("Valid expressions that evaluate to", target, "are:")
for expr in output:
    print(expr)
