class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1: return self.dfs(grid, r, c)
            
    def dfs(self, grid, r, c):
        grid[r][c] = 2
        perimeters = 4
        neighs = [[r-1,c], [r+1,c], [r,c-1], [r,c+1]]
        for nr, nc in neighs:
            if 0<=nr<len(grid) and 0<=nc<len(grid[0]):
                if grid[nr][nc] == 1:
                    perimeters += self.dfs(grid, nr, nc) - 1
                elif grid[nr][nc] == 2:
                    perimeters -= 1
        return perimeters
    