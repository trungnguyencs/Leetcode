class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        # on a new grid of size (3*R) * (3*C):
        # represent '/' as [1, 1, 0]
        #                  [1, 0, 1]
        #                  [0, 1, 1]
        # represent '/' as [0, 1, 1]
        #                  [1, 0, 1]
        #                  [1, 1, 0]
        # then the problem becomes finding the number of islands
        R, C = len(grid), len(grid[0])
        newGrid = [[1]*(3*C) for _ in range(3*R)]
        for r in range(R):
            for c in range(C):
                if grid[r][c] == '\\':
                    newGrid[3*r][3*c] = newGrid[3*r+1][3*c+1] = newGrid[3*r+2][3*c+2] = 0
                if grid[r][c] == '/':
                    newGrid[3*r+2][3*c] = newGrid[3*r+1][3*c+1] = newGrid[3*r][3*c+2] = 0
        return self.numberOfIslands(newGrid)
    
    def numberOfIslands(self, grid):
        islandCount = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    islandCount += 1
                    self.dfs(grid, r, c)
        return islandCount
    
    def dfs(self, grid, r, c):
        grid[r][c] = 2
        neighs = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
        for nr, nc in neighs:
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                self.dfs(grid, nr, nc)