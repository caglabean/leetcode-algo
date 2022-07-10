'''
Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must appear as many times as it shows in both arrays 
and you may return the result in any order.
'''
class Solution:
    def intersect(self, nums1: int, nums2: int) -> int:
        res = []   # Intersection array
        i = 0   # Current index of first array
        j = 0   # Current index of second array
        
        # Sort both arrays
        nums1.sort()
        nums2.sort()

        # Traverse both arrays to find intersections
        while (i < len(nums1) and j < len(nums2)):
            # If numbers at current indexes are equal, add
            # them to the resulting array
            if (nums1[i] == nums2[j]):
                res.append(nums1[i])
                i += 1
                j += 1
            # If nums2[j] is greater than nums1[i] then we should
            # increment i to check the bigger values in nums1
            elif (nums1[i] < nums2[j]):
                i += 1
            # If nums1[i] is greater than nums2[j] then we should
            # increment j to check the bigger values in nums2
            else:
                j += 1

        return res


s = Solution()
print(s.intersect([3,1,2],[1,3]))
print(s.intersect([1,2,2,1],[2,2]))


