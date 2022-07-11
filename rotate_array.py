"""
Given an array, rotate the array to the right by k steps,
where k is non-negative.
"""


class Solution:
    def rotate(self, nums: list, k: int) -> None:
        # In case k is bigger than size of array, get remainder to
        # iterate the list
        temp = []
        for num in nums:
            temp.append(num)

        k %= len(nums)

        temp = nums[len(nums) - k:] + nums[:len(nums) - k]
        for i in range(len(nums)):
            nums[i] = temp[i]


def main():
    s = Solution()

    l1 = [-1, -100, 3, 99]
    l2 = [1, 2, 3, 4, 5, 6, 7]
    l3 = [1, 3, 5, 7, 9]

    s.rotate(l1, 2)
    s.rotate(l2, 3)
    s.rotate(l3, 2)

    print(l1)
    print(l2)
    print(l3)


if __name__ == '__main__':
    main()
