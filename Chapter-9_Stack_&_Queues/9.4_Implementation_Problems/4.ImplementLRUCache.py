"""
LRU Cache

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

    LRUCache(int capacity)
        - Initialize the LRU cache with positive size capacity.

    int get(int key)
        - Return the value of the key if the key exists, otherwise return -1.

    void put(int key, int value)
        - Update the value of the key if the key exists.
        - Otherwise, add the key-value pair to the cache.
        - If the number of keys exceeds the capacity from this operation,
          evict the least recently used key.

Your implementation should run in O(1) average time complexity for both get and put.

Constraints:
- 1 <= capacity <= 3000
- 0 <= key <= 10^4
- 0 <= value <= 10^5
- At most 2 * 10^5 calls will be made to get and put.

Optimal Approach:
- Use a combination of:
    1. A hash map to store key → node mappings for O(1) access.
    2. A doubly linked list (or OrderedDict) to track LRU order.
       - Most recently used items at the front.
       - Least recently used items at the back.
- On every get/put, move the item to the front.
- If capacity exceeded, remove item from the back.

Example:

Input:
    ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    [[2], [1,1], [2,2], [1], [3,3], [2], [4,4], [1], [3], [4]]

Output:
    [None, None, None, 1, None, -1, None, -1, 3, 4]

Explanation:
    LRUCache cache = new LRUCache(2)
    cache.put(1, 1)         # cache = {1=1}
    cache.put(2, 2)         # cache = {1=1, 2=2}
    cache.get(1)            # returns 1, cache = {2=2, 1=1}
    cache.put(3, 3)         # evicts key 2, cache = {1=1, 3=3}
    cache.get(2)            # returns -1 (not found)
    cache.put(4, 4)         # evicts key 1, cache = {3=3, 4=4}
    cache.get(1)            # returns -1 (not found)
    cache.get(3)            # returns 3
    cache.get(4)            # returns 4
"""

from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return -1

        # mv key to end ( recently used )
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            # rem old val
            self.cache.move_to_end(key)

        self.cache[key] = value
        if len(self.cache) > self.capacity:
            # pop first item (least recently used)
            self.cache.popitem(last=False)


# Instantiate the cache with capacity 2
lru = LRUCache(2)

# Perform operations
lru.put(1, 1)  # Cache = {1=1}
lru.put(2, 2)  # Cache = {1=1, 2=2}
print(lru.get(1))  # Output: 1, Cache = {2=2, 1=1}
lru.put(3, 3)  # Evicts key 2, Cache = {1=1, 3=3}
print(lru.get(2))  # Output: -1 (not found)
lru.put(4, 4)  # Evicts key 1, Cache = {3=3, 4=4}
print(lru.get(1))  # Output: -1 (not found)
print(lru.get(3))  # Output: 3
print(lru.get(4))  # Output: 4

"""Doubly Linked List Approach"""


class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    """
    LRU Cache implemented with custom Doubly Linked List + HashMap for O(1) access and updates.
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> Node

        # Dummy head and tail nodes
        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

    # Internal helper: remove a node from the list
    def _remove(self, node: Node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    # Internal helper: add node right after head (MRU position)
    def _add_to_front(self, node: Node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        # Move to front
        self._remove(node)
        self._add_to_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update existing node and move to front
            self._remove(self.cache[key])

        new_node = Node(key, value)
        self._add_to_front(new_node)
        self.cache[key] = new_node

        if len(self.cache) > self.capacity:
            # Remove LRU from back (before tail)
            lru_node = self.tail.prev
            self._remove(lru_node)
            del self.cache[lru_node.key]


lru = LRUCache(2)
lru.put(1, 1)
lru.put(2, 2)
print(lru.get(1))  # 1
lru.put(3, 3)  # Evicts key 2
print(lru.get(2))  # -1
lru.put(4, 4)  # Evicts key 1
print(lru.get(1))  # -1
print(lru.get(3))  # 3
print(lru.get(4))  # 4
