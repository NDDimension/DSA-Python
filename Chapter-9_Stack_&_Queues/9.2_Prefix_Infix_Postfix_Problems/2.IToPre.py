"""
"Infix to Prefix"
Convert an infix expression to a prefix (Polish Notation) expression.

This function converts an infix expression to its equivalent prefix form.
It handles operators: +, -, *, /, ^ and respects operator precedence and parentheses.
The algorithm is based on reversing the infix expression, applying the postfix logic, and reversing the result.

Parameters:
    expression (str): Infix expression with operands and operators, e.g., "A + B * (C - D)".

Returns:
    str: Prefix expression with operators before their operands.

Example:
    >>> infixToPrefix("A + B * (C - D)")
    '+ A * B - C D'

Operator Precedence Table:
    +----------+------------+----------------+
    | Operator | Precedence | Associativity  |
    +----------+------------+----------------+
    |   ^      |     3      |   Right        |
    |  * /     |     2      |   Left         |
    |  + -     |     1      |   Left         |
    +----------+------------+----------------+

Step-by-Step Conversion (for "A + B * ( C - D )"):

    1. Reverse infix: (becomes) "( D - C ) * B + A"
    2. Convert to postfix: "D C - B * A +"
    3. Reverse postfix: "+ A * B - C D"

Conversion Table (Postfix Logic on Reversed Infix):

    +------+--------+--------------------+------------------------+-------------------------------+
    |Step  | Token  | Stack              | Output                | Action                        |
    +------+--------+--------------------+------------------------+-------------------------------+
    | 1    | D      |                    | D                      | Operand → Add to output       |
    | 2    | -      | -                  | D                      | Operator → Push to stack      |
    | 3    | C      | -                  | D C                    | Operand → Add to output       |
    | 4    | )      | - )                | D C                    | Right paren → Push to stack   |
    | 5    | (      | -                  | D C -                  | Pop till ')' & discard ')'    |
    | 6    | *      | *                  | D C -                  | Operator → Push               |
    | 7    | B      | *                  | D C - B                | Operand → Add to output       |
    | 8    | +      | + *                | D C - B *              | Lower precedence → Pop & Push |
    | 9    | A      | +                  | D C - B * A            | Operand → Add to output       |
    | 10   | End    |                    | D C - B * A +          | Pop remaining operators       |
    +------+--------+--------------------+------------------------+-------------------------------+

Final Prefix:
    + A * B - C D
"""

# TC : O(n/2) + O(n/2) + O(2n)
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


def infixToPostfix(s):
    stack = []
    ans = ""
    for ch in s:
        if ch == " ":  # Skip spaces
            continue
        if is_operand(ch):
            ans += ch
        elif ch == "(":
            stack.append(ch)
        elif ch == ")":
            while stack and stack[-1] != "(":
                ans += stack.pop()
            if stack and stack[-1] == "(":
                stack.pop()
        else:
            while stack and priority(ch) <= priority(stack[-1]):
                ans += stack.pop()
            stack.append(ch)
    while stack:
        ans += stack.pop()
    return ans


def infixToPrefix(s):
    # Step 1: Reverse the infix expression
    s = s[::-1]

    # Step 2: Swap ( with ) and vice versa
    swapped = []
    for ch in s:
        if ch == "(":
            swapped.append(")")
        elif ch == ")":
            swapped.append("(")
        else:
            swapped.append(ch)
    s = "".join(swapped)

    # Step 3: Convert to postfix
    postfix = infixToPostfix(s)

    # Step 4: Reverse the postfix to get prefix
    prefix = postfix[::-1]

    return prefix


expr = "A + B * (C - D)"
print("Infix:  ", expr)
print("Prefix: ", infixToPrefix(expr))
