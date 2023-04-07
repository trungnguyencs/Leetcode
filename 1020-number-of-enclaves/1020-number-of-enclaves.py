class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        area = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    tmp = self.dfs(grid, r, c)
                    if tmp != float('inf'):
                        area += tmp
        return area
        
    def dfs(self, grid, r, c):
        grid[r][c] = 2
        area = float('inf') if r in [0, len(grid) - 1] or c in [0, len(grid[0]) - 1] else 1
        for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                area += self.dfs(grid, nr, nc)
        return area