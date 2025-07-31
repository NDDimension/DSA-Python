"""
"Longest Consecutive sequence in the Array"

=> Given = [ 102,100,101,1,2,3,4]

Sequence => 1,2,3,4 len =4 , 100,101,102 len = 3 like wise

=> Brute Force :

    - Iterate taking one element at a time
    - Do linear search for the next term for forming sequence

=> Time Complexity : O(n^2)
=> Space Complexity : O(1)

=> Better Approach :

    - use last term and sorting to find out the longest sequence

=> Time Complexity : O(nlogn) + O(n)
=> Space Complexity : O(1)


=> Optimal Approach :

    - Use set and check element's previous partner
    - if present we dont iterate for it
    - if not then we do need to find

=> Time Complexity : O(3n)
=> Space Complexity : O(n)

"""


def ls(a, num):
    n = len(a)
    for i in range(n):
        if a[i] == num:
            return True

    return False


def longest_seq_brute(arr):
    longest = 1

    n = len(arr)
    for i in range(n):
        x = arr[i]
        count = 1

        while ls(arr, x + 1):
            x += 1
            count += 1

        longest = max(longest, count)

    return longest


def longest_seq_better(arr):
    longest = 1
    count_curr = 0
    last_smaller = float("-inf")

    arr = sorted(arr)
    for i in range(len(arr)):
        if arr[i] - 1 == last_smaller:
            count_curr += 1
            last_smaller = arr[i]

        elif arr[i] != last_smaller:
            count_curr = 1
            last_smaller = arr[i]

        longest = max(longest, count_curr)
    return longest


def longest_seq_optimal(arr):
    n = len(arr)
    if n == 0:
        return 0

    longest = 1
    st = set()

    for i in range(n):
        st.add(arr[i])

    for it in st:
        if it - 1 not in st:
            cnt = 1
            x = it
            while x + 1 in st:
                x += 1
                cnt += 1

            longest = max(longest, cnt)

    return longest


a = [100, 200, 1, 2, 3, 4]
print(longest_seq_optimal(a))
