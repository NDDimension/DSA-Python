"""
Convert a postfix (Reverse Polish Notation) expression to an infix expression.

This function evaluates a postfix expression and reconstructs its equivalent infix form.
It uses a stack to keep track of operands and builds sub-expressions as it processes operators.

Parameters:
    expression (str): A string representing a postfix expression, e.g., "A B C D - * +".
                      Operands and operators should be space-separated if multi-character.

Returns:
    str: The corresponding infix expression with appropriate parentheses.

Example:
    >>> postfixToInfix("A B C D - * +")
    '(A + (B * (C - D)))'

Operator Precedence Table:
    +----------+------------+----------------+
    | Operator | Precedence | Associativity  |
    +----------+------------+----------------+
    |   ^      |     3      |   Right        |
    |  * /     |     2      |   Left         |
    |  + -     |     1      |   Left         |
    +----------+------------+----------------+

Step-by-Step Conversion (for "A B C D - * +"):

    +------+---------+----------------------------+----------------------------+
    | Step | Token   | Stack                     | Action                     |
    +------+---------+----------------------------+----------------------------+
    | 1    | A       | ['A']                      | Push operand               |
    | 2    | B       | ['A', 'B']                 | Push operand               |
    | 3    | C       | ['A', 'B', 'C']            | Push operand               |
    | 4    | D       | ['A', 'B', 'C', 'D']       | Push operand               |
    | 5    | -       | ['A', 'B', '(C - D)']      | Pop 2, form '(C - D)'      |
    | 6    | *       | ['A', '(B * (C - D))']     | Pop 2, form 'B * (...)'    |
    | 7    | +       | ['(A + (B * (C - D)))']    | Pop 2, form 'A + (...)'    |
    +------+---------+----------------------------+----------------------------+

Final Infix:
    (A + (B * (C - D)))
"""


# TC : O(n) + O(n)
# SC : O(n)
def priority(op):
    if op == "^":
        return 3
    elif op in ("*", "/"):
        return 2
    elif op in ("+", "-"):
        return 1
    else:
        return 0


def is_operand(ch):
    return ch.isalnum()


def postfix_to_infix(s):
    st = []

    # Handle both spaced and unspaced expressions
    if " " in s:
        tokens = s.split()
    else:
        tokens = list(s)  # Split into individual characters

    for token in tokens:
        if is_operand(token):
            st.append(token)
        else:
            if len(st) < 2:
                raise ValueError("Invalid postfix expression")

            op1 = st.pop()
            op2 = st.pop()

            # Add parentheses based on operator precedence
            # This is a simplified version - you might want to expand this
            expr = f"({op2}{token}{op1})"
            st.append(expr)

    if len(st) != 1:
        raise ValueError("Invalid postfix expression")

    return st[0]


# Test cases
print(postfix_to_infix("AB+"))  # Output: (A+B)
print(postfix_to_infix("AB+C*"))  # Output: ((A+B)*C)
print(postfix_to_infix("ABC*+"))  # Output: (A+(B*C))
