"""
Given a string `s`, find the length of the longest substring without repeating characters.

This uses the optimal sliding window approach with a hash map to track the last seen position
of each character. The window expands until a duplicate character is found, at which point
the start of the window is moved right after the last occurrence of the duplicate character.

Time Complexity: O(n), where n is the length of the string.
Space Complexity: O(min(n, m)), where m is the size of the character set (e.g., 26 for lowercase letters).

Parameters:
----------
s : str
    Input string consisting of English letters, digits, symbols, and spaces.

Returns:
-------
int
    The length of the longest substring without repeating characters.

Examples:
--------
>>> lengthOfLongestSubstring("abcabcbb")
3
# The answer is "abc", with the length of 3.

>>> lengthOfLongestSubstring("bbbbb")
1
# The answer is "b", with the length of 1.

>>> lengthOfLongestSubstring("pwwkew")
3
# The answer is "wke", with the length of 3.
# Note that the answer must be a substring, "pwke" is a subsequence and not valid.

>>> lengthOfLongestSubstring("")
0
# Empty string has length 0.
"""

"""Brute Force
TC : O(n^2)
SC : O(256)"""


def LSSWOR(s: str) -> int:
    n = len(s)
    maxlen = 0

    for i in range(n):
        seen = set()
        for j in range(i, n):
            if s[j] in seen:
                break
            seen.add(s[j])
            maxlen = max(maxlen, j - i + 1)

    return maxlen


print(LSSWOR("abcabcbb"))  # Output: 3


"""Optimal Approach
TC : O(n)
SC : O(256)"""


def LSSWOROpt(s):
    char_idx = {}
    left = 0
    maxLen = 0

    for right, char in enumerate(s):
        if char in char_idx and char_idx[char] >= left:
            left = char_idx[char] + 1
        char_idx[char] = right
        maxLen = max(maxLen, right - left + 1)

    return maxLen


LSSWOROpt("abcabcbb")
