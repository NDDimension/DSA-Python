"""
"Sum of Beauty of All Substrings"

=> Given a string s, return the sum of beauty ( max frequency char - min frequency char) of all substring
"""


def beautySum(s: str) -> int:
    n = len(s)
    total_beauty = 0
    max_len = 100  # adjustable limit for substring length

    for i in range(n):
        freq = [0] * 26
        for j in range(i, min(i + max_len, n)):
            idx = ord(s[j]) - ord("a")
            freq[idx] += 1

            max_f = max(freq)
            min_f = min(f for f in freq if f > 0)
            total_beauty += max_f - min_f

    return total_beauty
