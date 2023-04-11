class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch != '*':
                stack.append(ch)
            elif stack:
                stack.pop()
        return ''.join(stack)