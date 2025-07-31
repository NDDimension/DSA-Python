"""
"Longest Palindromic Substring"

=> Given a string s, return the longest palindromic substring in s.
"""


def longestPalindrome(s):
    start, maxl = 0, 1
    for i in range(1, len(s)):
        l, r = i - 1, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > maxl:
                maxl = r - l + 1
                start = l
            l -= 1
            r += 1

        l, r = i - 1, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > maxl:
                maxl = r - l + 1
                start = l
            l -= 1

    return s[start : start + maxl]


print(longestPalindrome("babad"))
