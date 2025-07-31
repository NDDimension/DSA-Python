"""
"Roman to Integer and Vice Versa

=> Given roman convert to Integer and same thing way around.
"""


def romanToInt(s):
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    ans = 0
    for i in range(len(s) - 1):
        if roman[s[i]] < roman[s[i + 1]]:
            ans -= roman[s[i]]
        else:
            ans += roman[s[i]]
    ans += roman[s[-1]]

    return ans


def intToRoman(num):
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    roman = ""
    i = 0
    while num > 0:
        count = num // val[i]
        roman += syms[i] * count
        num -= val[i] * count
        i += 1
    return roman


s = "MCMXCIV"
print(romanToInt(s))
