"""
Hand of Straights

Alice has a hand of `hand.length` cards, each with an integer value.
She wants to rearrange the cards into groups of size `groupSize`, where
each group consists of `groupSize` consecutive cards.

Return True if she can rearrange the cards in this way. Otherwise, return False.

Parameters
----------
hand : List[int]
    A list of integers representing the cards in hand.

groupSize : int
    The required size of each group of consecutive cards.

Returns
-------
bool
    True if the hand can be rearranged into groups of consecutive cards of length `groupSize`.

Examples
--------
>>> sol = Solution()
>>> sol.isNStraightHand([1,2,3,6,2,3,4,7,8], 3)
True
>>> sol.isNStraightHand([1,2,3,4,5], 4)
False
>>> sol.isNStraightHand([1,2,3,4,5,6], 2)
True

Constraints
-----------
- 1 <= hand.length <= 10^4
- 0 <= hand[i] <= 10^9
- 1 <= groupSize <= hand.length
"""

"""Brute Force
Try to divide hand into groups of size `groupSize` such that each group is a sequence of consecutive integers.

--------------------
Time Complexity: O(N^2)
Space Complexity: O(N) due to list copy or pop operations

Explanation:
------------
    - Sort the hand.
    - While there are cards left:
        - Take the smallest card.
        - Try to form a consecutive group from it.
        - If not possible, return False.

"""


def isNStraightHand(hand, groupSize):
    if len(hand) % groupSize != 0:
        return False

    hand.sort()
    while hand:
        start = hand[0]
        for i in range(groupSize):
            card = start + i
            if card not in hand:
                return False
            hand.remove(card)

    return True


isNStraightHand([1, 2, 3, 6, 2, 3, 4, 7, 8], 3)

"""Optimal Approach
----------------
Time Complexity: O(N log N), where N = len(hand)
    - Sorting the unique keys (or using a heap).
    
Space Complexity: O(N)
    - For frequency map and heap.

Explanation:
------------
    - Count frequency of each card.
    - Use a min-heap to process the smallest available card.
    - For each card, try to form a group of `groupSize` consecutive cards.
        - Decrease the count in the frequency map.
        - If any card in the sequence is missing, return False.
    - If all cards are used successfully, return True.
"""


def isNStriaghtHandOptimal(hand, groupSize):
    from collections import Counter
    import heapq

    if len(hand) % groupSize != 0:
        return False

    count = Counter(hand)
    minHeap = list(count.keys())
    heapq.heapify(minHeap)

    while minHeap:
        first = minHeap[0]
        for i in range(groupSize):
            current = first + i
            if count[current] == 0:
                return False

            count[current] -= 1
            if count[current] == 0:
                if current != minHeap[0]:
                    continue
                heapq.heappop(minHeap)

    return True


isNStriaghtHandOptimal([1, 2, 3, 6, 2, 3, 4, 7, 8], 3)
