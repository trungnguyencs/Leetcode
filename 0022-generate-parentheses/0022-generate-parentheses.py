class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = []
        self.backtrack([], 0, 0, n)
        return self.ans

    def backtrack(self, arr, openCount, closeCount, n):
        if openCount == closeCount == n:
            self.ans.append(''.join(arr))
            return
        if closeCount > openCount or openCount > n:
            return
        self.backtrack(arr + ['('], openCount + 1, closeCount, n)
        self.backtrack(arr + [')'], openCount, closeCount + 1, n)