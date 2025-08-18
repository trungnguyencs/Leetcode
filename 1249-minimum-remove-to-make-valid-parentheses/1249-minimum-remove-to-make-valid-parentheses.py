class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        ans = ['' for _ in range(len(s))]
        for i, ch in enumerate(s):
            if ch not in '()':
                ans[i] = ch
            elif ch == '(':
                stack.append(i)
            elif stack:
                ans[stack.pop()] = '('
                ans[i] = ')'
        return ''.join(ans)