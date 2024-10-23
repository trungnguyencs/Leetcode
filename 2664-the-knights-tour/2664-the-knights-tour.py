from copy import deepcopy

class Solution:
    def tourOfKnight(self, R: int, C: int, r: int, c: int) -> List[List[int]]:
        board = [[-1]*C for _ in range(R)]
        board[r][c] = 0
        self.backtrack(board, r, c, 1)
        return board
    
    def backtrack(self, board, r, c, i):
        R, C = len(board), len(board[0])
        if i == R * C:
            return True
        neighs = [(r-2, c-1), (r-2, c+1),\
                  (r-1, c-2), (r-1, c+2),\
                  (r+1, c-2), (r+1, c+2),\
                  (r+2, c-1), (r+2, c+1),\
                 ]
        for nr, nc in neighs:
            if 0 <= nr < R and 0 <= nc < C and board[nr][nc] == -1:
                board[nr][nc] = i
                if self.backtrack(board, nr, nc, i + 1): return True
                board[nr][nc] = -1
        return False