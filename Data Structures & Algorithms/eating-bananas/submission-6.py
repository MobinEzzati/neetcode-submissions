import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left, right = 1, max(piles)
        res = max(piles)

        while left <= right :
            total_piles = 0 
            k = (left + right) // 2 
            for item in piles :
                total_piles = total_piles + math.ceil(item / k)
            
            if total_piles <= h : 
                res = k
                right = k - 1 
            else :
                left = k + 1 
            
        return res



        




        
            
            


       

       

            
            
            
            
            

            
            

        