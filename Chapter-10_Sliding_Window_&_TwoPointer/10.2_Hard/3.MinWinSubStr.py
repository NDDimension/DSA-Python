"""
Minimum Window Substring

Given two strings `s` and `t` of lengths `m` and `n` respectively,
return the minimum window substring of `s` such that every character
in `t` (including duplicates) is included in the window.
If there is no such substring, return the empty string "".

The result must have the smallest possible length.
If there are multiple such substrings, return the one that appears first.

Parameters
----------
s : str
    The source string in which to search for the window.
t : str
    The target string whose characters need to be included in the window.

Returns
-------
str
    The smallest substring of `s` that contains all characters of `t`.
    If no such substring exists, return an empty string.

Constraints
----------
- `1 <= s.length, t.length <= 10^5`
- `s` and `t` consist of uppercase and lowercase English letters.

Optimal Approach
----------------
Use a sliding window approach with two pointers (left and right)
to expand and contract the window as needed. Use a hashmap to keep
track of character counts in `t` and compare it with the current
window's character frequency.

Time Complexity: O(m + n)
Space Complexity: O(n)

Example
-------
>>> sol = Solution()
>>> sol.minWindow("ADOBECODEBANC", "ABC")
'BANC'
"""

"""Brute Force
TC : O(m * n)
SC : O(n)
"""


def func(s, t):
    n, m = len(s), len(t)
    minlen = float("inf")
    sidx = -1

    from collections import Counter

    for i in range(n):
        freq = Counter(t)
        cnt = 0
        for j in range(i, n):
            if s[j] in freq:
                freq[s[j]] -= 1
                if freq[s[j]] >= 0:
                    cnt += 1

            if cnt == m:
                if j - i + 1 < minlen:
                    minlen = j - i + 1
                    sidx = i
                break

    if sidx == -1:
        return ""
    return s[sidx : sidx + minlen]


func("ADOBECODEBANC", "ABC")

"""Optimal Approach
TC : O(m + n)
SC : O(n)
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter, defaultdict

        if not t or not s:
            return ""

        dict_t = Counter(t)
        required = len(dict_t)

        # Left and Right pointer
        l, r = 0, 0

        # formed: how many unique characters in t are present in the current window in desired count
        # window_counts: frequency of characters in current window
        window_counts = defaultdict(int)
        formed = 0

        # (window length, left, right)
        ans = float("inf"), None, None

        while r < len(s):
            character = s[r]
            window_counts[character] += 1

            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1

            while l <= r and formed == required:
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                window_counts[s[l]] -= 1
                if s[l] in dict_t and window_counts[s[l]] < dict_t[s[l]]:
                    formed -= 1
                l += 1

            r += 1

        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]


obj = Solution()
obj.minWindow("ADOBECODEBANC", "ABC")
