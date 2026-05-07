class Solution:
    def findMin(self, nums: List[int]) -> int:

        current = nums[0]

        for item in nums:

            if item < current: 

                current = item
        

        return current

        
        