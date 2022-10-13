class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = []
        self.backtrack([], 0, 0, n)
        return self.ans
        
    def backtrack(self, arr, openCount, closeCount, n):
        if openCount > n or openCount < closeCount: return
        if openCount == closeCount == n:
            self.ans.append(''.join(arr))
            return
        self.backtrack(arr + ['('], openCount + 1, closeCount, n)
        self.backtrack(arr + [')'], openCount, closeCount + 1, n)