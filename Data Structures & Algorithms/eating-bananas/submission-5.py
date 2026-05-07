import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        low, high = 1, max(piles)
        result = high
        
        while low <= high:
            mid = (low + high) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / mid)
            
            if hours <= h:
                result = mid
                high = mid - 1
            else:
                low = mid + 1
        return result


        




        
            
            


       

       

            
            
            
            
            

            
            

        