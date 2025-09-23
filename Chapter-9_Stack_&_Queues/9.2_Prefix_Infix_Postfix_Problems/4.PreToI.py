"""
Convert a prefix (Polish Notation) expression to an infix expression.

This function evaluates a prefix expression and reconstructs its equivalent infix form.
It uses a stack to store intermediate expressions as it scans the prefix string in reverse.
Supports basic operators: +, -, *, /, and ^.

Parameters:
    expression (str): A string representing a prefix expression, e.g., "+ A * B - C D".
                      Operands and operators should be space-separated if multi-character.

Returns:
    str: The corresponding infix expression with appropriate parentheses.

Example:
    >>> prefix_to_infix("+ A * B - C D")
    '(A + (B * (C - D)))'

Operator Precedence Table:
    +----------+------------+----------------+
    | Operator | Precedence | Associativity  |
    +----------+------------+----------------+
    |   ^      |     3      |   Right        |
    |  * /     |     2      |   Left         |
    |  + -     |     1      |   Left         |
    +----------+------------+----------------+

Step-by-Step Conversion (for "+ A * B - C D"):

    +------+---------+----------------------------+-------------------------------+
    | Step | Token   | Stack                      | Action                        |
    +------+---------+----------------------------+-------------------------------+
    | 1    | D       | ['D']                      | Push operand                  |
    | 2    | C       | ['D', 'C']                 | Push operand                  |
    | 3    | -       | ['(C - D)']                | Pop 2, form '(C - D)'         |
    | 4    | B       | ['(C - D)', 'B']           | Push operand                  |
    | 5    | *       | ['(B * (C - D))']          | Pop 2, form 'B * (...)'       |
    | 6    | A       | ['(B * (C - D))', 'A']     | Push operand                  |
    | 7    | +       | ['(A + (B * (C - D)))']    | Pop 2, form 'A + (...)'       |
    +------+---------+----------------------------+-------------------------------+

Final Infix:
    (A + (B * (C - D)))
"""


# TC : O(2n)
# SC : O(n)
def priority(op):
    if op == "^":
        return 3
    elif op in ("/", "*"):
        return 2
    elif op in ("-", "+"):
        return 1
    else:
        return 0


def is_operand(ch):
    return ch.isalnum()


def prefix_to_infix(s):
    stack = []

    # Read from right to left (reverse of prefix order)
    i = len(s) - 1
    while i >= 0:
        ch = s[i]
        if ch == " ":  # Skip spaces
            i -= 1
            continue

        if is_operand(ch):
            stack.append(ch)
        else:
            # Pop two operands
            if len(stack) < 2:
                raise ValueError("Invalid prefix expression")

            operand1 = stack.pop()
            operand2 = stack.pop()

            # Form the infix expression with parentheses
            expr = f"({operand1}{ch}{operand2})"
            stack.append(expr)

        i -= 1

    if len(stack) != 1:
        raise ValueError("Invalid prefix expression")

    return stack[0]


# Test
result = prefix_to_infix("-AB")
print(result)  # Output: (A-B)
