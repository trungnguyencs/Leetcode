class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for d in path.split('/'):
            if d not in ['.', '..', '']: stack.append(d)
            elif stack and d == '..': stack.pop()
        return '/' + '/'.join(stack)