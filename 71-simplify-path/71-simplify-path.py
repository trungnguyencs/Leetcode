class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for item in path.split('/'):
            if item not in ['', '.', '..']:
                stack.append(item)
            elif item == '..' and stack:
                stack.pop()
        return '/' + '/'.join(stack)