"""
"Painter's Partition Problem" / "Split array - Largest Sum / "Allocate Books"

=> Given some units to be painted and number of painter , we need to assign the painters
    to paint and complete the job.

Constraints:

    - Atleast one unit is to be assigned to the painter

return the min(max time taken by any of the painters)

TC : O((sum - max + 1) x N)
SC : O(1)
"""


def assignment(arr, k):
    var = 1
    hold = 0
    for i in range(len(arr)):
        if hold + arr[i] <= k:
            hold += arr[i]
        else:
            var += 1
            hold = arr[i]
    return var


def Painter_SplitArray(arr, k):
    low = max(arr)
    high = sum(arr)
    while low <= high:
        mid = (low + high) // 2
        if assignment(arr, mid) > k:
            low = mid + 1
        else:
            high = mid - 1
    return low


arr = [10, 20, 30, 40]
k = 2
print(Painter_SplitArray(arr, k))
