class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        isDuplicate = set()

        for item in nums:
            if item in isDuplicate:
                return True 
            
            isDuplicate.add(item)
        
        return False
        
        