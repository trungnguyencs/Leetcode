class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for r in range(len(board)):
            for c in range(len(board[0])):
                count = self.countLiveNeighs(board, r, c)
                if board[r][c] == 1 and (count < 2 or count > 3):
                    board[r][c] = -1
                elif board[r][c] == 0 and count == 3:
                    board[r][c] = 2
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 2: board[r][c] = 1
                elif board[r][c] == -1: board[r][c] = 0
        
    def countLiveNeighs(self, board, i, j):
        neighs = [[i-1,j-1],[i-1,j],[i-1,j+1],
                  [i,j-1],[i,j+1],
                  [i+1,j-1],[i+1,j],[i+1,j+1]]
        return sum([board[ni][nj] in [1, -1] for ni, nj in neighs if 0<=ni<len(board) and 0<=nj<len(board[0])])