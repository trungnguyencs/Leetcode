class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        maxArea = 0
        visited = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] != 0:
                    visited.add((r, c))
                    maxArea = max(maxArea, self.dfs(grid, r, c, visited))
        return maxArea

    def dfs(self, grid, r, c, visited):
        area = grid[r][c]
        neighs = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
        for nr, nc in neighs:
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[r][c] != 0 and (nr, nc) not in visited:
                visited.add((nr, nc))
                area += self.dfs(grid, nr, nc, visited)
        return area