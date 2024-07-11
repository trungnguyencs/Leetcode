class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch == ')':
                q = []
                while stack and stack[-1] != '(':
                    q.append(stack.pop())
                stack.pop()
                stack += q
            else:
                stack.append(ch)
        return ''.join(stack)