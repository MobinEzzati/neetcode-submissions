from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        
        test = Counter(s)
        test1 = Counter(t)
        
        if Counter(s) == Counter(t) :
            return True
        
        return False
        