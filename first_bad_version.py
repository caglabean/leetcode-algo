class Solution():
    def isBadVersion(self, n: int) -> int:
        if n == 0:
            return False
        return True

    def firstBadVersion(self, n: int, versions: list) -> int:
        # 0 0 0 1 1 1 1 1 1
        # 1 2 3 4 5 6 7 8 9
        low = 0
        high = n - 1
        while low < high:
            mid = (low + high) // 2
            if self.isBadVersion(versions[mid]):
                high = mid
            else:
                low = mid + 1
        return low + 1


def main():
    s = Solution()
    print("First bad version was published on the " + str(s.firstBadVersion(9, [0, 0, 0, 1, 1, 1, 1, 1, 1])) + ". day.")


if __name__ == '__main__':
    main()
