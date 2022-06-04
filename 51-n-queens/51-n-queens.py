class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.ans = []
        board = [['.']*n for _ in range(n)]
        self.backtrack(board, 0, set(), set(), set())
        return self.ans
        
    def backtrack(self, board, r, cols, diag, codiag):
        if r == len(board):
            self.ans.append([''.join(row) for row in board])
            return
        for c in range(len(board[0])):
            if c in cols or r + c in diag or r - c in codiag: continue
            board[r][c] = 'Q'
            cols.add(c); diag.add(r + c); codiag.add(r - c)
            self.backtrack(board, r + 1, cols, diag, codiag)
            board[r][c] = '.'
            cols.remove(c); diag.remove(r + c); codiag.remove(r - c)    