"""
Convert a prefix (Polish Notation) expression to a postfix (Reverse Polish Notation) expression.

This function processes a prefix expression and reconstructs the equivalent postfix form.
It uses a stack to store intermediate postfix expressions while scanning the prefix expression from right to left.
Supports standard arithmetic operators: +, -, *, /, and ^.

Parameters:
    expression (str): A prefix expression, e.g., "+ A * B - C D".
                      Tokens (operands and operators) should be space-separated.

Returns:
    str: The equivalent postfix expression as a string.

Example:
    >>> prefix_to_postfix("+ A * B - C D")
    'A B C D - * +'

Operator Precedence Table:
    +----------+------------+----------------+
    | Operator | Precedence | Associativity  |
    +----------+------------+----------------+
    |   ^      |     3      |   Right        |
    |  * /     |     2      |   Left         |
    |  + -     |     1      |   Left         |
    +----------+------------+----------------+

Step-by-Step Conversion (for "+ A * B - C D"):

    +------+---------+----------------------------------+------------------------------+
    | Step | Token   | Stack                           | Action                       |
    +------+---------+----------------------------------+------------------------------+
    | 1    | D       | ['D']                           | Push operand                 |
    | 2    | C       | ['D', 'C']                      | Push operand                 |
    | 3    | -       | ['C D -']                       | Pop 2, form 'C D -'          |
    | 4    | B       | ['C D -', 'B']                  | Push operand                 |
    | 5    | *       | ['B C D - *']                   | Pop 2, form 'B (C D -) *'    |
    | 6    | A       | ['B C D - *', 'A']              | Push operand                 |
    | 7    | +       | ['A B C D - * +']               | Pop 2, form 'A (B C D - *) +'|
    +------+---------+----------------------------------+------------------------------+

Final Postfix:
    A B C D - * +
"""

# TC : O(2n)
# SC : O(n)


def is_operand(ch):
    return ch.isalnum()


def prefix_to_postfix(s):
    i = len(s) - 1  # Process from right to left
    st = []
    while i >= 0:
        ch = s[i]
        if ch == " ":  # Skip spaces
            i -= 1
            continue

        if is_operand(ch):
            st.append(ch)
        else:
            if len(st) < 2:
                raise ValueError("Invalid prefix expression")
            operand1 = st.pop()
            operand2 = st.pop()
            st.append(operand1 + operand2 + ch)  # op1 + op2 + operator
        i -= 1

    if len(st) != 1:
        raise ValueError("Invalid prefix expression")

    return st[-1]


# Test cases
print(prefix_to_postfix("+AB"))  # Output: AB+
print(prefix_to_postfix("*+ABC"))  # Output: AB+C*
print(prefix_to_postfix("-*+ABCD"))  # Output: AB+C*D-
