class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash = {}
        t_hash = {}

        for item_s in s:
            if item_s in s_hash :
                s_hash[item_s] += 1
            else :
                s_hash[item_s] = 1
        for item_t in t :    
            if item_t in t_hash :
                t_hash[item_t] += 1
            else :
                t_hash[item_t] = 1 
        
        if t_hash == s_hash :
            return True 
        
        return False




        
        