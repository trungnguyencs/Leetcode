class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        stack = []
        for s in path:
            if s in ['', '.']:
                continue
            elif s == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(s)
        return ''.join('/' + '/'.join(stack))