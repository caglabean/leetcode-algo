class Solution:

    @staticmethod
    def search(nums: list, target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if target <= nums[mid]:
                high = mid
            else:
                low = mid + 1

        if nums[low] == target:
            return low

        return -1


def main():
    s = Solution()
    print(s.search([-1, 0, 3, 5, 9, 12], 9))
    print(s.search([-1, 0, 3, 5, 9, 12], 2))
    print(s.search([2, 5], 5))
    print(s.search([-1, 0, 3, 5, 9, 12], 13))


if __name__ == "__main__":
    main()
