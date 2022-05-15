class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        distinctIslands = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    distinctIslands.add(self.dfs(grid, r, c, 0, 0, []))
        return len(distinctIslands)
    
    def dfs(self, grid, r, c, offsetR, offsetC, offsets):
        grid[r][c] = '#'
        offsets.append((offsetR, offsetC))
        neighs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in neighs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                self.dfs(grid, nr, nc, offsetR + dr, offsetC + dc, offsets)
        return tuple(sorted(offsets))