class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ans = 0
        visited = set()
        rows, cols = self.findNeighbors(grid)
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    visited.add((r, c))
                    count = self.dfs(grid, r, c, visited, rows, cols)
                    if count > 1:
                        ans += count
        return ans
   
    def dfs(self, grid, r, c, visited, rows, cols):
        count = 1
        neighs = [(r, nc) for nc in rows[r] if nc != c] + [(nr, c) for nr in cols[c] if nr != r]
        for nr, nc in neighs:
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1 and (nr, nc) not in visited:
                visited.add((nr, nc))
                count += self.dfs(grid, nr, nc, visited, rows, cols)
        return count

    def findNeighbors(self, grid):
        rows = defaultdict(list)
        cols = defaultdict(list)
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    rows[r].append(c)
                    cols[c].append(r)
        return rows, cols