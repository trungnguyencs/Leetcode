class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        distinctIslands = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    distinctIslands.add(self.dfs(grid, r, c, r, c, [(0, 0)]))
        return len(distinctIslands)
    
    def dfs(self, grid, r, c, r0, c0, path):
        grid[r][c] = 2
        neighs = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
        for nr, nc in neighs:
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                path.append((nr - r0, nc - c0)) # relative offset
                self.dfs(grid, nr, nc, r0, c0, path)
        return tuple(path)