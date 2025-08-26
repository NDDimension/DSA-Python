"""
"Combination Sum"

=> Given candidates we need to find by choosing whom and how many times we can achieve our target.

Example : candidates = [2,3,6,7]    target = 7      Solution : [[2,2,3], [7]]

Time Complexity : O(2^t x k)
Space Complexity : O(k * x)
"""


def findCombination(idx, candidates, target, ans, ds):
    if idx == len(candidates):
        if target == 0:
            ans.append(ds.copy())  # Important fix!
        return

    # Pick the element if it's ≤ target
    if candidates[idx] <= target:
        ds.append(candidates[idx])
        findCombination(idx, candidates, target - candidates[idx], ans, ds)
        ds.pop()

    # Not pick the element
    findCombination(idx + 1, candidates, target, ans, ds)


candidates = [2, 3, 6, 7]
target = 7
ans = []
findCombination(0, candidates, target, ans, [])
print(ans)
