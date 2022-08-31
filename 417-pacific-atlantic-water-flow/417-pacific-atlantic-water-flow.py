class Solution:
    def pacificAtlantic(self, grid: List[List[int]]) -> List[List[int]]:
        visitedPacific, visitedAtlantic = set(), set()
        for r in range(len(grid)):
            self.dfs(grid, r, 0, visitedPacific)
            self.dfs(grid, r, len(grid[0]) - 1, visitedAtlantic)
        for c in range(len(grid[0])):
            self.dfs(grid, 0, c, visitedPacific)
            self.dfs(grid, len(grid) - 1, c, visitedAtlantic)
        return visitedPacific.intersection(visitedAtlantic)
        
    def dfs(self, grid, r, c, visited):
        visited.add((r, c))
        neighs = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
        for nr, nc in neighs:
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] >= grid[r][c] and (nr, nc) not in visited:
                self.dfs(grid, nr, nc, visited)