class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        arr = ['' for _ in range(len(s))]
        stack = []
        for i, ch in enumerate(s):
            if ch not in '()':
                arr[i] = ch
            if ch == '(':
                stack.append(i)
            if ch == ')' and stack:
                arr[stack.pop()] = '('
                arr[i] = ')'
        return ''.join(arr)
                
            
