class Solution:
    def isPalindrome(self, s: str) -> bool:



        clean_text = ''.join(char for char in s if char.isalnum())
        clean_text = clean_text.lower()
        leftPointer = 0
        rightPointer = len(clean_text) - 1
        while leftPointer < rightPointer :





            if clean_text[rightPointer] != clean_text[leftPointer]:



                return False
   
            leftPointer = leftPointer + 1
            rightPointer = rightPointer - 1 
        return True




        