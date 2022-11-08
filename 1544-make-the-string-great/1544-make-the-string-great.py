class Solution:
    def makeGood(self, s: str) -> str:
        i = 0
        stack = []
        for ch in s:
            if stack and abs(ord(ch) - ord(stack[-1])) == ord('a') - ord('A'):
                stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)