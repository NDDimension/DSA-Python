"""
"Infix to Postfix"

Convert an infix expression to a postfix (Reverse Polish Notation) expression.

This function uses the Shunting Yard algorithm to handle operator precedence and parentheses.
It supports basic arithmetic operators: +, -, *, /, and ^ (exponentiation).

Parameters:
    expression (str): Infix expression with operands and operators, e.g., "A + B * (C - D)".

Returns:
    str: Postfix expression with space-separated tokens.

Example:
    >>> infix_to_postfix("A + B * (C - D)")
    'A B C D - * +'

Operator Precedence Table:
    +----------+------------+----------------+
    | Operator | Precedence | Associativity  |
    +----------+------------+----------------+
    |   ^      |     3      |   Right        |
    |  * /     |     2      |   Left         |
    |  + -     |     1      |   Left         |
    +----------+------------+----------------+

Step-by-Step Conversion (for "A + B * ( C - D )"):


    +------+--------+--------------------+------------------------+-------------------------------+
    |Step  | Token  | Stack              | Output                | Action                        |
    +------+--------+--------------------+------------------------+-------------------------------+
    | 1     | A      |                    | A                      | Operand → Add to output       |
    | 2    | +      | +                  | A                      | Operator → Push to stack      |
    | 3    | B      | +                  | A B                    | Operand → Add to output       |
    | 4    | *      | + *                | A B                    | Higher precedence → Push      |
    | 5    | (      | + * (              | A B                    | Left parenthesis → Push       |
    | 6    | C      | + * (              | A B C                  | Operand → Add to output       |
    | 7    | -      | + * ( -            | A B C                  | Operator → Push to stack      |
    | 8    | D      | + * ( -            | A B C D                | Operand → Add to output       |
    | 9    | )      | + *                | A B C D -              | Pop until ( and discard (     |
    | 10   | End    |                    | A B C D - * +          | Pop remaining operators       |
    +------+--------+--------------------+------------------------+-------------------------------+

Final Postfix:
    A B C D - * +
"""

# TC : O(N) + O(N)
# SC : O(N) + O(N)


def priority(op):
    if op == "^":
        return 3
    elif op in ("*", "/"):
        return 2
    elif op in ("+", "-"):
        return 1
    else:
        return 0


def infixToPostfix(s):
    stack = []
    ans = ""
    i = 0

    while i < len(s):
        ch = s[i]

        # If operand, add to output
        if ch.isalnum():
            ans += ch

        # If '(', push to stack
        elif ch == "(":
            stack.append(ch)

        # If ')', pop until '('
        elif ch == ")":
            while stack and stack[-1] != "(":
                ans += stack.pop()
            if stack and stack[-1] == "(":
                stack.pop()  # discard '('

        # Operator
        else:
            while stack and priority(ch) <= priority(stack[-1]):
                ans += stack.pop()
            stack.append(ch)

        i += 1

    # Pop remaining operators
    while stack:
        ans += stack.pop()

    return ans


infixToPostfix("A+B*(C-D)")
