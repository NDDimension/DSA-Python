"""
Simulate the Least Recently Used (LRU) Page Replacement algorithm.

LRU (Least Recently Used) is a page replacement strategy that removes the
page that has not been used for the longest period of time when a new
page needs to be loaded into a full memory frame.

Parameters
----------
pages : list[int]
    The sequence of page references (page numbers requested by a process).
capacity : int
    The maximum number of pages that can be held in memory (i.e., number of frames).

Returns
-------
int
    The total number of page faults (times when a page had to be loaded
    because it was not already in memory).

Example
-------
>>> pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
>>> LRU(pages, 4)
6

Explanation
-----------
- Frames capacity = 4
- Page faults occur when a requested page is not in memory.
- LRU keeps track of the least recently used page and replaces it.

Simulation:
    Pages: [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
    Page Faults = 6
"""

"""
⚙️ Optimal Approach

The optimal way to simulate LRU is using:

    - A set (for quick lookup if a page is in memory)
    - A queue or OrderedDict (to track usage order)

Every time a page is accessed:

1. If it’s in memory → move it to the most recently used position.
2. If it’s not in memory → page fault occurs.

    - If memory is full → remove the least recently used page.
    - Then insert the new page.

Time Complexity:

Average: O(1) per operation using collections.OrderedDict
Total: O(n) for n page references
"""


def LRU(pages, capacity):
    from collections import OrderedDict

    memory = OrderedDict()
    pg_faults = 0

    for page in pages:
        if page not in memory:
            pg_faults += 1
            if len(memory) >= capacity:
                memory.popitem(last=False)

        else:
            memory.move_to_end(page)
        memory[page] = True

    return pg_faults


LRU([7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2], 4)
