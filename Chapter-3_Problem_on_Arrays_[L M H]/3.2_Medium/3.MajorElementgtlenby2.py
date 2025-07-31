"""
"Majority Element > N/2"

array = [2,2,3,3,1,2,2]
Len = 7
7/2 = 3.5 so element greater than this times is 2 which is 4 times.
Hence return 4.

=> Brute Force :

    - Iterate through the array and count occurences.

=> Time Complexity => O(n^2)
=> Space Complexity => O(1)

=> Better Approach :

    - using Hashmap to store count of each element.

=> Time Complexity => O(n) + O(n log n)
=> Space Complexity => O(n)

=> Optimal Approach :

    - Using Moore's Voting Algorithm.
    - Pick one ele and initialize count as 0.
    - Iterate and update count if element is same as picked.
    - Decrease count if element is not same as picked.
    - if count becomes 0, pick new element and do the same

=> Time Complexity => O(n)
=> Space Complexity => O(1)

"""


def majorityElement(array):
    for i in range(len(array)):
        count = 0
        for j in range(len(array)):
            if array[i] == array[j]:
                count += 1
        if count > len(array) // 2:
            return array[i], count


def majorityElementBetter(array):
    count_dict = {}
    for num in array:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    for num, count in count_dict.items():
        if count > len(array) // 2:
            return num, count


from collections import Counter


def majorityElementCounter(array):
    count = Counter(array)

    for num, count in count.items():
        if count > len(array) // 2:
            return num, count


def majorityElementMoore(array):
    count, element = 0, None

    for i in range(len(array)):
        if count == 0:
            count = 1
            element = array[i]
        elif array[i] == element:
            count += 1
        else:
            count -= 1

    count1 = 0
    for i in range(len(array)):
        if array[i] == element:
            count1 += 1

    if count1 > len(array) // 2:
        return element

    return -1


array = [2, 2, 3, 3, 1, 2, 2]
print(majorityElementMoore(array))
