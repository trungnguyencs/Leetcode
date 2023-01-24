class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        q = deque([(1, 0)])
        visited = set([1])
        while q:
            cur, d = q.popleft()
            if cur == n**2: return d
            for nxt in range(cur + 1, 1 + min(cur + 6, n**2)):
                if self.getBoardValue(nxt, board) != -1:
                    nxt = self.getBoardValue(nxt, board)
                if nxt not in visited:
                    visited.add(nxt)
                    q.append((nxt, d + 1))
        return -1
        
    def getBoardValue(self, x, board):
        n = len(board)
        r = (n - 1) - (x - 1)//n
        c = (x - 1) % n if r % 2 != n % 2 else (n - 1) - (x - 1) % n
        return board[r][c]