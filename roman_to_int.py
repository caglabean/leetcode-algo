"""
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        # Create a dictionary to hold the letters and their values
        letters = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IV': 5,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }
        num = 0
        i = 0
        # Iterate the string to calculate the integer equivalent
        while i <= len(s) - 1:
            if i == len(s) - 1:
                num += letters[s[i]]

            else:
                if letters[s[i]] < letters[s[i + 1]]:
                    num -= letters[s[i]]
                else:
                    num += letters[s[i]]
            i += 1
        return num


def main():
    s = "MCMXCIV"
    a = Solution()
    print(a.romanToInt(s))


if __name__ == '__main__':
    main()
