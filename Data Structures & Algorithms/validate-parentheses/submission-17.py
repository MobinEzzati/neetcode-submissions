
class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {"}":"{", "]":"[",")":"("}
        opens = ["(","[","{"]
        stack = []

        if len(s) <= 1 :
            return False

        for character in s:
            if character in "([{" : 
                stack.append(character)
            else:
                if stack : 
                    lastItem = stack[-1]
                    if lastItem == mapping[character] :
                        stack.pop()
                    else :
                        return False 
                else:
                    stack.append(character)
        
        if len(stack) == 0 :
            return True
        
        return False
        # print(stack)
        
        


        
        