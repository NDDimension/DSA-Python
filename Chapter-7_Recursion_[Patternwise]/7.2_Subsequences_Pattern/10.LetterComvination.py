"""
"Letter Combination of phone number"

=> Given a string containing digits from 2 to 9, return all possible letter combinations that the number could represent.
    A mapping of digits to letters is given as follows (just like a phone keypad):
    2 -> "abc"
    3 -> "def"
    4 -> "ghi"
    5 -> "jkl"
    6 -> "mno"
    7 -> "pqrs"
    8 -> "tuv"
    9 -> "wxyz"

=> Example:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
"""


def letterCombination(digits):
    if not digits:
        return []

    # Mapping
    d_to_c = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    result = []

    def backtrack(idx, path):
        if idx == len(digits):
            result.append("".join(path))
            return

        for char in d_to_c[digits[idx]]:
            # Current char
            path.append(char)

            # Explore next digit
            backtrack(idx + 1, path)

            # Backtrack and remove char
            path.pop()

    backtrack(0, [])
    return result


combination = letterCombination(digits="23")
combination
