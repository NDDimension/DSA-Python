"""
424. Longest Repeating Character Replacement (LeetCode)

You are given a string `s` and an integer `k`. You can choose any character of the string and
change it to any other uppercase English character. You can perform this operation at most `k` times.

Return the length of the longest substring containing the same letter you can get after performing
the above operations.

Args:
-------
s : str
    The input string consisting of only uppercase English letters.
k : int
    The maximum number of character replacements allowed.

Returns:
--------
int
    The length of the longest substring with repeating characters after at most k replacements.

Example:
--------
>>> characterReplacement("ABAB", 2)
4
# Replace two 'B's with 'A's or two 'A's with 'B's to get "AAAA" or "BBBB".

>>> characterReplacement("AABABBA", 1)
4
# Replace the last 'B' with 'A' to get "AABAAA".

Optimal Approach:
-----------------
Use the sliding window technique to maintain a window with at most `k` characters that are
different from the most frequent character in the window.

At each step:
  - Track the count of the most frequent character in the current window.
  - If the number of characters to be replaced (window size - max frequency) > k,
    shrink the window from the left.

Time Complexity: O(n), where n is the length of the string.
Space Complexity: O(1), since the character set is fixed (only 26 uppercase letters).
"""

"""Brute Force
TC : O(n^2)
SC : O(26)"""


def LRCR(s, k):
    n = len(s)
    maxlen = 0

    for i in range(n):
        count = {}
        maxfreq = 0
        for j in range(i, n):
            count[s[j]] = count.get(s[j], 0) + 1
            maxfreq = max(maxfreq, count[s[j]])

            if (j - i + 1) - maxfreq <= k:
                maxlen = max(maxlen, j - i + 1)

    return maxlen


LRCR("ABAB", 2)

"""Optimal Approach
TC : O(n)
SC : O(26)"""


from collections import defaultdict


def LRCR(s, k):
    freq = defaultdict(int)
    left = 0
    maxlen = 0
    maxfreq = 0

    for right in range(len(s)):
        freq[s[right]] += 1
        maxfreq = max(maxfreq, freq[s[right]])

        if (right - left + 1) - maxfreq > k:
            freq[s[left]] -= 1
            left += 1

        maxlen = max(maxlen, right - left + 1)

    return maxlen


LRCR("ABAB", 2)
