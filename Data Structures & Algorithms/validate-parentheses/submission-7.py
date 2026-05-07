class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {")": "(", "}": "{", "]": "["}
        stack = deque()
        for char in s:
            if char not in mapping:
                stack.append(char)
            else:
                # If there's no matching opening bracket, return False immediately.
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
        return not stack