'''
Given an integer array nums, return true if any value appears at 
least twice in the array,and return false if every element is distinct.
'''

class Solution:
    def containsDuplicate(self, nums: int) -> bool:
        for i in range(len(nums)-1):
            num = nums[i]
            if (num in nums[i+1:]):
                return True
            else:
                return False

s = Solution()
print(s.containsDuplicate([1,2,3,1]))
print(s.containsDuplicate([1,2,3,4]))
print(s.containsDuplicate([2,14,18,22,22]))