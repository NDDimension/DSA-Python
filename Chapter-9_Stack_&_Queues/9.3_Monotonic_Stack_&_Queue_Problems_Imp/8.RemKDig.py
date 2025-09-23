"""
Problem: Remove K Digits

Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:
- The resulting number should not have leading zeros.
- You must remove exactly k digits.

Example 1:
    Input: num = "1432219", k = 3
    Output: "1219"
    Explanation: Remove the three digits 4, 3, and 2 to form the new number "1219".

Example 2:
    Input: num = "10200", k = 1
    Output: "200"
    Explanation: Remove the digit 1 to form the new number "200". Note that the leading zero is removed.

Example 3:
    Input: num = "10", k = 2
    Output: "0"
    Explanation: Remove all digits, resulting in the number "0".

Constraints:
- 1 <= num.length <= 100
- 1 <= k <= num.length
- num only consists of digits and does not contain leading zeros.

Approach:
    1. The problem is a stack-based greedy approach.
    2. Traverse the number from left to right. For each digit, compare it with the top of the stack:
       - If the current digit is smaller than the top of the stack, we pop the top (remove it) to make the number smaller.
       - Continue this process until you've removed k digits or the stack is in the optimal state.
    3. After traversing the number, if you haven't removed k digits, remove the remaining digits from the end.
    4. Finally, handle leading zeros and return the resulting number as a string.

Time Complexity: O(n), where n is the length of the input string (num).
Space Complexity: O(n), for the stack used during the processing.
"""


# TC : O(3n) + O(k)
# SC : O(2n)
def Rem_K_Digits(s, k):
    st = []

    # Traverse through the digits of the string
    for i in range(len(s)):
        # While we still have digits to remove and the current digit is smaller than the last one in the stack
        while st and k > 0 and (st[-1] > s[i]):
            st.pop()
            k -= 1

        st.append(s[i])

    # If there are still digits to remove, remove them from the end
    while k > 0:
        st.pop()
        k -= 1

    # Build the result by joining the stack elements
    res = "".join(st)

    # Remove leading zeros
    res = res.lstrip("0")

    # If the result is empty, return '0'
    if not res:
        return "0"

    return res


# Test the function
print(Rem_K_Digits("1432219", 3))  # Expected output: "1219"
