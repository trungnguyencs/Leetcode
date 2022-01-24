class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.backtrack(board, i, j, 0, word): return True
        return False
    
    def backtrack(self, board, i, j, idx, word):
        if idx == len(word): return True
        if not (0<=i<len(board) and 0<=j<len(board[0]) and board[i][j] == word[idx]): return False
        tmp, board[i][j] = board[i][j], '#'
        ret = self.backtrack(board, i-1, j, idx+1, word) or\
            self.backtrack(board, i+1, j, idx+1, word) or\
            self.backtrack(board, i, j-1, idx+1, word) or\
            self.backtrack(board, i, j+1, idx+1, word)
        board[i][j] = tmp
        return ret