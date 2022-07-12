"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        index = 0

        paren_dict = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        while index < len(s) and len(s) > 1:
            if s[index] in paren_dict:
                stack.append(s[index])
            else:
                if len(stack) == 0:
                    return False
                elif len(stack) > 0 and paren_dict[stack.pop()] != s[index]:
                    return False

            index += 1

        if len(stack) == 0 and len(s) > 1:
            return True
        return False


def main():
    s1 = "()"
    s2 = "()[]{}"
    s3 = "(]"
    s4 = "([)]"
    s5 = "{[]}"
    s6 = "["
    sol = Solution()
    print(sol.isValid(s1))  # True
    print(sol.isValid(s2))  # True
    print(sol.isValid(s3))  # False
    print(sol.isValid(s4))  # False
    print(sol.isValid(s5))  # True
    print(sol.isValid(s6))  # False


if __name__ == '__main__':
    main()
