"""
Minimum Window Subsequence

Given strings S and T, find the minimum contiguous substring W of S,
so that T is a subsequence of W.

If there is no such window in S that covers all characters in T, return the empty string "".
If there are multiple such minimum-length windows, return the one with the left-most starting index.

Optimal Approach:
- Use two pointers and dynamic programming.
- Forward pass: For each position in S, try to match T from left to right.
- When a complete match of T is found, do a backward pass to find the start of the minimum window.
- Keep track of the smallest window found during the iterations.

Time Complexity: O(n * m), where n = len(S) and m = len(T)
Space Complexity: O(1) (if you optimize carefully, otherwise O(n) for DP arrays)

Args:
    S (str): The string in which to find the window subsequence.
    T (str): The target subsequence to find.

Returns:
    str: The minimum window in S that contains T as a subsequence.

Example:
    >>> minWindow("abcdebdde", "bde")
    "bcde"
"""


def minWindow(S, T):
    n, m = len(S), len(T)
    start = 0
    min_len = float("inf")

    # dp[i] stores the start index in S where a subsequence matching T[:j] ends at i
    dp = [-1] * n

    for j in range(m):
        prev = -1
        new_dp = [-1] * n
        for i in range(n):
            if S[i] == T[j]:
                if j == 0:
                    new_dp[i] = i
                else:
                    new_dp[i] = prev
            if dp[i] != -1:
                prev = dp[i]
        dp = new_dp

    for i in range(n):
        if dp[i] != -1:
            length = i - dp[i] + 1
            if length < min_len:
                start = dp[i]
                min_len = length

    return "" if min_len == float("inf") else S[start : start + min_len]


minWindow("abcdebdde", "bde")

"""
    Brute Force Approach:
    - Try every possible substring of S.
    - For each substring, check if T is a subsequence.
    - Track the minimum length substring which contains T as a subsequence.
    
    Time Complexity: O(n^2 * m), where n = len(S), m = len(T).
    This is because there are O(n^2) substrings and checking subsequence takes O(m).
    
    Space Complexity: O(1)
    
    Args:
        S (str): The string to search within.
        T (str): The target subsequence.
        
    Returns:
        str: The minimum window in S containing T as subsequence, or "" if none.
        
    Example:
        >>> minWindow("abcdebdde", "bde")
        "bcde"
    """


def minWin(S, T):
    def is_subsequence(sub, target):
        tidx = 0
        for char in sub:
            if tidx < len(target) and char == target[tidx]:
                tidx += 1
            if tidx == len(target):
                return True
        return False

    n = len(S)
    minlen = float("inf")
    res = ""

    for start in range(n):
        for end in range(start, n):
            substring = S[start : end + 1]
            if is_subsequence(substring, T):
                if (end - start + 1) < minlen:
                    minlen = end - start + 1
                    res = substring
                break

    return res


minWin("abcdebdde", "bde")
