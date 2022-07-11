"""
Given an integer array nums sorted in non-decreasing order,
return an array of the squares of each number sorted in non-decreasing order.
"""


class Solution:
    def sortedSquares(self, nums: list) -> list:

        for i in range(len(nums)):
            nums[i] = nums[i] * nums[i]

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] >= nums[j]:
                    temp = nums[j]
                    nums[j] = nums[i]
                    nums[i] = temp
        return nums


def main():
    s = Solution()
    print(s.sortedSquares([-4, -1, 0, 3, 10]))  # [0,1,9,16,100]
    print(s.sortedSquares([-7, -3, 2, 3, 11]))  # [4,9,9,49,121]


if __name__ == '__main__':
    main()
