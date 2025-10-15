"""
Introduction to Priority Queues Using Binary Heaps
=================================================

A priority queue retrieves the "highest-priority" item efficiently. In Python,
the idiomatic and optimal approach is to use the built-in ``heapq`` module,
which implements a binary min-heap:

- Insert (heappush): O(log n)
- Remove-min (heappop): O(log n)
- Peek (min element): O(1)
- Build-heap from list (heapify): O(n)
- Push-then-pop in one pass (heappushpop): O(log n)  [often faster than push+pop]
- Pop-then-push in one pass (heapreplace): O(log n)

Use cases
---------
- Scheduling and simulation (always run the next earliest task/event)
- Graph algorithms (e.g., Dijkstra/A*)
- Streaming "top-k" queries (get n smallest/largest items)
- Anytime you repeatedly need the smallest (or largest) priority

Optimal approach in Python
--------------------------
- Use ``heapq`` for speed and low overhead.
- For a max-heap, invert the priority (store ``-priority``) or wrap with a
  comparator object.
- Break ties with a monotonic counter to avoid comparing non-comparable items.
- Prefer ``nlargest``/``nsmallest`` for top-k queries; they're optimized.
- There is no native "decrease-key"; the common pattern is to push a new entry
  and lazily discard the old one when popped.

Basic example (min-heap, stable on ties)
----------------------------------------
Use a counter to make equal-priority items pop in insertion order and to avoid
TypeError when items are incomparable.

>>> import heapq, itertools
>>> pq = []
>>> counter = itertools.count()  # unique sequence number

# Push (priority, tiebreaker, item)
>>> heapq.heappush(pq, (2, next(counter), "task-B"))
>>> heapq.heappush(pq, (1, next(counter), "task-A"))
>>> heapq.heappush(pq, (1, next(counter), "task-C"))

# Pop in priority order; A then C (same priority, earlier tie-breaker first), then B
>>> [heapq.heappop(pq)[-1] for _ in range(3)]
['task-A', 'task-C', 'task-B']

Max-heap pattern (invert priorities)
------------------------------------
>>> import heapq, itertools
>>> pq = []
>>> c = itertools.count()
>>> def push_max(pq, priority, item):
...     heapq.heappush(pq, (-priority, next(c), item))
>>> def pop_max(pq):
...     p, _, it = heapq.heappop(pq)
...     return -p, it

>>> push_max(pq, 5, "A"); push_max(pq, 2, "B"); push_max(pq, 7, "C")
>>> [pop_max(pq)[1] for _ in range(3)]
['C', 'A', 'B']

Top-k queries
-------------
>>> import heapq
>>> data = [9, 1, 4, 7, 3, 6]
>>> heapq.nsmallest(3, data)
[1, 3, 4]
>>> heapq.nlargest(2, data)
[9, 7]

Push-then-pop in one step (heappushpop)
---------------------------------------
When you often push then immediately pop, this variant can be faster than
separate calls because it does at most one sift operation.

>>> pq = []
>>> heapq.heapify(pq)
>>> heapq.heappush(pq, (10, 0, "keep"))
>>> heapq.heappushpop(pq, (5, 1, "new"))   # new is smaller, so it pops right back out
(5, 1, 'new')
>>> pq[0]
(10, 0, 'keep')

Handling "decrease-key"
-----------------------
The heap API lacks a direct "decrease-key". The standard pattern is:
- Keep an ``entry_finder`` dict mapping item -> current heap entry
- When decreasing a key, mark the old entry as REMOVED and push a new one
- On pop, discard any entries marked REMOVED

This avoids O(n) searches and preserves O(log n) updates amortized.

Caveats and tips
----------------
- Heap order is by tuple comparison: if priorities tie, Python compares the next
  elements. Use a counter as a tie-breaker to avoid comparing the items themselves.
- Do not mutate an item's priority after it’s in the heap; push a new entry instead.
- ``heapq`` is a min-heap; use negative priorities for max-heap semantics.
- For concurrent producers/consumers, use ``queue.PriorityQueue`` (thread-safe),
  noting it has locking overhead and is slower than raw ``heapq``.

References
----------
- heapq docs: https://docs.python.org/3/library/heapq.html
- queue.PriorityQueue: https://docs.python.org/3/library/queue.html#queue.PriorityQueue
"""

