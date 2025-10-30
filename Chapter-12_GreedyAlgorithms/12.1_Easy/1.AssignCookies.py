"""
Assign Cookies - Greedy Algorithm Problem

Problem:
    Assume you are an awesome parent and want to give your children some cookies.
    But, you should give each child at most one cookie.

    Each child `i` has a greed factor `g[i]`, which is the minimum size of a cookie
    that the child will be content with; and each cookie `j` has a size `s[j]`.

    You aim to maximize the number of your content children and can assign at most
    one cookie to each child.

Parameters:
    g (List[int]): A list of greed factors of the children.
    s (List[int]): A list of cookie sizes.

Returns:
    int: The maximum number of children that can be content with the available cookies.

Optimal Approach:
    - Sort the greed factors and the cookie sizes in non-decreasing order.
    - Use two pointers: one for the children (`i`), one for the cookies (`j`).
    - For each child, find the smallest available cookie that satisfies their greed.
    - If such a cookie exists, assign it and move to the next child.
    - Continue this process until you've gone through either all children or all cookies.

Time Complexity:
    O(n log n + m log m) where n = len(g), m = len(s), due to the sorting step.

Example:
    >>> findContentChildren([1, 2, 3], [1, 1])
    1

    >>> findContentChildren([1, 2], [1, 2, 3])
    2
"""


def AssignCookies(greed, size):
    n, m = len(greed), len(size)
    l, r = 0, 0
    greed, size = sorted(greed), sorted(size)
    while l < m and r < n:
        if greed[r] <= size[l]:
            r += 1
        l += 1
    return r


AssignCookies([1, 2, 3], [1, 1])


def findContentChildren(g: list[int], s: list[int]) -> int:
    g.sort()
    s.sort()
    i = j = 0
    while i < len(g) and j < len(s):
        if s[j] >= g[i]:
            i += 1  # child is content
        j += 1  # move to the next cookie
    return i
