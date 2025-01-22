class Solution:
    def sumRemoteness(self, grid: List[List[int]]) -> int:
        totalSum = 0
        arr = []
        visited = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] != -1 and (r, c) not in visited:
                    visited.add((r, c))
                    regionSum, regionCount = self.dfs(grid, r, c, visited)
                    arr.append((regionSum, regionCount))
                    totalSum += regionSum
        return sum(regionCount * (totalSum - regionSum) for regionSum, regionCount in arr)

    def dfs(self, grid, r, c, visited):
        sum, count = grid[r][c], 1
        neighs = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
        for nr, nc in neighs:
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] != -1 and (nr, nc) not in visited:
                visited.add((nr, nc))
                s, c = self.dfs(grid, nr, nc, visited)
                sum += s
                count += c
        return sum, count