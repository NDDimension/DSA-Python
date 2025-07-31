def Palindrome(i):
    if i >= n // 2:
        return True

    if s[i] != s[n - i - 1]:
        return False
    return Palindrome(i + 1)


s = input("Enter a String: ")
n = len(s)
print(f'String "{s}" is Palindrome ? => {Palindrome(0)}')
