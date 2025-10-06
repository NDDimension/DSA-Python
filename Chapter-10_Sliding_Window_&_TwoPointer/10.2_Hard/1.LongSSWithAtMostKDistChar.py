"""
"Longest Sub String with At Most K Distinct Characters"

Given a string s and an integer k, return the length of the longest substring
that contains at most k distinct characters.

Parameters:
s (str): The input string consisting of ASCII characters.
k (int): The maximum number of distinct characters allowed in the substring.

Returns:
int: The length of the longest valid substring.

Constraints:
- 0 <= len(s) <= 10^5
- 0 <= k <= 26

Example 1:
>>> length_of_longest_substring_k_distinct("eceba", 2)
3
Explanation: The substring is "ece" with 2 distinct characters.

Example 2:
>>> length_of_longest_substring_k_distinct("aa", 1)
2
Explanation: The substring is "aa" with 1 distinct character.

Example 3:
>>> length_of_longest_substring_k_distinct("a", 0)
0
Explanation: No characters allowed, so result is 0.

Optimal Approach:
Use the sliding window technique with two pointers and a hash map to track character frequency.
Expand the right pointer to include characters until there are more than k distinct characters.
Shrink from the left until we have at most k distinct characters.
Track the maximum window size during the process.

Time Complexity: O(n), where n is the length of the string.
Space Complexity: O(k), for storing at most k characters in the map.
"""

"""Brute Force
TC : O(n^2)
SC : O(256)
"""
from collections import defaultdict


def LSSWAMKDC(s, k):
    maxlen = 0
    for i in range(len(s)):
        mapp = defaultdict(int)
        for j in range(i, len(s)):
            mapp[s[j]] += 1
            if len(mapp) <= k:
                maxlen = max(maxlen, j - i + 1)
            else:
                break
    return maxlen


LSSWAMKDC("aa", 1)

"""Optimal Approach"""


def funct(s, k):
    if k == 0 or not s:
        return 0

    maxlen = 0
    l = 0
    c_map = defaultdict(int)

    for r in range(len(s)):
        c_map[s[r]] += 1

        while len(c_map) > k:
            c_map[s[l]] -= 1
            if c_map[s[l]] == 0:
                del c_map[s[l]]
            l += 1

        maxlen = max(maxlen, r - l + 1)
    return maxlen


funct("aa", 1)
