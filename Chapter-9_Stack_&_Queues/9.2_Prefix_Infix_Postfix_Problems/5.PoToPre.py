"""
Convert a postfix (Reverse Polish Notation) expression to a prefix (Polish Notation) expression.

This function evaluates a postfix expression and reconstructs its equivalent prefix form.
It uses a stack to hold intermediate prefix sub-expressions while scanning the input from left to right.
Supports standard arithmetic operators: +, -, *, /, and ^.

Parameters:
    expression (str): A postfix expression, e.g., "A B C D - * +".
                      Tokens (operands and operators) should be space-separated.

Returns:
    str: The equivalent prefix expression as a string.

Example:
    >>> postfix_to_prefix("A B C D - * +")
    '+ A * B - C D'

Operator Precedence Table:
    +----------+------------+----------------+
    | Operator | Precedence | Associativity  |
    +----------+------------+----------------+
    |   ^      |     3      |   Right        |
    |  * /     |     2      |   Left         |
    |  + -     |     1      |   Left         |
    +----------+------------+----------------+

Step-by-Step Conversion (for "A B C D - * +"):

    +------+---------+----------------------------------+------------------------------+
    | Step | Token   | Stack                           | Action                       |
    +------+---------+----------------------------------+------------------------------+
    | 1    | A       | ['A']                           | Push operand                 |
    | 2    | B       | ['A', 'B']                      | Push operand                 |
    | 3    | C       | ['A', 'B', 'C']                 | Push operand                 |
    | 4    | D       | ['A', 'B', 'C', 'D']            | Push operand                 |
    | 5    | -       | ['A', 'B', '- C D']             | Pop 2, form '- C D', push    |
    | 6    | *       | ['A', '* B - C D']              | Pop 2, form '* B - C D', push|
    | 7    | +       | ['+ A * B - C D']               | Pop 2, form '+ A * B - C D'  |
    +------+---------+----------------------------------+------------------------------+

Final Prefix:
    + A * B - C D
"""


# TC & SC : O(N)
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


def postfix_to_prefix(s):
    i = 0
    st = []
    while i < len(s):
        ch = s[i]
        if ch == " ":  # Skip spaces
            i += 1
            continue

        if is_operand(ch):
            st.append(ch)
        else:
            if len(st) < 2:  # Error checking
                raise ValueError("Invalid postfix expression")
            operand1 = st.pop()
            operand2 = st.pop()
            st.append(ch + operand2 + operand1)  # operator + op2 + op1
        i += 1

    if len(st) != 1:  # Final validation
        raise ValueError("Invalid postfix expression")

    return st[-1]
