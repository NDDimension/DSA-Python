"""
Given Array size = 5
Array => [1, 3 , 2 , 1 , 3]
Queries => 5 -> how many 1 , 4 , 2 , 3 & 12 ?

"""

from collections import Counter

# Intial Stage
n = int(input("Enter the size of the array: "))
array = list(map(int, input(f"Enter {n} ele sep by space : ").split()))

# Precompute => Creating HashArray
hash_map = Counter(array)

# Query Stage
query = int(input("Enter the number of queries: "))
q_array = list(map(int, input(f"Enter {query} q sep by space : ").split()))

# Hashing

print("Array =>", array)

print("Hash Map =>", hash_map)

for q in q_array:
    print(f"{q} appears {hash_map[q]} times")
