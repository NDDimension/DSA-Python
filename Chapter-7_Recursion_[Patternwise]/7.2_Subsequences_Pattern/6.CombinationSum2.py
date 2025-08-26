"""
"Combination Sum 2"

=> Given candidates we need to find all unique combinations where these candidates sum up to target.
    but no duplicate pairs and each number from candidates can only be used once.

=> Example :

candidates = [10, 1 , 2 , 7 , 6 , 1 , 5]
target = 8

O/P => [1,1,6] , [1,2,5] , [1,7] , [2,6]

Time Complexity : O(2^n * k)
Space Complexity : O(k * x)
"""


def findCombination2(idx, candidates, target, ans, ds):
    if target == 0:
        ans.append(ds.copy())
        return

    for i in range(idx, len(candidates)):
        # skipping duplicates
        if i > idx and candidates[i] == candidates[i - 1]:
            continue

        if candidates[i] > target:
            break  # no point to continue

        ds.append(candidates[i])
        findCombination2(i + 1, candidates, target - candidates[i], ans, ds)
        ds.pop()


candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
candidates.sort()  # imp to skip duplicates
ans = []
findCombination2(0, candidates, target, ans, [])
print(ans)
