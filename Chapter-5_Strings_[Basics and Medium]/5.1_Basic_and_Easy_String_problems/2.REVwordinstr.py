"""
"Reverse the words in the String"

=> Given a string we need to reverse its order and also need to
    remove beginning or trailing spaces or space between words if more than 1.

=> Example

String = " Hello World " -> "World Hello"
"""


def reverse_words(string):
    words = string.strip().split()
    return " ".join(reversed(words))


string = " Hello World "
reverse_words(string)
