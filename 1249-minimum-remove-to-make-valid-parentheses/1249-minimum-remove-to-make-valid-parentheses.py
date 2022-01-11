class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        ans = ['']*len(s)
        stack = []
        for i, ch in enumerate(s):
            if ch not in '()':
                ans[i] = ch
            elif ch == '(':
                stack.append(i)
            elif stack:
                ans[stack.pop()] = '('
                ans[i] = ')'
        return ''.join(ans)