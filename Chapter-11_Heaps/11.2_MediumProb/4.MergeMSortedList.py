"""
Merge k (or m) sorted linked lists into one sorted list.

**Problem statement (LeetCode style)**
--------------------------------------
You are given an array ``lists`` of *k* linked-lists, each of which is sorted
in non‑decreasing order.

Merge all the linked-lists into one sorted linked-list and return its head.

**Constraints**
---------------
* ``1 <= k <= 10⁴`` – number of input lists.
* The total number of nodes across all lists is ``N`` where ``0 <= N <= 10⁵``.
* ``-10⁴ <= node.val <= 10⁴``.
* Each individual list is already sorted in non‑decreasing order.

**Optimal approach**
--------------------
The most efficient generic solution runs in ``O(N log k)`` time and ``O(k)`` extra
space:

1. Insert the first node of every non‑empty list into a **min‑heap** keyed by
   ``node.val``.
2. Repeatedly pop the smallest node from the heap, attach it to the result
   list, and push the popped node’s ``next`` (if any) back into the heap.
3. Continue until the heap is empty – at that point all nodes have been
   extracted in sorted order.

The heap never holds more than ``k`` elements, giving the ``log k`` factor
for each of the ``N`` extractions/insertions.

**Complexity analysis**
-----------------------
*Time*   : ``O(N log k)`` – each of the ``N`` nodes is pushed and popped once,
each operation costing ``log k``.
*Space*  : ``O(k)`` – the heap stores at most one node from each list.

**Examples**
------------
>>> # Helper to build a linked list from a Python list
>>> def build(lst):
...     dummy = ListNode()
...     cur = dummy
...     for v in lst:
...         cur.next = ListNode(v)
...         cur = cur.next
...     return dummy.next
>>> # Helper to convert a linked list back to a Python list
>>> def to_list(node):
...     out = []
...     while node:
...         out.append(node.val)
...         node = node.next
...     return out
>>> lists = [build([1,4,5]), build([1,3,4]), build([2,6])]
>>> merged_head = Solution().mergeKLists(lists)
>>> to_list(merged_head)
[1, 1, 2, 3, 4, 4, 5, 6]

>>> # Edge case – all lists are empty
>>> Solution().mergeKLists([None, None])
None

>>> # Single list – should be returned unchanged (but as a new reference)
>>> single = build([0])
>>> merged = Solution().mergeKLists([single])
>>> to_list(merged)
[0]
"""


# Definition for singly‑linked list.
class ListNode:
    """
    A node of a singly‑linked list.

    Attributes
    ----------
    val : int
        The value stored in the node.
    next : ListNode | None
        Reference to the next node in the list (or ``None`` if this is the tail).
    """

    __slots__ = ("val", "next")

    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"ListNode({self.val})"


class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        """
        Merge ``k`` sorted linked lists.

        Parameters
        ----------
        lists : list[ListNode | None]
            A list containing the head of each sorted linked list. Empty lists are
            represented by ``None``.

        Returns
        -------
        ListNode | None
            The head of the merged sorted linked list, or ``None`` if all input
            lists are empty.
        """
        import heapq

        # The heap will store tuples of the form (node value, unique id, node)
        # The unique id (``id(node)``) breaks ties when values are equal,
        # preventing ``TypeError`` from comparing ListNode objects directly.
        heap: list[tuple[int, int, ListNode]] = []

        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, id(node), node))

        dummy = ListNode()  # Dummy head to simplify list construction
        tail = dummy

        while heap:
            val, _, node = heapq.heappop(heap)
            tail.next = node
            tail = tail.next
            if node.next:
                heapq.heappush(heap, (node.next.val, id(node.next), node.next))

        return dummy.next
