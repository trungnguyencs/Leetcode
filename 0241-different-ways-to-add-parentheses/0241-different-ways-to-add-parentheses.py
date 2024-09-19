class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        return self.dfs(expression, 0, len(expression) - 1)
        
    def dfs(self, s, i, j):
        if s[i:j+1].isnumeric():
            return [int(s[i:j+1])]
        ret = []
        for k in range(i+1, j):
            if s[k] not in '+-*': continue
            leftArr = self.dfs(s, i, k - 1)
            rightArr = self.dfs(s, k + 1, j)
            if s[k] == '+':
                ret.extend([left + right for left in leftArr for right in rightArr])
            if s[k] == '-':
                ret.extend([left - right for left in leftArr for right in rightArr])
            if s[k] == '*':
                ret.extend([left * right for left in leftArr for right in rightArr])
        return ret