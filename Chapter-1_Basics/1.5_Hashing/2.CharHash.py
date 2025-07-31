from collections import Counter

string = input("Enter a string: ")
freq = Counter(string.lower())

print(f"String => '{string}'")
for ch in freq:
    print(f"{ch} => {freq[ch]} times")
