class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        self.dfs(board, click[0], click[1])
        return board
        
    def dfs(self, board, r, c):
        if board[r][c] == 'M':
            board[r][c] = 'X'
            return
        neighs = ((r-1,c),(r+1,c),(r,c-1),(r,c+1),\
                  (r-1,c-1),(r-1,c+1),(r+1,c-1),(r+1,c+1))
        mCount = 0
        for x, y in neighs:
            if 0<=x<len(board) and 0<=y<len(board[0]) and board[x][y] == 'M':
                mCount += 1
        if mCount:
            board[r][c] = str(mCount)
        else:
            board[r][c] = 'B'
            for x, y in neighs:
                if 0<=x<len(board) and 0<=y<len(board[0]) and board[x][y] == 'E':
                    self.dfs(board, x, y)
            
