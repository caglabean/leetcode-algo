class Solution():
    def firstBadVersion(self, versions: list) -> int:
        low = 0
        high = len(versions) - 1
        while (low < high):
            mid = (low + high) // 2
            if versions[mid] > 0:
                low = mid + 1
            else:
                high = mid
        if versions[low] == 0:
            return low
        else:
            return -1


def main():
    s = Solution()
    print(s.firstBadVersion([1, 1, 1, 1, 1, 0, 0, 0]))


if __name__ == '__main__':
    main()
