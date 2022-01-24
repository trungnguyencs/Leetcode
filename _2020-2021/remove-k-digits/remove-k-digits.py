class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack, attempts = [], k
        for ch in num:
            while stack and ord(ch) < ord(stack[-1]) and attempts > 0:
                stack.pop()
                attempts -= 1
            stack.append(ch)
        ans = ''.join(stack[:(len(num)-k)])
        return str(int(ans)) if ans else '0'
