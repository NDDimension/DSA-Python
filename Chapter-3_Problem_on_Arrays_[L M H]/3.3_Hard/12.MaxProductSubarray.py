"""
"Maximum Product given By Subarray"

=> Given an array we need to find the max product possible
    by any subarray.
"""

"""
=> Brute Force:
    - Generate all the subarrays and find it .
    
=> Time Complexity : O(n^3)
=> Space Complexity : O(1)    
"""


def maxProduct(arr):
    n = len(arr)
    maxi = float("-inf")

    for i in range(n):
        for j in range(i + 1, n):
            product = 1
            for k in range(i, j + 1):
                product *= arr[k]
            maxi = max(maxi, product)
    return maxi


arr = [2, 3, -2, 4]
print(maxProduct(arr))

"""
=> Better Approach:
    - using two loops only.
    
=> Time Complexity : O(n^2)
=> Space Complexity : O(1)    
"""


def maxProductBetter(arr):
    n = len(arr)
    maxi = float("-inf")

    for i in range(n):
        product = 1
        for j in range(i, n):
            product *= arr[j]
            maxi = max(maxi, product)
    return maxi


arr = [2, 3, -2, 4]
print(maxProductBetter(arr))

"""
=> Optimal Approach:
    - using the prefix and suffix observation

=> Time Complexity : O(n)
=> Space Complexity : O(1)    
"""


def maxProductOptimal(arr):
    n = len(arr)
    prefix = 1
    suffix = 1
    maxi = float("-inf")

    for i in range(n):
        if prefix == 0:
            prefix = 1
        if suffix == 0:
            suffix = 1

        prefix *= arr[i]
        suffix *= arr[n - i - 1]
        maxi = max(maxi, max(prefix, suffix))
    return maxi


arr = [2, 3, -2, 4]
print(maxProductOptimal(arr))


"""
=> Generate with elements
def maxProduct(arr):
    n = len(arr)
    max_product = float("-inf")
    result_subarray = []

    for i in range(n):
        product = 1
        temp = []
        for j in range(i, n):  # Fix: start from i, not i+1
            product *= arr[j]
            temp.append(arr[j])
            if product > max_product:
                max_product = product
                result_subarray = temp[:]  # Make a copy

    return max_product, result_subarray


# Example usage
arr = [2, 3, -2, 4]
product, subarray = maxProduct(arr)
print("Max product:", product)
print("Subarray with max product:", subarray)
"""
