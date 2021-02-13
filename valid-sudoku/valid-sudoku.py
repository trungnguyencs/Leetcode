class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, squares = defaultdict(set), defaultdict(set), defaultdict(set)
        for r in range(len(board)):
            for c in range(len(board[0])):
                num = board[r][c]
                if num == '.': continue
                if num in rows[r] or num in cols[c] or num in squares[(r//3, c//3)]: return False
                rows[r].add(num)
                cols[c].add(num)
                squares[(r//3, c//3)].add(num)
        return True