"""
Introduction to Priority Queues Using Binary Heaps (Python)

This module demonstrates how to use Python's built-in 'heapq' module to implement
priority queues, including:
- A simple stable min-priority queue (MinPriorityQueue)
- A simple stable max-priority queue (MaxPriorityQueue)
- A decrease-key capable priority queue (DecreaseKeyPriorityQueue)
- Top-k helpers and snippets showing heapify, heappushpop, and heapreplace

Complexities (binary heap):
- Push (heappush): O(log n)
- Pop (heappop):  O(log n)
- Peek:           O(1)
- Build (heapify):O(n)
"""

from __future__ import annotations

import heapq
import itertools
from typing import Any, Dict, Iterable, List, Optional, Tuple


# -----------------------------------------------------------------------------
# Simple, stable min-priority queue
# -----------------------------------------------------------------------------
class MinPriorityQueue:
    """
    Stable min-priority queue using a binary heap (heapq).
    - Stability: if two items share the same priority, insertion order is preserved.
    - Items do not need to be comparable, since we use a tie-breaker counter.

    Stored heap entries are tuples: (priority, tie_breaker, item)
    """

    def __init__(self) -> None:
        self._heap: List[Tuple[float, int, Any]] = []
        self._counter = itertools.count()  # unique sequence numbers

    def push(self, priority: float, item: Any) -> None:
        """Insert an item with the given priority. O(log n)"""
        entry = (priority, next(self._counter), item)
        heapq.heappush(self._heap, entry)

    def peek(self) -> Any:
        """Return the item with the smallest priority without removing it. O(1)"""
        if not self._heap:
            raise IndexError("peek from an empty MinPriorityQueue")
        return self._heap[0][2]

    def pop(self) -> Any:
        """Remove and return the item with the smallest priority. O(log n)"""
        if not self._heap:
            raise IndexError("pop from an empty MinPriorityQueue")
        _, _, item = heapq.heappop(self._heap)
        return item

    def __len__(self) -> int:
        return len(self._heap)

    def empty(self) -> bool:
        return not self._heap


# -----------------------------------------------------------------------------
# Simple, stable max-priority queue
# -----------------------------------------------------------------------------
class MaxPriorityQueue:
    """
    Stable max-priority queue implemented by inverting priorities (store -priority).
    Stored entries: (-priority, tie_breaker, item)
    """

    def __init__(self) -> None:
        self._heap: List[Tuple[float, int, Any]] = []
        self._counter = itertools.count()

    def push(self, priority: float, item: Any) -> None:
        """Insert an item with the given (max) priority. O(log n)"""
        entry = (-priority, next(self._counter), item)
        heapq.heappush(self._heap, entry)

    def peek(self) -> Any:
        """Return the item with the largest priority without removing it. O(1)"""
        if not self._heap:
            raise IndexError("peek from an empty MaxPriorityQueue")
        return self._heap[0][2]

    def pop(self) -> Any:
        """Remove and return the item with the largest priority. O(log n)"""
        if not self._heap:
            raise IndexError("pop from an empty MaxPriorityQueue")
        _, _, item = heapq.heappop(self._heap)
        return item

    def __len__(self) -> int:
        return len(self._heap)

    def empty(self) -> bool:
        return not self._heap


