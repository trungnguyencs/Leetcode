class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.solve()
        
    def solve(self):
        r, c = self.findNextEmpty()
        if r == c == -1: return True
        for num in "123456789":
            if not self.isSafe(r, c, num): continue
            self.board[r][c] = num
            if self.solve(): return True
            self.board[r][c] = '.'
        return False
        
    def findNextEmpty(self):
        for r in range(9):
            for c in range(9):
                if self.board[r][c] == '.': return r, c
        return -1, -1
    
    def isSafe(self, r, c, num):
        return self.isValidRow(r, num) and self.isValidCol(c, num) and self.isValidSquare(r, c, num)
    
    def isValidRow(self, r, num):
        return num not in self.board[r]
        
    def isValidCol(self, c, num):
        return num not in [self.board[r][c] for r in range(9)]
        
    def isValidSquare(self, r, c, num):
        return num not in [self.board[squareRow][squareCol] for squareRow in range(r//3*3, r//3*3 + 3) for squareCol in range(c//3*3, c//3*3 + 3)]