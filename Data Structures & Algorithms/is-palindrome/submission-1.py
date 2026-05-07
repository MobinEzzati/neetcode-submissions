class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0 
        refinedText = s.replace(" ","")
        refindedText = refinedText.lower()
        for char in s : 
            if not char.isalnum():
                refindedText = refindedText.replace(char,"")
        
        right = len(refindedText) - 1

        while left < right :

            if refindedText[left] != refindedText[right]:
                return False
            
            left = left + 1 
            right = right - 1
        
        return True 

                
     
        