# -----------------------------------------------------------------------------
# Decrease-key capable priority queue via "lazy deletion"
# -----------------------------------------------------------------------------
class DecreaseKeyPriorityQueue:
    """
    Priority queue that supports "decrease-key" (and general reprioritization)
    by pushing new entries and lazily discarding old ones.

    Approach:
    - Keep an 'entry_finder' dict: item -> entry (a list for mutability).
    - On update, mark the old entry as REMOVED and push a new entry.
    - On pop/peek, discard any REMOVED entries found at the top.

    Notes:
    - Items must be hashable (used as dict keys).
    - This queue is a min-heap by default.
    - pop() and peek() return (priority, item).

    Complexities (amortized):
    - add/update: O(log n)
    - pop:        O(log n) but may skip over removed entries
    """

    def __init__(self) -> None:
        self._heap: List[List[Any]] = []  # store [priority, tie_breaker, item]
        self._entry_finder: Dict[Any, List[Any]] = {}
        self._counter = itertools.count()
        self._REMOVED = object()  # sentinel for removed entries

    def push_or_update(self, item: Any, priority: float) -> None:
        """
        Add a new item or update its priority if it already exists. O(log n)
        """
        if item in self._entry_finder:
            # Mark the existing entry as removed
            self._remove(item)
        entry = [priority, next(self._counter), item]
        self._entry_finder[item] = entry
        heapq.heappush(self._heap, entry)

    def _remove(self, item: Any) -> None:
        """Mark an existing entry as removed. O(1)"""
        entry = self._entry_finder.pop(item, None)
        if entry is not None:
            entry[2] = self._REMOVED  # mutate the item slot

    def discard(self, item: Any) -> None:
        """
        Remove an item from the queue if present (like a cancel). O(1)
        Safe to call even if the item is absent.
        """
        self._remove(item)

    def _discard_removed_at_top(self) -> None:
        """Pop and discard any removed entries that reached the top."""
        while self._heap and self._heap[0][2] is self._REMOVED:
            heapq.heappop(self._heap)

    def peek(self) -> Tuple[float, Any]:
        """Return the (priority, item) pair with smallest priority without removing. O(1) amortized."""
        self._discard_removed_at_top()
        if not self._heap:
            raise IndexError("peek from an empty DecreaseKeyPriorityQueue")
        priority, _, item = self._heap[0]
        return priority, item

    def pop(self) -> Tuple[float, Any]:
        """Remove and return the (priority, item) with smallest priority. O(log n) amortized."""
        while self._heap:
            priority, _, item = heapq.heappop(self._heap)
            if item is not self._REMOVED:
                # Remove from entry_finder and return
                self._entry_finder.pop(item, None)
                return priority, item
        raise IndexError("pop from an empty DecreaseKeyPriorityQueue")

    def __contains__(self, item: Any) -> bool:
        """True if item currently has an active entry."""
        return item in self._entry_finder

    def __len__(self) -> int:
        """Number of active items (does not count removed tombstones)."""
        return len(self._entry_finder)

    def empty(self) -> bool:
        return len(self) == 0


# -----------------------------------------------------------------------------
# Helper functions for top-k queries
# -----------------------------------------------------------------------------
def top_k_smallest(data: Iterable[Any], k: int) -> List[Any]:
    """
    Return the k smallest items from 'data'.
    Uses heapq.nsmallest which is optimized internally.
    """
    return heapq.nsmallest(k, data)


def top_k_largest(data: Iterable[Any], k: int) -> List[Any]:
    """
    Return the k largest items from 'data'.
    Uses heapq.nlargest which is optimized internally.
    """
    return heapq.nlargest(k, data)


