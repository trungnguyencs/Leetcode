class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        part = list(part)
        n = len(part)
        for ch in s:
            stack.append(ch)
            if len(stack) >= n and stack[-n:] == part:
                for _ in range(n):
                    stack.pop()
        return ''.join(stack)