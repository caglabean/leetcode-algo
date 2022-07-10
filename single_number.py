'''
Given a non-empty array of integers nums, every element 
appears twice except for one. Find that single one.

You must implement a solution with a linear runtime 
complexity and use only constant extra space.
'''

class Solution:
    def singleNumber(self, nums: int) -> int:
        # Check if number at current index exists in 
        # the rest of the list starting from next index
        for num in nums:
            if num not in nums[nums.index(num)+1:]:
                return num
    

s = Solution()
print(s.singleNumber([2,2,1]))
print(s.singleNumber([4,1,2,1,2]))
print(s.singleNumber([1]))
