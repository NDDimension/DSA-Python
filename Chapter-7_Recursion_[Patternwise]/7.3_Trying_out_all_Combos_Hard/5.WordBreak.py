"""
"Word Break"

=> Given a string s and a dictionary of words wordDict,
    return True if s can be segmented into a space-separated
    sequence of one or more dictionary words.

=> Example:

s = "leetcode"
wordDict = ["leet", "code"]

Output: True
# Because "leet" + "code" are in wordDict

"""
# Recursive
# Time Complexity : O(2^n)
# Space Complexity : O(n)


def word_break(s, wordDict):
    # if string empty : Done
    if s == "":
        return True

    # Try every prefix
    for i in range(1, len(s) + 1):
        prefix = s[:i]
        suffix = s[i:]

        # if prefix in dict , recursively check suffix
        if prefix in wordDict:
            if word_break(suffix, wordDict):
                return True

    return False


word_break("leetcode", ["leet", "code"])

# Dynamic Programming
# Time Complexity : O(n^2)
# Space Complexity : O(n)


def word_break(s, wordDict):
    memo = {}

    def can_break(s):
        if s == "":
            return True

        if s in memo:
            return memo[s]

        for i in range(1, len(s) + 1):
            prefix = s[:i]
            suffix = s[i:]
            if prefix in wordDict and can_break(suffix):
                memo[s] = True
                return True

        memo[s] = False
        return False

    return can_break(s)
