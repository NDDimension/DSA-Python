from collections import Counter

n = int(input("Enter the size of the array: "))
array = list(map(int, input(f"Enter {n} elements separated by space : ").split()))

hash_map = Counter(array)

max_freq = max(hash_map.values())
min_freq = min(hash_map.values())

print("Array =>", array)
print("Hash Map =>", dict(hash_map))

# Elements with max frequency
max_freq_elements = [key for key, val in hash_map.items() if val == max_freq]
# Elements with min frequency
min_freq_elements = [key for key, val in hash_map.items() if val == min_freq]

q = int(input("Enter the number of queries: "))
q_array = list(map(int, input(f"Enter {q} queries separated by space : ").split()))

for query in q_array:
    if query in hash_map:
        print(f"Number {query} appears {hash_map[query]} times")
    else:
        print(f"Number {query} does not appear in the array")

print(
    f"\nMax Frequency: {max_freq} (Element(s): {', '.join(map(str, max_freq_elements))})"
)
print(
    f"Min Frequency: {min_freq} (Element(s): {', '.join(map(str, min_freq_elements))})"
)
