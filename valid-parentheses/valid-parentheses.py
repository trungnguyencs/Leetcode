class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'(':')', '[':']', '{':'}'}
        stack = []
        for ch in s:
            if ch in '([{':
                stack.append(ch)
            elif not stack or dic[stack.pop()] != ch:
                return False
        return not stack
        
        
