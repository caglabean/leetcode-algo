class Solution:

    @staticmethod
    def searchInsert(nums: int, target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid
        if nums[low] >= target:
            return low
        else:
            return low + 1


def main():
    s = Solution()
    print(s.searchInsert([1, 3, 5, 6], 5))
    print(s.searchInsert([1, 3, 5, 6], 2))
    print(s.searchInsert([1, 3, 5, 6], 7))


if __name__ == '__main__':
    main()
