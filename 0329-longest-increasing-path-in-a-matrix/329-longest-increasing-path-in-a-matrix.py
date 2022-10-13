class Solution:
    def longestIncreasingPath(self, grid: List[List[int]]) -> int:
        maxPath = 1
        self.grid = grid
        for r in range(len(self.grid)):
            for c in range(len(self.grid[0])):
                maxPath = max(maxPath, self.dp(r, c))
        return maxPath
        
    @cache
    def dp(self, r, c):
        maxPath = 1
        neighs = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
        for nr, nc in neighs:
            if 0 <= nr < len(self.grid) and 0 <= nc < len(self.grid[0]) and self.grid[r][c] > self.grid[nr][nc]:
                maxPath = max(maxPath, 1 + self.dp(nr, nc)) 
        return maxPath