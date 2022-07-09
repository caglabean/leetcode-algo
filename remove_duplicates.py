class Solution:
    def removeDuplicates(self, nums):
        current = None  # Keeps track of unique values
        count = 0   # Number of unique values
        for num in nums:
            '''
            If current value is not equal to the next value in the array,
            then current value is unique.
            '''
            if (current != num):   
                current = num
                nums[count] = current   # Modify the front of the array to keep only the unique values
                count +=1
                
        return nums[:count] # Return the modified front of the array


s = Solution()
print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))