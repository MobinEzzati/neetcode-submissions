class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i, curr_item in enumerate(temperatures):
            while stack and curr_item > stack[-1][0] :
                 item , index = stack.pop()
                 result[index] = (i - index)
            stack.append([curr_item,i])
        return result       
        

        
                
            
        
        