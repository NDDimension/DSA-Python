from collections import OrderedDict

my_map = {"apple": 2, "cherry": 0, "banana": 1}
sorted_map = OrderedDict(sorted(my_map.items()))

for key, value in sorted_map.items():
    print(f"{key} -> {value}")
