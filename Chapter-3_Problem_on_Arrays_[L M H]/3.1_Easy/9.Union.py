"""
"Union of two sorted arrays"

=> Time Complexity: O(n + m)
=> Space Complexity: O(n + m)

"Intersection of two sorted arrays"

=> Time Complexity: O(n x m)
=> Space Complexity: O(min(n, m))

=> Time Complexity: O(n + m)
=> Space Complexity: O(1)
"""


def union(arr1, arr2):
    union = list(set(arr1) | set(arr2))
    return union


def union_two_sorted(arr1, arr2):
    i, j = 0, 0
    result = []

    while i < len(arr1) and j < len(arr2):
        # Skip duplicates in arr1
        if i > 0 and arr1[i] == arr1[i - 1]:
            i += 1
            continue
        # Skip duplicates in arr2
        if j > 0 and arr2[j] == arr2[j - 1]:
            j += 1
            continue

        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            result.append(arr2[j])
            j += 1
        else:
            # Both elements are equal, add one and move both pointers
            result.append(arr1[i])
            i += 1
            j += 1

    # Add remaining elements of arr1 (skip duplicates)
    while i < len(arr1):
        if i == 0 or arr1[i] != arr1[i - 1]:
            result.append(arr1[i])
        i += 1

    # Add remaining elements of arr2 (skip duplicates)
    while j < len(arr2):
        if j == 0 or arr2[j] != arr2[j - 1]:
            result.append(arr2[j])
        j += 1

    return result


def Intersection(arr1, arr2):
    return list(set(arr1) & set(arr2))


def Intersect(arr1, arr2):
    ans = []
    visited = [0] * len(arr2)

    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] == arr2[j] and visited[j] == 0:
                ans.append(arr1[i])
                visited[j] = 1
                break

            if arr2[j] > arr1[i]:
                break

    return ans


def Inter(arr1, arr2):
    n, m = len(arr1), len(arr2)

    i, j = 0, 0
    ans = []
    while i < n and j < m:
        if arr1[i] < arr2[j]:
            i += 1

        elif arr2[j] < arr1[i]:
            j += 1

        else:
            ans.append(arr1[i])
            i += 1
            j += 1

    return ans


arr1 = [1, 3, 5, 7, 9]
arr2 = [2, 3, 5, 8, 10]
print(Inter(arr1, arr2))
