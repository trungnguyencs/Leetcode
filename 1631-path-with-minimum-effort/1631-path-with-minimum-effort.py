class Solution:
    def minimumEffortPath(self, grid: List[List[int]]) -> int:
        dp = [[float('inf')]*len(grid[0]) for _ in range(len(grid))]
        dp[0][0] = 0
        q = deque([(0, 0 ,0)])
        while q:
            r, c, d = q.popleft()
            neigh = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
            for nr, nc in neigh:
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                    newD = max(d, abs(grid[r][c] - grid[nr][nc]))
                    if newD < dp[nr][nc]:
                        dp[nr][nc] = newD
                        q.append((nr, nc, newD))
        return dp[-1][-1]