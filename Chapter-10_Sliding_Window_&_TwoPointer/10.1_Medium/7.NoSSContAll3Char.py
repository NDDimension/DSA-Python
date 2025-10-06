"""
Number of Substring Containing All Three Characters

Given a string s consisting only of characters 'a', 'b', and 'c',
return the number of substrings that contain at least one occurrence
of all these characters.

Optimal Approach:
-----------------
We use a sliding window technique. The idea is to maintain a window
[left, right] such that s[left:right+1] contains all three characters
at least once. Every time we expand the right pointer and the window
becomes valid, we can add (len(s) - right) to the result, since all
substrings starting at `left` and ending from `right` to end of string
will be valid.

Time Complexity: O(n), where n is the length of the string.
Space Complexity: O(1), constant space for character counts.

Parameters:
-----------
s : str
    A string consisting only of characters 'a', 'b', and 'c'.

Returns:
--------
int
    The number of substrings that contain at least one 'a', one 'b', and one 'c'.

Example:
--------
>>> numberOfSubstrings("abcabc")
10

Explanation:
The valid substrings are:
"abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc", "abc"
"""


def NSSCA3C(stri):
    """
    Brute-force approach to count substrings containing at least one 'a', 'b', and 'c'.
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    count = 0
    n = len(stri)

    for i in range(n):
        freq = [0, 0, 0]  # for a , b , c

        for j in range(i, n):
            if stri[j] in "abc":
                freq[ord(stri[j]) - ord("a")] = 1

            if sum(freq) == 3:
                count += 1

    return count


NSSCA3C("abcabc")


"""Optimal Approach
"""


def NSSCA3C(s):
    n = len(s)
    lastSeen = [-1, -1, -1]
    count = 0

    for i in range(n):
        lastSeen[ord(s[i]) - ord("a")] = i
        if lastSeen[0] != -1 and lastSeen[1] != -1 and lastSeen[2] != -1:
            count += 1 + min(lastSeen[0], lastSeen[1], lastSeen[2])

    return count


NSSCA3C("abcabc")
