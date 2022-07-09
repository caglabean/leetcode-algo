'''
Given an array, rotate the array to the right by k steps, 
where k is non-negative.
'''
class Solution:
    def rotate(self, nums: int, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        1,2,3,4,5,6,7
        k=3
        5,6,7,1,2,3,4
        '''
        k = k % len(nums)
        temp=[]
        for i in range(len(nums)):
            temp.append(nums[i])
        for i in range(len(nums)):
            if((i+k) >= len(nums)):
                nums[(i+k)-len(nums)]=temp[i]
            else:
                nums[i+k]=temp[i]
        return nums

s = Solution()
print(s.rotate([-1,-100,3,99],2))
print(s.rotate([1,2,3,4,5,6,7],3))
print(s.rotate([1, 3, 5, 7, 9],2))


        