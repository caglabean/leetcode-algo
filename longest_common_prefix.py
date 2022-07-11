"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""


class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        max_prefix = ""
        shortest = min(strs, key=len)  # Find the shortest word
        check = False
        for i in range(len(shortest)):  # Traverse the letters
            current = shortest[i]
            for j in range(len(strs)):
                if strs[j][i] == current:
                    check = True
                else:
                    return max_prefix
            if check:
                max_prefix += current

        return max_prefix


def main():
    strs1 = ["flower", "flow", "flight"]
    strs2 = ["dog", "racecar", "car"]
    strs3 = ["ab", "a"]
    strs4 = ["cir", "car"]
    sol = Solution()
    print(sol.longestCommonPrefix(strs1))
    print(sol.longestCommonPrefix(strs2))
    print(sol.longestCommonPrefix(strs3))
    print(sol.longestCommonPrefix(strs4))


if __name__ == '__main__':
    main()
