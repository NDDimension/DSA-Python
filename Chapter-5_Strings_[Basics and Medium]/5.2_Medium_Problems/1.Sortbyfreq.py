"""
"Sort Characters by Frequency"

=> Given a string we need to return the string in frequency of characters by descending order.

=> Example

string = "tree"
output = "eert"
"""

from collections import Counter, defaultdict


def sort_characters_by_frequency(string):
    count = Counter(string)
    bucket = defaultdict(list)

    for char, freq in count.items():
        bucket[freq].append(char)

    res = ""
    for i in range(len(string), 0, -1):
        for c in bucket[i]:
            res += c * i

    return res


print(sort_characters_by_frequency("tree"))
