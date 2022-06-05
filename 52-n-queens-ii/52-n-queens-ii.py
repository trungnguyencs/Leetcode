class Solution:
    def totalNQueens(self, n: int) -> int:
        self.ans = 0
        self.backtrack(0, n, set(), set(), set())
        return self.ans
        
    def backtrack(self, r, n, cols, diag, codiag):
        if r == n:
            self.ans += 1
            return
        for c in range(n):
            if c in cols or (r + c) in diag or (r - c) in codiag: continue
            cols.add(c); diag.add(r + c); codiag.add(r - c)
            self.backtrack(r + 1, n, cols, diag, codiag)
            cols.remove(c); diag.remove(r + c); codiag.remove(r - c)