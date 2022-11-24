class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        letters = [ch for row in board for ch in row if ch in word]
        if Counter(letters) < Counter(word): return False
        for r in range(len(board)):
            for c in range(len(board[0])):
                 if self.backtrack(board, r, c, word, 0): return True
        return False
                
    def backtrack(self, board, r, c, word, i):
        if i == len(word): return True
        if not 0 <= r < len(board) or not 0 <= c < len(board[0]) or board[r][c] != word[i]: return False
        board[r][c] = '#'
        if any(self.backtrack(board, nr, nc, word, i+1) for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]): return True
        board[r][c] = word[i]
        return False