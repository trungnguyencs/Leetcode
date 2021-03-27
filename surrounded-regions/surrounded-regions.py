class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        R, C = len(board), len(board[0])
        for r in range(R):
            if board[r][0] == 'O': self.dfs(board, r, 0)
            if board[r][C-1] == 'O': self.dfs(board, r, C-1)
        for c in range(C):
            if board[0][c] == 'O': self.dfs(board, 0, c)
            if board[R-1][c] == 'O': self.dfs(board, R-1, c)
        for r in range(R):
            for c in range(C):
                if board[r][c] == 'O': board[r][c] = 'X'
                if board[r][c] == 'E': board[r][c] = 'O'
    
    def dfs(self, board, r, c):
        board[r][c] = 'E'
        neighs = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
        for x, y in neighs:
            if 0<=x<len(board) and 0<=y<len(board[0]) and board[x][y] == 'O':
                self.dfs(board, x, y)