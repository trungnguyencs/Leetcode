class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for ch in s:
            if ch == '(':
                stack.append(0)
            else:
                last = stack.pop()
                stack[-1] += 1 if last == 0 else last*2            
        return stack[0]