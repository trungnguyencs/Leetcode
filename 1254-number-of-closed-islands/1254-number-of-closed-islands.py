class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        islands = 0
        for r in range(len(grid)):
            if grid[r][0] == 0:
                self.dfs(grid, r, 0)
            if grid[r][C - 1] == 0:
                self.dfs(grid, r, C - 1)
        for c in range(len(grid[0])):
            if grid[0][c] == 0:
                self.dfs(grid, 0, c)
            if grid[R - 1][c] == 0:
                self.dfs(grid, R - 1, c)
        for r in range(1, len(grid)):
            for c in range(1, len(grid[0])):
                if grid[r][c] == 0:
                    islands += 1
                    self.dfs(grid, r, c)
        return islands
        
    def dfs(self, grid, r, c):
        grid[r][c] = 2
        for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 0:
                self.dfs(grid, nr, nc)