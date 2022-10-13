class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for ch in num:
            while k > 0 and stack and ch < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(ch)
        ans = ''.join(stack[:len(stack) - k]).lstrip('0')
        return "0" if not ans else ans