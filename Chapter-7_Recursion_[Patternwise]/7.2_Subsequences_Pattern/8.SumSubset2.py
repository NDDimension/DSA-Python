"""
"Subset Sum 2"

=> Given an integer array containing duplicates , return the all possible subsets ; but not duplicate subsets.

=> Example:

arr = [1 , 2 , 2]

O/P => [] , [1] , [1 , 2] , [1 , 2 , 2] , [2] , [2 , 2]

Time Complexity : O(2^n * n)
Space Complexity : O(2^n) x O(k) + O(n)
"""


def subsetSum2(arr):
    arr.sort()
    ans = []

    def helper(idx, path):
        ans.append(path[:])  # appending copyy of current subset

        for i in range(idx, len(arr)):
            # skip duplicates at same recursive depth
            if i > idx and arr[i] == arr[i - 1]:
                continue

            path.append(arr[i])
            helper(i + 1, path)
            path.pop()

    helper(0, [])
    return ans


arr = [1, 2, 2]
subset = subsetSum2(arr)
for ss in subset:
    print(ss)
print()
