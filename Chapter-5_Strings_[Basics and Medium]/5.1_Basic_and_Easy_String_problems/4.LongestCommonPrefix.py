"""
"Longest Common Prefix"

=> Given an array of words we need to return the longest common prefix.

=> Example

Input: ["flower","flow","flight"]
Output: "fl"
"""


def longestCommonPrefix(strs):
    strs = sorted(strs)
    first = strs[0]
    last = strs[-1]
    i = 0
    while i < len(first) and i < len(last) and first[i] == last[i]:
        i += 1
    return first[:i]


strs = ["flower", "flow", "flight"]
print(longestCommonPrefix(strs))
