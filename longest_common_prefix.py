"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""


class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        pass


def main():
    strs1 = ["flower", "flow", "flight"]
    strs2 = ["dog", "racecar", "car"]
    sol = Solution()
    print(sol.longestCommonPrefix(strs1))
    print(sol.longestCommonPrefix(strs2))


if __name__ == '__main__':
    main()
