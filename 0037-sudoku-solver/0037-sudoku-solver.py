class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rowDic, colDic, squareDic, empties = self.buildDic(board)
        self.backtrack(board, rowDic, colDic, squareDic, empties, 0)

    def backtrack(self, board, rowDic, colDic, squareDic, empties, i):
        if i == len(empties):
            return True  # solved
        r, c = empties[i] # further optimization: choose cell with least #branchings
        for d in '123456789':
            if d in rowDic[r] or d in colDic[c] or d in squareDic[(r//3, c//3)]:
                continue
            # place
            board[r][c] = d
            rowDic[r].add(d)
            colDic[c].add(d)
            squareDic[(r//3, c//3)].add(d)
            # recurse and short-circuit on success
            if self.backtrack(board, rowDic, colDic, squareDic, empties, i + 1):
                return True
            # undo
            board[r][c] = '.'
            rowDic[r].remove(d)
            colDic[c].remove(d)
            squareDic[(r//3, c//3)].remove(d)
        return False

    def buildDic(self, board):
        rowDic = defaultdict(set)
        colDic = defaultdict(set)
        squareDic = defaultdict(set)
        empties = [] #loop over a set while removing its elements is troublesome, so use a list with index instead
        for r in range(9):
            for c in range(9):
                v = board[r][c]
                if v == '.':
                    empties.append((r, c))
                else:
                    rowDic[r].add(v)
                    colDic[c].add(v)
                    squareDic[(r//3, c//3)].add(v)
        return rowDic, colDic, squareDic, empties

# Old solution (non-optimal)
"""
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.solve(board)
        
    def solve(self, board): # backtracking method
        r, c = self.findFirstBlank(board)
        if r == c == -1: return True
        for num in "123456789":
            if not self.isSafe(board, r, c, num): continue
            board[r][c] = num
            if self.solve(board): return True
            board[r][c] = '.' 
        return False
    
    def findFirstBlank(self, board):
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.': return r, c
        return -1, -1
        
    def isSafe(self, board, r, c, num):
        return self.isValidRow(board, r, num) and self.isValidCol(board, c, num) and self.isValidSquare(board, r, c, num)
        
    def isValidRow(self, board, r, num):
        return num not in board[r]
        
    def isValidCol(self, board, c, num):
        return num not in [board[r][c] for r in range(9)]
    
    def isValidSquare(self, board, r, c, num):
        return num not in [board[squareRow][squareCol] for squareRow in range(r//3*3, r//3*3 + 3) for squareCol in range(c//3*3, c//3*3 + 3)]
"""