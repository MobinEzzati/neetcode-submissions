class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        s = sorted(s)
        t = sorted(t)
        counter = 0
        
        for i, j in zip(s,t):
            if i != j :
                counter = counter + 1 
        
        if counter > 0 :
            return False 
        
        return True
            
        