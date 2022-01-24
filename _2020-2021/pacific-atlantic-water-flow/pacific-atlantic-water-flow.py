class Solution:
    def pacificAtlantic(self, board: List[List[int]]) -> List[List[int]]:
        R, C = len(board), len(board[0])
        visitedPacific = set()
        visitedAtlantic = set()
        for r in range(R):
            self.dfs(board, r, 0, visitedPacific)
            self.dfs(board, r, C - 1, visitedAtlantic)
        for c in range(C):
            self.dfs(board, 0, c, visitedPacific)
            self.dfs(board, R - 1, c, visitedAtlantic)
        return visitedPacific.intersection(visitedAtlantic)
        
    def dfs(self, board, r, c, visited):
        visited.add((r, c))
        neighs = [[r-1, c], [r+1, c], [r, c-1], [r, c+1]]
        for nr, nc in neighs:
            if not 0 <= nr < len(board) or not 0 <= nc < len(board[0]) or (nr, nc) in visited or board[nr][nc] < board[r][c]:
                continue
            self.dfs(board, nr, nc, visited) 