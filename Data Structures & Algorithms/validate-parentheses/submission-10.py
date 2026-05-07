class Solution:
    def isValid(self, s: str) -> bool:


        para = {"}" : "{", "]":"[", ")":"("}
        stack = deque()
        for item in s :
            print(item)
            if item not in para :

                print(f"Item added:{item}")

                stack.append(item)
            else:

                print(f"else item here :{item}")

                if stack and stack[-1] == para[item]:
                    stack.pop()
                else:
                    return False
                 


        if len(stack) == 0 :
            return True
        else:
            return False 