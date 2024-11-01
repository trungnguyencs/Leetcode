class Solution:
    def makeFancyString(self, s: str) -> str:
        stack = []
        for ch in s:
            if len(stack) > 1 and stack[-1] == stack[-2] == ch:
                stack.pop()
            stack.append(ch)
        return ''.join(stack)