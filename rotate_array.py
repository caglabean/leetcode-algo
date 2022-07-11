"""
Given an array, rotate the array to the right by k steps,
where k is non-negative.
"""


class Solution:
    def rotate(self, nums: list, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        1,2,3,4,5,6,7
        k=3
        5,6,7,1,2,3,4
        '''
        # In case k is bigger than size of array, get remainder to
        # iterate the list
        k %= len(nums)

        return nums[len(nums)-k:]+nums[:len(nums)-k]

def main():
    s = Solution()
    print(s.rotate([-1, -100, 3, 99], 2))
    print(s.rotate([1, 2, 3, 4, 5, 6, 7], 3))
    print(s.rotate([1, 3, 5, 7, 9], 2))


if __name__ == '__main__':
    main()
