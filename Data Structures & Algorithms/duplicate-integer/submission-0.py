class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visited = {}
        for item in nums:

            if item in visited:
                 visited[item] += 1 
            else:
                 visited[item] = 1 
            
            if visited[item] > 1:
                return True 
        
        return False   

        