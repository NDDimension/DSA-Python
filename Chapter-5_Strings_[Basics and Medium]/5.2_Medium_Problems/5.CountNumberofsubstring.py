from collections import defaultdict


def count_substrings_with_k_distinct(s, k):
    def at_most_k(s, k):
        count = 0
        left = 0
        freq = defaultdict(int)

        for right in range(len(s)):
            freq[s[right]] += 1
            while len(freq) > k:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1
            count += right - left + 1
        return count

    return at_most_k(s, k) - at_most_k(s, k - 1)