# -----------------------------------------------------------------------------
# Demo / Usage Examples
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    print("=== Basic heapify and heappop (min-heap over numbers) ===")
    nums = [9, 1, 4, 7, 3, 6]
    print("Original:", nums)
    heapq.heapify(nums)  # in-place, O(n)
    print("Heapified:", nums)
    popped = [heapq.heappop(nums) for _ in range(len(nums))]
    print("Popped in non-decreasing order:", popped)
    print()

    print("=== Stable MinPriorityQueue (ties keep insertion order) ===")
    mpq = MinPriorityQueue()
    mpq.push(2, "task-B")
    mpq.push(1, "task-A")
    mpq.push(1, "task-C")
    result = []
    while not mpq.empty():
        result.append(mpq.pop())
    print("Pop order:", result)  # ['task-A', 'task-C', 'task-B']
    print()

    print("=== Stable MaxPriorityQueue (invert priorities internally) ===")
    maxpq = MaxPriorityQueue()
    maxpq.push(5, "A")
    maxpq.push(2, "B")
    maxpq.push(7, "C")
    result = []
    while not maxpq.empty():
        result.append(maxpq.pop())
    print("Pop order:", result)  # ['C', 'A', 'B']
    print()

    print("=== Top-k queries ===")
    data = [9, 1, 4, 7, 3, 6]
    print("3 smallest:", top_k_smallest(data, 3))  # [1, 3, 4]
    print("2 largest:", top_k_largest(data, 2))  # [9, 7]
    print()

    print("=== heappushpop vs separate push/pop ===")
    # heappushpop does a push, then pops the smallest in one pass (often faster).
    pq = []
    heapq.heapify(pq)
    heapq.heappush(pq, 10)
    print("Heap:", pq)
    print("heappushpop with 5 returns:", heapq.heappushpop(pq, 5))
    print("Heap (5 was smaller so popped right away):", pq)
    print("heappushpop with 20 returns:", heapq.heappushpop(pq, 20))
    print("Heap (20 stayed, 10 popped):", pq)
    print()

    print("=== heapreplace (pop then push) ===")
    # heapreplace pops the smallest item and then pushes a new one (always keeps new item).
    pq = []
    for x in [3, 8, 4]:
        heapq.heappush(pq, x)
    print("Start heap:", pq)
    print("heapreplace with 5 returns (popped):", heapq.heapreplace(pq, 5))
    print("Heap now:", pq)
    print()

    print("=== DecreaseKeyPriorityQueue (update priorities) ===")
    dk = DecreaseKeyPriorityQueue()
    dk.push_or_update("task-A", 5)
    dk.push_or_update("task-B", 3)
    dk.push_or_update("task-C", 4)

    # Decrease task-A's priority (higher urgency)
    dk.push_or_update("task-A", 1)

    # Cancel task-C entirely (optional)
    dk.discard("task-C")

    order = []
    while not dk.empty():
        priority, item = dk.pop()
        order.append((priority, item))
    print("Pop order with updates/cancels:", order)  # [(1, 'task-A'), (3, 'task-B')]
    print()

    print("All demos complete.")

"""
Simple Priority Queue using a Binary Heap (min-heap)

This PriorityQueue is:
- Simple: push, peek, pop, empty, and len
- Stable on ties: equal priorities pop in insertion order
- Safe with non-comparable items: uses a tie-breaker counter

Complexities (binary heap):
- push: O(log n)
- pop:  O(log n)
- peek: O(1)

Note:
- This is a min-priority queue (smallest priority comes out first).
- For a max-priority queue, invert priorities (store -priority).
"""

import heapq
import itertools
from typing import Any, List, Tuple


class PriorityQueue:
    """
    A simple, stable min-priority queue.

    Internally stores tuples of the form: (priority, tie_breaker, item)
    - tie_breaker ensures a consistent order for equal priorities and avoids
      comparing the items themselves.
    """

    def __init__(self) -> None:
        self._heap: List[Tuple[float, int, Any]] = []
        self._counter = itertools.count()  # unique increasing integers

    def push(self, priority: float, item: Any) -> None:
        """Insert an item with the given priority. O(log n)"""
        entry = (priority, next(self._counter), item)
        heapq.heappush(self._heap, entry)

    def peek(self) -> Any:
        """Return the item with the smallest priority without removing it. O(1)"""
        if not self._heap:
            raise IndexError("peek from an empty PriorityQueue")
        return self._heap[0][2]

    def pop(self) -> Any:
        """Remove and return the item with the smallest priority. O(log n)"""
        if not self._heap:
            raise IndexError("pop from an empty PriorityQueue")
        _, _, item = heapq.heappop(self._heap)
        return item

    def empty(self) -> bool:
        """True if the queue has no items."""
        return not self._heap

    def __len__(self) -> int:
        """Number of items in the queue."""
        return len(self._heap)


# Demo usage
if __name__ == "__main__":
    pq = PriorityQueue()
    pq.push(2, "task-B")
    pq.push(1, "task-A")
    pq.push(1, "task-C")

    print("Next item (peek):", pq.peek())  # -> task-A

    order = []
    while not pq.empty():
        order.append(pq.pop())

    print("Pop order:", order)  # -> ['task-A', 'task-C', 'task-B']

    # Max-heap variant (simple trick: invert the priority)
    print("\nMax-heap demo (using negative priorities):")
    max_pq = PriorityQueue()
    max_pq.push(-5, "A")  # store -priority
    max_pq.push(-2, "B")
    max_pq.push(-7, "C")
    print([max_pq.pop() for _ in range(len(max_pq))])  # -> ['C', 'A', 'B']
