class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_val = 0
        for i in range(len(prices) -1  ,-1,-1):
            for j in range( i - 1, -1 , -1 ):

                current = 0
            
                if prices[i] > prices[j]:

                    current = prices[i] - prices[j]
            
                max_val = max(max_val,current)
        
        return max_val
            
        


        

               
        
            
            


        