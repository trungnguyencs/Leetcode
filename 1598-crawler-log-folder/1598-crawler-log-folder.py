class Solution:
    def minOperations(self, logs: List[str]) -> int:
        level = 0
        for log in logs:
            if log == './': continue
            if log != '../':
                level += 1
            elif level > 0:
                level -= 1
        return level