"""
"Palindrome Partitioning"

=> Given a string , partition it in such a way that the substring is palindrome.

=> Example:

string = "aab"
O/P => [a , a , b] , [aa , b]

Time Complexity : O( (2^n) *k*(n/2) )
Space Complexity : O(k * x)
"""


def PalindromePartition(string):
    res, path = [], []

    def partitioner(idx):
        if idx == len(string):
            res.append(path[:])
            return

        for i in range(idx, len(string)):
            if isPalindrome(string, idx, i):
                path.append(string[idx : i + 1])
                partitioner(i + 1)
                path.pop()

    def isPalindrome(string, start, end):
        while start <= end:
            if string[start] != string[end]:
                return False

            start += 1
            end -= 1

        return True

    partitioner(0)
    return res


sub = PalindromePartition("aab")
for s in sub:
    print(s)
