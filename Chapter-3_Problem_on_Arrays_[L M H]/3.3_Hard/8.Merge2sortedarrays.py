"""
"Merge 2 Sorted Arrays without using Extra Space"

=> Given two arrays we need to return both of them singly sorted
    without extra space.

Example => a1 = [1, 3, 5] and a2 = [2, 4, 6]

Now what we need to do is merge them but it should be sorted i.e
a1 = [1,2,3] and a2 = [4,5,6]

like this .
"""

"""
=> Brute Force:
    - using a 3rd array we store the full sorted array
    - then just place them in both arrays sorted

=> Time Complexity : O(2(n + m))
=> Space Complexity : O(n + m)    
"""


def merge(a1, a2):
    l1 = len(a1)
    l2 = len(a2)
    l, r, ind = 0, 0, 0
    a3 = [0] * (l1 + l2)

    while l < l1 and r < l2:
        if a1[l] <= a2[r]:
            a3[ind] = a1[l]
            l += 1
            ind += 1

        else:
            a3[ind] = a2[r]
            r += 1
            ind += 1

    while l < l1:
        a3[ind] = a1[l]
        l += 1
        ind += 1

    while r < l2:
        a3[ind] = a2[r]
        r += 1
        ind += 1

    for i in range(len(a3)):
        if i < l1:
            a1[i] = a3[i]
        else:
            a2[i - l1] = a3[i]

    return a1, a2


a1 = [1, 3, 5]
a2 = [2, 4, 6]

print(merge(a1, a2))

"""
=> Better Approach:
    - using two pointers one pointing max of a1 and another min of a2
    - if they are on wrong place we swap them else break and sort both
    
=> Time Complexity : O(min(n , m)) + O(nlogn) + O(mlogm)
=> Space Complexity : O(1)    
"""


def mergeBetter(a1, a2):
    l1 = len(a1)
    l2 = len(a2)
    l, r = l1 - 1, 0

    while l >= 0 and r < l2:
        if a1[l] > a2[r]:
            a1[l], a2[r] = a2[r], a1[l]
            l -= 1
            r += 1
        else:
            break

    a1.sort()
    a2.sort()

    return a1, a2


a1 = [1, 3, 5]
a2 = [2, 4, 6]

print(mergeBetter(a1, a2))

"""
=> Optimal Approach:
    - using "Gap Method" from "Shell Sort"
    - do the (n+m) / 2 and take ceiling value of that
    - its our intial gap 
    - assingn the first pointer on 0 and second gap place away
    - start comparing if either of pointer moves out of bound stop
    - do gap/2 and take  its ceiling value and repeat
    - stop when gap = 1
    
=> Time Complexity : O(log_base2(n + m)) + O(n + m)
=> Space Complexity : O(1)    
"""


def swapG(a1, a2, i1, i2):
    if a1[i1] > a2[i2]:
        a1[i1], a2[i2] = a2[i2], a1[i1]


def mergeOptimal(a1, a2):
    l1 = len(a1)
    l2 = len(a2)
    len_ = l1 + l2
    gap = (len_ // 2) + (len_ % 2)

    while gap > 0:
        l = 0
        r = l + gap
        while r < len_:
            if l < l1 and r >= l1:
                swapG(a1, a2, l, r - l1)

            elif l >= l1:
                swapG(a2, a2, l - l1, r - l1)

            else:
                swapG(a1, a1, l, r)

            l += 1
            r += 1

        if gap == 1:
            break

        gap = (gap // 2) + (gap % 2)

    return a1, a2


a1 = [1, 3, 5]
a2 = [2, 4, 6]

mergeOptimal(a1, a2)
