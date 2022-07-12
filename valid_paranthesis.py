"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        open_parentheses = ['(', '[', '{']
        close_parentheses = [')', ']', '}']
        i = 0
        while i < len(s) - 1:
            if s[i + 1] in close_parentheses and open_parentheses.index(s[i]) == close_parentheses.index(s[i + 1]):
                i += 2

            else:
                return False
        return True


def main():
    s1 = "()"
    s2 = "()[]{}"
    s3 = "(]"
    s4 = "([)]"
    s5 = "{[]}"
    sol = Solution()
    print(sol.isValid(s1))  # True
    print(sol.isValid(s2))  # True
    print(sol.isValid(s3))  # False
    print(sol.isValid(s4))  # False
    print(sol.isValid(s5))  # True


if __name__ == '__main__':
    main()
