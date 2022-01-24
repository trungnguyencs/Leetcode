class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    count += 1
                    self.dfs(grid, r, c)
        return count
        
    def dfs(self, grid, r, c):
        grid[r][c] = '#'
        neighs = ((r-1, c), (r+1, c), (r, c-1), (r, c+1))
        for nr, nc in neighs:
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == '1':
                self.dfs(grid, nr, nc)