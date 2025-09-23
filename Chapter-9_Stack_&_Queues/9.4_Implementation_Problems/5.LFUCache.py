"""
Design and implement a data structure for a Least Frequently Used (LFU) cache.

Implement the LFUCache class:

    LFUCache(int capacity) - Initializes the object with the capacity of the cache.
    int get(int key)       - Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
    void put(int key, int value) - Updates or inserts the value if the key is not already present.
                                   When the cache reaches its capacity, it should invalidate and remove
                                   the least frequently used key. If there is a tie, remove the least
                                   recently used key among them.

Your implementation should be optimized such that both `get` and `put` operations run in **O(1)** average time.

Approach:
----------
We use a combination of three data structures:

1. `key_to_val_freq`: Dictionary mapping key -> (value, freq)
2. `freq_to_keys`: Dictionary mapping freq -> OrderedDict of keys (preserves insertion order for LRU)
3. `min_freq`: Tracks the minimum frequency in the cache (helps in eviction)

On `get(key)`:
- If key not found, return -1.
- Otherwise, update frequency of the key, move it to the next frequency bucket, update min_freq accordingly, and return the value.

On `put(key, value)`:
- If capacity is 0, do nothing.
- If key exists, update the value and frequency.
- If key doesn't exist:
    - If at capacity, evict the LRU key in the lowest frequency bucket.
    - Insert the new key with freq = 1.
    - Update `min_freq` to 1.

Time Complexity:
----------------
- `get` : O(1)
- `put` : O(1)

Space Complexity:
-----------------
- O(capacity)

Example:
---------
    cache = LFUCache(2)
    cache.put(1, 1)         # cache = {1=1}
    cache.put(2, 2)         # cache = {1=1, 2=2}
    cache.get(1)            # returns 1, freq of key 1 becomes 2
    cache.put(3, 3)         # evicts key 2 (freq=1, LRU), cache = {1=1, 3=3}
    cache.get(2)            # returns -1 (not found)
    cache.get(3)            # returns 3, freq of key 3 becomes 2
    cache.put(4, 4)         # evicts key 1 (freq=2, LRU), cache = {4=4, 3=3}
    cache.get(1)            # returns -1
    cache.get(3)            # returns 3
    cache.get(4)            # returns 4
"""

from collections import defaultdict, OrderedDict


class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.key_to_val_freq = {}  # key -> {val , freq}
        self.freq_to_keys = defaultdict(OrderedDict)  # freq -> {key : None}
        self.min_freq = 0

    def _update_freq(self, key):
        val, freq = self.key_to_val_freq[key]

        # rm from old list of freq
        del self.freq_to_keys[freq][key]
        if not self.freq_to_keys[freq]:
            del self.freq_to_keys[freq]
            if freq == self.min_freq:
                self.min_freq += 1

        # Add to new freq list
        self.freq_to_keys[freq + 1][key] = None
        self.key_to_val_freq[key] = (val, freq + 1)

    def get(self, key):
        if key not in self.key_to_val_freq:
            return -1
        self._update_freq(key)
        return self.key_to_val_freq[key][0]

    def put(self, key, value):
        if self.capacity == 0:
            return

        if key in self.key_to_val_freq:
            self.key_to_val_freq[key] = (value, self.key_to_val_freq[key][1])
            self._update_freq(key)
        else:
            if len(self.key_to_val_freq) >= self.capacity:
                # Evict LFU and LRU key
                evict_key, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
                del self.key_to_val_freq[evict_key]

            self.key_to_val_freq[key] = (value, 1)
            self.freq_to_keys[1][key] = None
            self.min_freq = 1


cache = LFUCache(2)
cache.put(1, 1)  # cache = {1=1}
cache.put(2, 2)  # cache = {1=1, 2=2}
print(cache.get(1))  # returns 1
cache.put(3, 3)  # evicts key 2
print(cache.get(2))  # returns -1 (not found)
print(cache.get(3))  # returns 3
cache.put(4, 4)  # evicts key 1
print(cache.get(1))  # returns -1
print(cache.get(3))  # returns 3
print(cache.get(4))
