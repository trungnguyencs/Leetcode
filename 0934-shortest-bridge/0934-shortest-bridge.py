class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        q = deque([])
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    q.append((r, c))
                    self.dfs(grid, r, c, q)
                    return self.bfs(grid, q)
            
    def dfs(self, grid, r, c, q):
        grid[r][c] = 2
        neighs = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
        for nr, nc in neighs:
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                if self.nearWater(grid, nr, nc):
                    q.append((nr, nc))
                self.dfs(grid, nr, nc, q)

    def bfs(self, grid, q):
        d = 0
        visited = set()
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                neighs = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
                for nr, nc in neighs:
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                        if grid[nr][nc] == 1: return d
                        if grid[nr][nc] == 0 and (nr, nc) not in visited:
                            q.append((nr, nc))
                            visited.add((nr, nc))
            d += 1       

    def nearWater(self, grid, r, c):
        neighs = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
        for nr, nc in neighs:
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 0:
                return True
        return False