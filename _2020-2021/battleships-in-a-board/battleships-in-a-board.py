class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        count = 0
        for r in range(len(board)):
            for c in range(len(board[0])):
                if r > 0 and board[r-1][c] == 'X':
                    continue
                if c > 0 and board[r][c-1] == 'X':
                    continue
                if board[r][c] == 'X':
                    count += 1
        return count