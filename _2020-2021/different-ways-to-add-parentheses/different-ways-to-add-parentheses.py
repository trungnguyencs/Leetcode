class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if not any([ch in expression for ch in '+-*']): return [int(expression)]
        ret = []
        for i, ch in enumerate(expression):
            if ch.isdigit(): continue
            leftArr, rightArr = self.diffWaysToCompute(expression[:i]), self.diffWaysToCompute(expression[i+1:])
            if ch == '+': ret.extend([left + right for left in leftArr for right in rightArr])
            elif ch == '-': ret.extend([left - right for left in leftArr for right in rightArr])
            elif ch == '*': ret.extend([left * right for left in leftArr for right in rightArr])
        return ret